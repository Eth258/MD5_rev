

name='admin';
e=name;

passwd='admin';
a=passwd;

f = e + ":" + a + ":quanyingtec";

console.log(f)

e='Data'

function i(t, e) {
        var n = {
            "[object Function]": 1,
            "[object RegExp]": 1,
            "[object Date]": 1,
            "[object Error]": 1,
            "[object CanvasGradient]": 1,
            "[object CanvasPattern]": 1,
            "[object Image]": 1,
            "[object Canvas]": 1
        }
          , i = {
            "[object Int8Array]": 1,
            "[object Uint8Array]": 1,
            "[object Uint8ClampedArray]": 1,
            "[object Int16Array]": 1,
            "[object Uint16Array]": 1,
            "[object Int32Array]": 1,
            "[object Uint32Array]": 1,
            "[object Float32Array]": 1,
            "[object Float64Array]": 1
        }
          , r = Object.prototype.toString
          , o = Array.prototype
          , a = o.forEach
          , s = o.filter
          , l = o.slice
          , u = o.map
          , c = o.reduce
          , h = {};
        function d(t) {
            if (null == t || "object" != typeof t)
                return t;
            var e = t
              , o = r.call(t);
            if ("[object Array]" === o) {
                if (!C(t)) {
                    e = [];
                    for (var a = 0, s = t.length; a < s; a++)
                        e[a] = d(t[a])
                }
            } else if (i[o]) {
                if (!C(t)) {
                    var l = t.constructor;
                    if (t.constructor.from)
                        e = l.from(t);
                    else {
                        e = new l(t.length);
                        for (a = 0,
                        s = t.length; a < s; a++)
                            e[a] = d(t[a])
                    }
                }
            } else if (!n[o] && !C(t) && !w(t))
                for (var u in e = {},
                t)
                    t.hasOwnProperty(u) && (e[u] = d(t[u]));
            return e
        }
        function f(t, e, n) {
            if (!_(e) || !_(t))
                return n ? d(e) : t;
            for (var i in e)
                if (e.hasOwnProperty(i)) {
                    var r = t[i]
                      , o = e[i];
                    !_(o) || !_(r) || b(o) || b(r) || w(o) || w(r) || x(o) || x(r) || C(o) || C(r) ? !n && i in t || (t[i] = d(e[i])) : f(r, o, n)
                }
            return t
        }
        function p(t, e, n) {
            for (var i in e)
                e.hasOwnProperty(i) && (n ? null != e[i] : null == t[i]) && (t[i] = e[i]);
            return t
        }
        var m, g = function() {
            return h.createCanvas()
        };
        function v(t, e, n) {
            if (t && e)
                if (t.forEach && t.forEach === a)
                    t.forEach(e, n);
                else if (t.length === +t.length)
                    for (var i = 0, r = t.length; i < r; i++)
                        e.call(n, t[i], i, t);
                else
                    for (var o in t)
                        t.hasOwnProperty(o) && e.call(n, t[o], o, t)
        }
        function y(t, e) {
            var n = l.call(arguments, 2);
            return function() {
                return t.apply(e, n.concat(l.call(arguments)))
            }
        }
        function b(t) {
            return "[object Array]" === r.call(t)
        }
        function _(t) {
            var e = typeof t;
            return "function" === e || !!t && "object" === e
        }
        function x(t) {
            return !!n[r.call(t)]
        }
        function w(t) {
            return "object" == typeof t && "number" == typeof t.nodeType && "object" == typeof t.ownerDocument
        }
        h.createCanvas = function() {
            return document.createElement("canvas")
        }
        ;
        var S = "__ec_primitive__";
        function C(t) {
            return t[S]
        }
        function k(t) {
            var e = b(t);
            this.data = {};
            var n = this;
            function i(t, i) {
                e ? n.set(t, i) : n.set(i, t)
            }
            t instanceof k ? t.each(i) : t && v(t, i)
        }
        k.prototype = {
            constructor: k,
            get: function(t) {
                return this.data.hasOwnProperty(t) ? this.data[t] : null
            },
            set: function(t, e) {
                return this.data[t] = e
            },
            each: function(t, e) {
                for (var n in void 0 !== e && (t = y(t, e)),
                this.data)
                    this.data.hasOwnProperty(n) && t(this.data[n], n)
            },
            removeKey: function(t) {
                delete this.data[t]
            }
        },
        e.$override = function(t, e) {
            "createCanvas" === t && (m = null),
            h[t] = e
        }
        ,
        e.clone = d,
        e.merge = f,
        e.mergeAll = function(t, e) {
            for (var n = t[0], i = 1, r = t.length; i < r; i++)
                n = f(n, t[i], e);
            return n
        }
        ,
        e.extend = function(t, e) {
            for (var n in e)
                e.hasOwnProperty(n) && (t[n] = e[n]);
            return t
        }
        ,
        e.defaults = p,
        e.createCanvas = g,
        e.getContext = function() {
            return m || (m = g().getContext("2d")),
            m
        }
        ,
        e.indexOf = function(t, e) {
            if (t) {
                if (t.indexOf)
                    return t.indexOf(e);
                for (var n = 0, i = t.length; n < i; n++)
                    if (t[n] === e)
                        return n
            }
            return -1
        }
        ,
        e.inherits = function(t, e) {
            var n = t.prototype;
            function i() {}
            for (var r in i.prototype = e.prototype,
            t.prototype = new i,
            n)
                n.hasOwnProperty(r) && (t.prototype[r] = n[r]);
            t.prototype.constructor = t,
            t.superClass = e
        }
        ,
        e.mixin = function(t, e, n) {
            p(t = "prototype"in t ? t.prototype : t, e = "prototype"in e ? e.prototype : e, n)
        }
        ,
        e.isArrayLike = function(t) {
            if (t)
                return "string" != typeof t && "number" == typeof t.length
        }
        ,
        e.each = v,
        e.map = function(t, e, n) {
            if (t && e) {
                if (t.map && t.map === u)
                    return t.map(e, n);
                for (var i = [], r = 0, o = t.length; r < o; r++)
                    i.push(e.call(n, t[r], r, t));
                return i
            }
        }
        ,
        e.reduce = function(t, e, n, i) {
            if (t && e) {
                if (t.reduce && t.reduce === c)
                    return t.reduce(e, n, i);
                for (var r = 0, o = t.length; r < o; r++)
                    n = e.call(i, n, t[r], r, t);
                return n
            }
        }
        ,
        e.filter = function(t, e, n) {
            if (t && e) {
                if (t.filter && t.filter === s)
                    return t.filter(e, n);
                for (var i = [], r = 0, o = t.length; r < o; r++)
                    e.call(n, t[r], r, t) && i.push(t[r]);
                return i
            }
        }
        ,
        e.find = function(t, e, n) {
            if (t && e)
                for (var i = 0, r = t.length; i < r; i++)
                    if (e.call(n, t[i], i, t))
                        return t[i]
        }
        ,
        e.bind = y,
        e.curry = function(t) {
            var e = l.call(arguments, 1);
            return function() {
                return t.apply(this, e.concat(l.call(arguments)))
            }
        }
        ,
        e.isArray = b,
        e.isFunction = function(t) {
            return "function" == typeof t
        }
        ,
        e.isString = function(t) {
            return "[object String]" === r.call(t)
        }
        ,
        e.isObject = _,
        e.isBuiltInObject = x,
        e.isTypedArray = function(t) {
            return !!i[r.call(t)]
        }
        ,
        e.isDom = w,
        e.eqNaN = function(t) {
            return t != t
        }
        ,
        e.retrieve = function(t) {
            for (var e = 0, n = arguments.length; e < n; e++)
                if (null != arguments[e])
                    return arguments[e]
        }
        ,
        e.retrieve2 = function(t, e) {
            return null != t ? t : e
        }
        ,
        e.retrieve3 = function(t, e, n) {
            return null != t ? t : null != e ? e : n
        }
        ,
        e.slice = function() {
            return Function.call.apply(l, arguments)
        }
        ,
        e.normalizeCssArray = function(t) {
            if ("number" == typeof t)
                return [t, t, t, t];
            var e = t.length;
            return 2 === e ? [t[0], t[1], t[0], t[1]] : 3 === e ? [t[0], t[1], t[2], t[1]] : t
        }
        ,
        e.assert = function(t, e) {
            if (!t)
                throw new Error(e)
        }
        ,
        e.trim = function(t) {
            return null == t ? null : "function" == typeof t.trim ? t.trim() : t.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g, "")
        }
        ,
        e.setAsPrimitive = function(t) {
            t[S] = !0
        }
        ,
        e.isPrimitive = C,
        e.createHashMap = function(t) {
            return new k(t)
        }
        ,
        e.concatArray = function(t, e) {
            for (var n = new t.constructor(t.length + e.length), i = 0; i < t.length; i++)
                n[i] = t[i];
            var r = t.length;
            for (i = 0; i < e.length; i++)
                n[i + r] = e[i];
            return n
        }
        ,
        e.noop = function() {}
    }
function encData(t, e) {
    if (function(t, e) {
        if (!i.isBuffer(t) && "string" != typeof t)
            throw new TypeError(e + " must be a string or a buffer")
    }(t, "Data"),
    this._finalized)
        throw new Error("Digest already called");
    i.isBuffer(t) || (t = i.from(t, e));
    for (var n = this._block, r = 0; this._blockOffset + t.length - r >= this._blockSize; ) {
        for (var o = this._blockOffset; o < this._blockSize; )
            n[o++] = t[r++];
        this._update(),
        this._blockOffset = 0
    }
    for (; r < t.length; )
        n[this._blockOffset++] = t[r++];
    for (var a = 0, s = 8 * t.length; s > 0; ++a)
        this._length[a] += s,
        (s = this._length[a] / 4294967296 | 0) > 0 && (this._length[a] -= 4294967296 * s);
    return this
}

encData(f,e)