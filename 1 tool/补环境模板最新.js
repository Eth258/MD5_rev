

const originalLog = Function.prototype.call.bind(console.log);


const v_log = function (...args) {
    // 使用原始引用直接调用，跳过可能被修改的 console.log
    return originalLog(console, ...args);
};

Window = function Window(){}

for (let name in global){
    switch(name){
        case "Window":
            continue;
        case "global":
            continue;
    }
    Window.prototype[name] = global[name];
    delete global[name]
}

//代理器
const myProxy = function myProxy(obj, name) {

    const myProxy_flag = 1

    const keyToString = function keyToString(propkey) {
        return typeof propkey === 'symbol' ? `[${propkey.toString().replace('Symbol(', '').replace(')', '')}]` : propkey;
    }

    // 辅助函数：处理属性值的序列化
    const serializeValue = function serializeValue(value, visited = new WeakSet()) {
        if (typeof value === 'symbol') {
            return value.toString().replace('Symbol(', '').replace(')', '');
        }
        if (typeof value === 'function') {
            const funcName = value.name || 'anonymous';
            return `[Function: ${funcName}]`;
        }
        if (typeof value === 'object' && value !== null) {
            if (visited.has(value)) {
                return '[Circular Reference]';
            }
            visited.add(value);
            const parts = [];
            Reflect.ownKeys(value).forEach((key) => {
                const keyStr = keyToString(key);
                const val = value[key];
                const serializedVal = serializeValue(val, visited);
                parts.push(`${JSON.stringify(keyStr)}:${serializedVal}`);
            });
            return `{${parts.join(',')}}`;
        }
        if (typeof value === 'number' || typeof value === 'boolean' || value === null) {
            return JSON.stringify(value);
        }
        if (typeof value === 'string') {
            return `"${value}"`;
        }
        return JSON.stringify(value);
    }

    const my_Proxy = function my_Proxy(obj, name) {
        if (myProxy_flag) {
            return new Proxy(obj, {
                defineProperty(target, propkey, propDesc) {
                    const keyStr = keyToString(propkey);
                    // 确保 propDesc 是有效的属性描述符对象
                    if (typeof propDesc !== 'object' || propDesc === null) {
                        console.warn(`${name} -> 定义属性时，属性描述符无效`);
                        return false;
                    }
                    const result = Reflect.defineProperty(target, propkey, propDesc);
                    const valueToLog = serializeValue(propDesc);
                    v_log(`${name} -> 定义了属性 ${keyStr}  值为 -> ${valueToLog}`);
                    return result;
                },
                deleteProperty(target, propkey) {
                    const keyStr = keyToString(propkey);
                    const result = Reflect.deleteProperty(target, propkey);
                    v_log(`对象 ${name} -> 删除了属性 ${keyStr}`);
                    return result;
                },
                // 其他拦截器方法保持不变
                get(target, propkey, receiver) {
                    const keyStr = keyToString(propkey);
                    const value = Reflect.get(target, propkey, receiver);
                    const valueToLog = serializeValue(value);
                    if (!Reflect.has(target, propkey)) {
                        v_log(`${name} -> 获取了属性 ${keyStr}  值为 -> ${valueToLog} 该属性不存在`);
                    } else {
                        v_log(`${name} -> 获取了属性 ${keyStr}  值为 -> ${valueToLog} 存在该属性`)
                    }
                    ;
                    if (typeof value === 'object' && value !== null) {
                        return my_Proxy(value, `${name} --> ${keyStr}`);
                    }
                    return value;
                },
                set(target, propkey, value, receiver) {
                    const keyStr = keyToString(propkey);
                    const result = Reflect.set(target, propkey, value, receiver);
                    const valueToLog = serializeValue(value);
                    v_log(`${name} -> 设置了属性 ${keyStr}  值为 -> ${valueToLog}`);
                    return result;
                },
                has(target, propkey) {
                    const keyStr = keyToString(propkey);
                    const result = Reflect.has(target, propkey);
                    v_log(`${name} -> 是否拥有属性 ${keyStr} -> ${result}`);
                    return result;
                },
                ownKeys(target) {
                    const keys = Reflect.ownKeys(target);
                    v_log(`${name} -> 获取了自身所有属性 -> ${keys.map(keyToString)}`);
                    return keys;
                },
                getOwnPropertyDescriptor(target, propkey) {
                    const keyStr = keyToString(propkey);
                    const descriptor = Reflect.getOwnPropertyDescriptor(target, propkey);
                    const valueToLog = serializeValue(descriptor);
                    if (!descriptor) {
                        v_log(`${name} -> 获取私有属性 ${keyStr} 的描述为 -> ${valueToLog} 该属性非私有或不存在`);
                    } else {
                        v_log(`${name} -> 获取私有属性 ${keyStr} 的描述为 -> ${valueToLog} 该私有属性存在`);
                    }
                    return descriptor;
                },
                preventExtensions(target) {
                    const result = Reflect.preventExtensions(target);
                    v_log(`${name} -> 被设置为不可添加属性`);
                    return result;
                },
                getPrototypeOf(target) {
                    const prototype = Reflect.getPrototypeOf(target);
                    const prototypeToLog = serializeValue(prototype)
                    if (prototype) {
                        v_log(`获取了 ${name} 对象的原型, 值为${prototypeToLog} 该原型存在`);
                    } else {
                        v_log(`获取了 ${name} 对象的原型, 值为${prototypeToLog} 该原型不存在`);
                    }
                    return prototype;
                },
                isExtensible(target) {
                    const result = Reflect.isExtensible(target);
                    v_log(`对象 ${name} 允许添加新的属性`);
                    return result;
                },
                setPrototypeOf(target, proto) {
                    const result = Reflect.setPrototypeOf(target, proto);
                    const valueToLog = serializeValue(proto);
                    v_log(`对象 ${name} 将 ${valueToLog} 设为原型`);
                    return result;
                },
                apply(target, object, args) {
                    if (object === null || object === undefined) {
                        console.warn(`调用 ${target.name} 方法时，上下文对象为 ${object}`);
                    }
                    const result = Reflect.apply(target, object, args);
                    const newArgs = args.map(val => serializeValue(val));
                    v_log(`正在运行apply的对象 ${serializeValue(object)} 调用了 ${target.name || 'anonymous'} 方法 并传入了 [${newArgs}] 参数 返回的结果为${result}`);
                    return result;
                },
                construct(target, args) {
                    const instance = Reflect.construct(target, args);
                    const serializedArgs = args.map(serializeValue);
                    v_log(
                        `正在创建构造函数 ${target.name || '匿名构造函数'} 的实例 传入了 ${serializedArgs.length ? serializedArgs.join(', ') : '无'} 参数 结果为 ${instance}`
                    );
                    return instance;
                }
            });
        } else {
            return obj
        }
    }

    return my_Proxy(obj, name)
}

