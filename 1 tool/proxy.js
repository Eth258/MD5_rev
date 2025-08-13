// proxy.js

function get_enviroment(proxy_array) {
    // 直接使用 global，不要再声明！
    for (let i = 0; i < proxy_array.length; i++) {
        const targetName = proxy_array[i];
        let target = global[targetName];

        // 如果 global 上没有这个属性，创建一个空对象
        if (target == null || typeof target !== 'object' && typeof target !== 'function') {
            target = {};
            global[targetName] = target;
        }

        // 定义 Proxy handler（使用对象字面量，避免 eval）
        const handler = {
            get(obj, prop, receiver) {
                console.log("方法: get  ", "对象:", targetName, "属性:", prop, "属性类型:", typeof prop, "值类型:", typeof obj[prop]);
                return Reflect.get(obj, prop, receiver);
            },
            set(obj, prop, value, receiver) {
                console.log("方法: set  ", "对象:", targetName, "属性:", prop, "属性类型:", typeof prop, "原值类型:", typeof obj[prop]);
                return Reflect.set(obj, prop, value, receiver);
            }
        };

        // 代理 global[targetName]
        global[targetName] = new Proxy(target, handler);
    }
}

// 调用函数
const proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen'];
get_enviroment(proxy_array);