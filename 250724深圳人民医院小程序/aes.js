

    exports.kValueA = void 0;
    exports.kValueA = {
        kValue: [1, 0, 9, 8, 5, 4, 7, 4, 1, 7, 8, 2, 2, 7, 9, 7, 4]
    };

    exports.kValueB = void 0;
    exports.kValueB = {
        kValue: [3, 2, 3, 4, 1, 9, 5, 4, 4, 2, 4, 7, 3, 5, 5, 5, 3, 8]
    };

    exports.kValueC = void 0;
    exports.kValueC = {
        kValue: [7, 7, 3, 8, 5, 5, 3, 1, 9, 4, 3, 5, 8, 2, 9, 1, 0]
    };


    exports.kValueD = void 0;
    exports.kValueD = {
        kValue: [6, 6, 6, 4, 6, 8, 2, 2, 1, 1, 1, 4, 5, 2, 8, 0, 4, 4]
    };


    exports.kValueE = void 0;
    exports.kValueE = {
        kValue: [5, 6, 8, 0, 5, 4, 0, 5, 8, 0, 7, 6, 5, 6, 4, 9, 7, 3]
    };


    exports.kValueF = void 0;
    exports.kValueF = {
        kValue: [5, 0, 4, 2, 7, 6, 7, 1, 3, 6, 0, 9, 9, 6, 7, 6, 3, 9]
    };


    exports.kValueG = void 0;
    exports.kValueG = {
        kValue: [9, 7, 5, 9, 5, 1, 7, 1, 6, 5, 1, 0, 2, 3, 7, 9, 2]
    };



    exports.kValueH = void 0;
    exports.kValueH = {
        kValue: [9, 6, 0, 7, 7, 2, 4, 8, 2, 0, 2, 0, 6, 7, 9, 8, 5, 7, 1]
    };



    exports.vValueA = void 0;
    exports.vValueA = {
        vValue: [1, 0, 9, 8, 5, 4, 7, 4, 1, 7, 8, 2, 2, 7, 9, 7, 7, 4]
    };


    exports.vValueB = void 0;
    exports.vValueB = {
        vValue: [3, 2, 3, 4, 1, 9, 5, 4, 4, 2, 4, 7, 3, 5, 5, 5, 4, 2]
    };


    exports.vValueC = void 0;
    exports.vValueC = {
        vValue: [7, 7, 3, 8, 5, 5, 3, 1, 9, 4, 3, 5, 8, 2, 9, 1, 3, 5]
    };


    exports.vValueD = void 0;
    exports.vValueD = {
        vValue: [6, 6, 6, 4, 6, 8, 2, 2, 1, 1, 1, 4, 5, 2, 8, 0, 1]
    };

    exports.vValueE = void 0;
    exports.vValueE = {
        vValue: [5, 6, 8, 0, 5, 4, 0, 5, 8, 0, 7, 6, 5, 6, 4, 9, 9, 9, 9]
    };


    exports.vValueF = void 0;
    exports.vValueF = {
        vValue: [5, 0, 4, 2, 7, 6, 7, 1, 3, 6, 0, 9, 9, 6, 7, 6, 8, 7]
    };


    exports.vValueG = void 0;
    exports.vValueG = {
        vValue: [9, 7, 5, 9, 5, 1, 7, 1, 6, 5, 1, 0, 2, 3, 7, 9, 0]
    };


    exports.vValueH = void 0;
    exports.vValueH = {
        vValue: [9, 6, 0, 7, 7, 2, 4, 8, 2, 0, 2, 0, 6, 7, 9, 8, 1, 1]
    };

    var e = require("./aes.js")
      , u = require("./aes.js")
      , a = require("./aes.js")
      , l = require("./aes.js")
      , V = require("./aes.js")
      , v = require("/aes.js")
      , k = require("./aes.js")
      , r = require("./aes.js")
      , i = require("./aes.js")
      , s = require("./aes.js")
      , t = require("./aes.js")
      , n = require("./aes.js")
      , q = require("./aes.js")
      , j = require("./aes.js")
      , C = require("./aes.js")
      , p = require("./aes.js")
      , c = require("./CryptoJS").CryptoJS



function encrypt(E){
    var d = E
      , o = e.kValueA.kValue[0] + "" + u.kValueB.kValue[1] + a.kValueC.kValue[2] + l.kValueD.kValue[3] + V.kValueE.kValue[4] + v.kValueF.kValue[5] + k.kValueG.kValue[6] + r.kValueH.kValue[7] + e.kValueA.kValue[8] + u.kValueB.kValue[9] + a.kValueC.kValue[10] + l.kValueD.kValue[11] + V.kValueE.kValue[12] + v.kValueF.kValue[13] + k.kValueG.kValue[14] + r.kValueH.kValue[15]
      , A = i.vValueA.vValue[0] + "" + s.vValueB.vValue[1] + t.vValueC.vValue[2] + n.vValueD.vValue[3] + q.vValueE.vValue[4] + j.vValueF.vValue[5] + C.vValueG.vValue[6] + p.vValueH.vValue[7] + i.vValueA.vValue[8] + s.vValueB.vValue[9] + t.vValueC.vValue[10] + n.vValueD.vValue[11] + q.vValueE.vValue[12] + j.vValueF.vValue[13] + C.vValueG.vValue[14] + p.vValueH.vValue[15];
    return c.AES.encrypt(d, c.enc.Latin1.parse(o), {
        iv: c.enc.Latin1.parse(A),
        mode: c.mode.CBC,
        padding: c.pad.Pkcs7
    }).toString()
}

data='123'
console.log(encrypt(data))