const safeFunction = function safeFunction(func) {
    //处理安全函数
    Function.prototype.$call = Function.prototype.call;
    const $toString = Function.toString;
    const myFunction_toString_symbol = Symbol('('.concat('', ')'));

    const myToString = function myToString() {
        return typeof this === 'function' && this[myFunction_toString_symbol] || $toString.$call(this);
    }

    const set_native = function set_native(func, key, value) {
        Object.defineProperty(func, key, {
            "enumerable": false,
            "configurable": true,
            "writable": true,
            "value": value
        });
    }

    delete Function.prototype['toString'];
    set_native(Function.prototype, "toString", myToString);
    set_native(Function.prototype.toString, myFunction_toString_symbol, "function toString() { [native code] }");

    const safe_Function = function safe_Function(func) {
        set_native(func, myFunction_toString_symbol, "function" + (func.name ? " " + func.name : "") + "() { [native code] }");
    }

    return safe_Function(func)
}

//创建函数
const makeFunction = function makeFunction(name) {
    // 使用 Function 保留函数名
    let func = new Function("v_log", `
        return function ${name}() {
            v_log('函数${name}传参-->', arguments);
        };
    `)(v_log); // 传递 v_log 到动态函数

    safeFunction(func);
    func.prototype = myProxy(func.prototype, `方法${name}.prototype`);

    return func;
}

window = global;


delete global
delete Buffer
// delete process
delete __dirname
delete __filename


Window.prototype = myProxy(Window.prototype, 'window');
Object.setPrototypeOf(window, Window.prototype);


// self = window
// window.top = window


Document = function Document(){}
Document.prototype.createElement = function createElement(ss){
    v_log("document.createlement创建了一个标签", ss)
}
HTMLDocument = function HTMLDocument(){}
Object.setPrototypeOf(HTMLDocument.prototype, Document.prototype)
document = new HTMLDocument()


navigator = {};
screen = {};
history = {};
location = {};
localStorage = {
    getItem: function getItem(ss) {
        v_log("localStorage.getItem传入了参数", ss)
        return this[ss]
    },
    setItem: function setItem(aa, bb) {
        v_log("localStorage.setItem传入了参数", arguments)
        this[aa] = bb
    },
    removeItem: function removeItem(aa) {
        v_log("localStorage.removeItem传入了参数", arguments)
        delete this[aa]
    }
};


document = myProxy(document, 'document')
navigator = myProxy(navigator, 'navigator')
screen = myProxy(screen, 'screen')
history = myProxy(history, 'history')
location = myProxy(location, 'location')
localStorage = myProxy(localStorage, 'localStorage')



//重写 正则表达式test 方法
!function () {
    // 保存原始的 RegExp.prototype.test 方法
    const originalTest = RegExp.prototype.test;

    // 重写 RegExp.prototype.test 方法
    const hookedTest = function (str) {
        v_log('调用了正则test方法，结果为', originalTest.call(this, str), '传入了参数', str);
        return originalTest.call(this, str);
    };

    // 还原 name 属性
    Object.defineProperty(hookedTest, 'name', {
        value: originalTest.name,
        writable: false,
        enumerable: false,
        configurable: true
    });

    // 还原 length 属性
    Object.defineProperty(hookedTest, 'length', {
        value: originalTest.length,
        writable: false,
        enumerable: false,
        configurable: true
    });

    // 还原 toString 方法
    hookedTest.toString = function () {
        return originalTest.toString();
    };

    // 将重写后的函数赋值给 RegExp.prototype.test
    RegExp.prototype.test = hookedTest;
}();


// 重写 match 方法, 查看是否检测了空格等字符串
!function () {
    // 保存原始的 String.prototype.match 方法
    const originalMatch = String.prototype.match;

    // 重写 String.prototype.match 方法
    const hookedMatch = function (regex) {
        v_log('match传入的参数是:', regex);
        // 调用原始的 match 方法并返回结果
        return originalMatch.call(this, regex);
    };

    // 还原 name 属性
    Object.defineProperty(hookedMatch, 'name', {
        value: originalMatch.name,
        writable: false,
        enumerable: false,
        configurable: true
    });

    // 还原 length 属性
    Object.defineProperty(hookedMatch, 'length', {
        value: originalMatch.length,
        writable: false,
        enumerable: false,
        configurable: true
    });

    // 还原 toString 方法
    hookedMatch.toString = function () {
        return originalMatch.toString();
    };

    // 将重写后的函数赋值给 String.prototype.match
    String.prototype.match = hookedMatch;
}();

//重写 toString 方法, 检测所有函数，数组，数字，字符串，符号类型的toString调用
!function () {
    // 保存原始的 Object.prototype.toString 方法
    const originalObjectToString = Object.prototype.toString;
    // 保存原始的 Function.prototype.toString 方法
    const originalFunctionToString = Function.prototype.toString;
    // 保存原始的 String.prototype.toString 方法
    const originalStringToString = String.prototype.toString;
    // 保存原始的 Number.prototype.toString 方法
    const originalNumberToString = Number.prototype.toString;
    // 保存原始的 Array.prototype.toString 方法
    const originalArrayToString = Array.prototype.toString;
    // 保存原始的 Symbol.prototype.toString 方法
    const originalSymbolToString = Symbol.prototype.toString;

    // 定义一个辅助函数来重写 toString 方法
    function overrideToString(target, original, logMessage) {
        const hookedToString = function (...args) {
            logMessage(this, ...args);
            return original.apply(this, args);
        };

        // 还原 name 属性
        Object.defineProperty(hookedToString, 'name', {
            value: original.name,
            configurable: false,
            enumerable: false,
            writable: false
        });

        // 还原 length 属性
        Object.defineProperty(hookedToString, 'length', {
            value: original.length,
            configurable: false,
            enumerable: false,
            writable: false
        });

        // 还原 toString 方法
        hookedToString.toString = function () {
            return original.toString();
        };

        target.toString = hookedToString;
    }

    // 重写 Function.prototype.toString 方法
    overrideToString(Function.prototype, originalFunctionToString, function (func) {
        let functionName;
        if (typeof func === 'function') {
            functionName = func.name;
            if (!functionName) {
                const funcStr = originalFunctionToString.call(func);
                // const firstPart = funcStr.slice(0, 100);
                const firstPart = funcStr;
                functionName = `匿名函数-${firstPart}`;
            }
        } else {
            functionName = '非函数对象';
        }
        v_log(`正在调用 toString 方法的函数名: ${functionName}`);
    });

    // 重写 String.prototype.toString 方法
    overrideToString(String.prototype, originalStringToString, function (str) {
        v_log(`正在调用 toString 方法的字符串: ${originalStringToString.call(str)}`);
    });

    // 重写 Number.prototype.toString 方法
    overrideToString(Number.prototype, originalNumberToString, function (num) {
        v_log(`正在调用 toString 方法的数字: ${originalNumberToString.call(num)}`);
    });

    // 重写 Array.prototype.toString 方法
    overrideToString(Array.prototype, originalArrayToString, function (arr) {
        v_log(`正在调用 toString 方法的数组: [${originalArrayToString.call(arr)}]`);
    });

    // 重写 Object.prototype.toString 方法
    overrideToString(Object.prototype, originalObjectToString, function (obj) {
        v_log(`正在调用 toString 方法的对象:`, obj);
    });

    // 重写 Symbol.prototype.toString 方法
    overrideToString(Symbol.prototype, originalSymbolToString, function (sym) {
        v_log(`正在调用 toString 方法的符号: ${originalSymbolToString.call(sym)}`);
    });

}();

//hook 所有call调用的方法，查看方法名，入参，出参
// !function () {
//     // 保存原始的 Function.prototype.call 方法
//     const originalCall = Function.prototype.call;
//
//     // 定义一个标志，用于避免递归调用
//     let isCallingOriginal = false;
//
//     // 自定义序列化函数，处理循环引用并详细打印
//     function customStringify(value, indent = 0) {
//         const seen = new WeakSet();
//
//         function serialize(val, currentIndent) {
//             if (typeof val ==='symbol') {
//                 return val.toString().replace('Symbol(', '').replace(')', '');
//             }
//             if (typeof val === 'object' && val !== null) {
//                 if (seen.has(val)) {
//                     return '[Circular Reference]';
//                 }
//                 seen.add(val);
//                 if (Array.isArray(val)) {
//                     if (val.length === 0) {
//                         return '[]';
//                     }
//                     const arrayIndent = ' '.repeat(currentIndent + 2);
//                     const items = val.map(item => {
//                         return `${arrayIndent}${serialize(item, currentIndent + 2)}`;
//                     }).join(',\n');
//                     return `[\n${items}\n${' '.repeat(currentIndent)}]`;
//                 }
//                 const keys = Object.keys(val);
//                 if (keys.length === 0) {
//                     return '{}';
//                 }
//                 const objectIndent = ' '.repeat(currentIndent + 2);
//                 const properties = keys.map(key => {
//                     return `${objectIndent}"${key}": ${serialize(val[key], currentIndent + 2)}`;
//                 }).join(',\n');
//                 return `{\n${properties}\n${' '.repeat(currentIndent)}}`;
//             }
//             if (typeof val === 'function') {
//                 const funcName = val.name || 'anonymous';
//                 return `[Function: ${funcName}]`;
//             }
//             if (typeof val === 'number' || typeof val === 'boolean' || val === null) {
//                 return JSON.stringify(val);
//             }
//             if (typeof val ==='string') {
//                 return `"${val}"`;
//             }
//             return JSON.stringify(val);
//         }
//
//         return serialize(value, indent);
//     }
//
//     // 重写 Function.prototype.call 方法
//     const hookedCall = function (thisArg, ...args) {
//         if (isCallingOriginal) {
//             // 正确调用原始 call 方法
//             return originalCall.apply(this, [thisArg, ...args]);
//         }
//         try {
//             isCallingOriginal = true;
//             // 获取当前正在调用的函数名称
//             const functionName = this.name || '匿名函数';
//
//             // 使用原始的 call 方法来执行函数
//             const result = originalCall.apply(this, [thisArg, ...args]);
//
//             // 只记录非内部函数的调用
//             if (!functionName.startsWith('on') &&
//                 !functionName.startsWith('_') &&
//                 functionName !== "addListener" &&
//                 functionName !== "removeListener" &&
//                 functionName !== "emit") {
//                 v_log(`正在运行call方法的函数: ${functionName} 上下文为${customStringify(thisArg, 2)} -> 传参: ${customStringify(args, 2)} -> 返回: ${customStringify(result, 2)}`);
//             }
//             return result;
//         } finally {
//             isCallingOriginal = false;
//         }
//     };
//
//     // 还原 name 属性
//     Object.defineProperty(hookedCall, 'name', {
//         value: originalCall.name,
//         writable: false,
//         enumerable: false,
//         configurable: true
//     });
//
//     // 还原 length 属性
//     Object.defineProperty(hookedCall, 'length', {
//         value: originalCall.length,
//         writable: false,
//         enumerable: false,
//         configurable: true
//     });
//
//     // 还原 toString 方法
//     hookedCall.toString = function () {
//         return originalCall.toString();
//     };
//
//     // 将重写后的函数赋值给 Function.prototype.call
//     Function.prototype.call = hookedCall;
// }();


//hook 所有apply调用的方法，查看方法名，入参，出参
!function () {
    // 保存原始的 Function.prototype.apply 方法
    const originalApply = Function.prototype.apply;

    // 定义一个标志，用于避免递归调用
    let isCallingOriginal = false;

    /**
     * 自定义序列化函数，处理循环引用并详细打印
     * @param {any} value - 要序列化的值
     * @param {number} [indent=0] - 缩进量
     * @returns {string} - 序列化后的字符串
     */
    function customStringify(value, indent = 0) {
        const seen = new WeakSet();

        function serialize(val, currentIndent) {
            if (typeof val ==='symbol') {
                return val.toString().replace('Symbol(', '').replace(')', '');
            }
            if (typeof val === 'object' && val !== null) {
                if (seen.has(val)) {
                    return '[Circular Reference]';
                }
                seen.add(val);
                if (Array.isArray(val)) {
                    if (val.length === 0) {
                        return '[]';
                    }
                    const arrayIndent = ' '.repeat(currentIndent + 2);
                    const items = val.map(item => {
                        return `${arrayIndent}${serialize(item, currentIndent + 2)}`;
                    }).join(',\n');
                    return `[\n${items}\n${' '.repeat(currentIndent)}]`;
                }
                const keys = Object.keys(val);
                if (keys.length === 0) {
                    return '{}';
                }
                const objectIndent = ' '.repeat(currentIndent + 2);
                const properties = keys.map(key => {
                    return `${objectIndent}"${key}": ${serialize(val[key], currentIndent + 2)}`;
                }).join(',\n');
                return `{\n${properties}\n${' '.repeat(currentIndent)}}`;
            }
            if (typeof val === 'function') {
                const funcName = val.name || 'anonymous';
                return `[Function: ${funcName}]`;
            }
            if (typeof val === 'number' || typeof val === 'boolean' || val === null) {
                return JSON.stringify(val);
            }
            if (typeof val ==='string') {
                return `"${val}"`;
            }
            return JSON.stringify(val);
        }
        return serialize(value, indent);
    }

    /**
     * 重写后的 Function.prototype.apply 方法
     * @param {any} thisArg - 函数调用时的 this 值
     * @param {Array} argsArray - 函数调用时的参数数组
     * @returns {any} - 函数调用的结果
     */
    const hookedApply = function (thisArg, argsArray) {
        if (isCallingOriginal) {
            return originalApply.call(this, thisArg, argsArray);
        }
        try {
            isCallingOriginal = true;
            // 获取当前正在调用的函数名称
            const functionName = this.name || '匿名函数';
            // 获取传入的参数
            const parameters = argsArray || [];

            // 使用原始的 apply 方法来执行函数
            const result = originalApply.call(this, thisArg, argsArray);

            if (functionName !== "addListener" && functionName !== "removeListener") {
                v_log(`正在运行apply方法的函数: ${functionName} 上下文为${customStringify(thisArg, 2)}-> 传参: ${customStringify(parameters, 2)} -> 返回: ${customStringify(result, 2)}`);
            }
            return result;
        } finally {
            isCallingOriginal = false;
        }
    };

    // 还原 name 属性
    Object.defineProperty(hookedApply, 'name', {
        value: originalApply.name,
        writable: false,
        enumerable: false,
        configurable: true
    });

    // 还原 length 属性
    Object.defineProperty(hookedApply, 'length', {
        value: originalApply.length,
        writable: false,
        enumerable: false,
        configurable: true
    });

    // 还原 toString 方法
    hookedApply.toString = function () {
        return originalApply.toString();
    };

    // 将重写后的函数赋值给 Function.prototype.apply
    Function.prototype.apply = hookedApply;
}();


//对eval进行hook
!function(){
        // 重写 eval 函数的代码
    const originalEval = window.eval;
    const hookedEval = function (code) {
        try {
            if (typeof code === 'string' && code.includes('debugger')) {
                debugger;
            }
            const startTime = performance.now();
            const result = originalEval(code);
            const endTime = performance.now();
            const executionTime = endTime - startTime;
            v_log(`eval 执行的代码: ${code}   执行结果: ${result}   执行时间: ${executionTime} 毫秒`);
            return result;
        } catch (error) {
            console.error(`eval 执行出错: ${error.message}`);
            v_log(`eval 执行的代码: ${code}`);
            throw error;
        }
    };
    Object.defineProperty(hookedEval, 'name', {
        value: originalEval.name,
        writable: false,
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(hookedEval, 'length', {
        value: originalEval.length,
        writable: false,
        enumerable: false,
        configurable: true
    });
    hookedEval.toString = function () {
        return originalEval.toString();
    };
    window.eval = hookedEval;
}()


//对setTimeOut进行hook
!function () {
    // 保存原始的 setTimeout 函数
    const originalSetTimeout = window.setTimeout;

    // 重写 setTimeout 函数
    const hookedSetTimeout = function (callback, delay, ...args) {
        // 包装回调函数
        const wrappedCallback = function () {
            try {
                // 判断参数是否为 1
                if (args.length === 1 && args[0] === 1) {
                    debugger;
                }
                const startTime = performance.now();
                // 执行原始回调函数
                const result = callback.apply(this, args);
                const endTime = performance.now();
                const executionTime = endTime - startTime;

                // 打印回调函数执行信息
                v_log(`setTimeout 回调函数执行结果:`, result);
                v_log(`setTimeout 回调函数执行时间: ${executionTime} 毫秒`);

                return result;
            } catch (error) {
                // 打印回调函数执行出错信息
                console.error(`setTimeout 回调函数执行出错: ${error.message}`);
                throw error;
            }
        };

        // 调用原始的 setTimeout 函数，传入包装后的回调函数
        return originalSetTimeout(wrappedCallback, delay, ...args);
    };

    // 还原 name 属性
    Object.defineProperty(hookedSetTimeout, 'name', {
        value: originalSetTimeout.name,
        writable: false,
        enumerable: false,
        configurable: true
    });

    // 还原 length 属性
    Object.defineProperty(hookedSetTimeout, 'length', {
        value: originalSetTimeout.length,
        writable: false,
        enumerable: false,
        configurable: true
    });

    // 还原 toString 方法
    hookedSetTimeout.toString = function () {
        return originalSetTimeout.toString();
    };

    // 将重写后的函数赋值给 window.setTimeout
    window.setTimeout = hookedSetTimeout;
}();


//对setInterval进行hook
!function () {
    // 保存原始的 setInterval 函数
    const originalSetInterval = window.setInterval;

    // 重写 setInterval 函数
    const hookedSetInterval = function (callback, delay, ...args) {
        // 包装回调函数
        const wrappedCallback = function () {
            try {
                // 判断参数是否为 1
                if (args.length === 1 && args[0] === 1) {
                    debugger;
                }
                const startTime = performance.now();
                // 执行原始回调函数
                const result = callback.apply(this, args);
                const endTime = performance.now();
                const executionTime = endTime - startTime;

                // 打印回调函数执行信息
                v_log(`setInterval 回调函数执行结果:`, result);
                v_log(`setInterval 回调函数执行时间: ${executionTime} 毫秒`);

                return result;
            } catch (error) {
                // 打印回调函数执行出错信息
                console.error(`setInterval 回调函数执行出错: ${error.message}`);
                throw error;
            }
        };

        // 调用原始的 setInterval 函数，传入包装后的回调函数
        return originalSetInterval(wrappedCallback, delay, ...args);
    };

    // 还原 name 属性
    Object.defineProperty(hookedSetInterval, 'name', {
        value: originalSetInterval.name,
        writable: false,
        enumerable: false,
        configurable: true
    });

    // 还原 length 属性
    Object.defineProperty(hookedSetInterval, 'length', {
        value: originalSetInterval.length,
        writable: false,
        enumerable: false,
        configurable: true
    });

    // 还原 toString 方法
    hookedSetInterval.toString = function () {
        return originalSetInterval.toString();
    };

    // 将重写后的函数赋值给 window.setInterval
    window.setInterval = hookedSetInterval;
}();


v_log("正文代码从此处开始.............\n" + '+'.repeat(200) + '\n'.repeat(20) + '+'.repeat(200));
