// encrypt.js

// === 1. 定义所有 kValue 和 vValue 模块 ===
const kValueA = {
    kValue: [1, 0, 9, 8, 5, 4, 7, 4, 1, 7, 8, 2, 2, 7, 9, 7, 4]
};

const kValueB = {
    kValue: [3, 2, 3, 4, 1, 9, 5, 4, 4, 2, 4, 7, 3, 5, 5, 5, 3, 8]
};

const kValueC = {
    kValue: [7, 7, 3, 8, 5, 5, 3, 1, 9, 4, 3, 5, 8, 2, 9, 1, 0]
};

const kValueD = {
    kValue: [6, 6, 6, 4, 6, 8, 2, 2, 1, 1, 1, 4, 5, 2, 8, 0, 4, 4]
};

const kValueE = {
    kValue: [5, 6, 8, 0, 5, 4, 0, 5, 8, 0, 7, 6, 5, 6, 4, 9, 7, 3]
};

const kValueF = {
    kValue: [5, 0, 4, 2, 7, 6, 7, 1, 3, 6, 0, 9, 9, 6, 7, 6, 3, 9]
};

const kValueG = {
    kValue: [9, 7, 5, 9, 5, 1, 7, 1, 6, 5, 1, 0, 2, 3, 7, 9, 2]
};

const kValueH = {
    kValue: [9, 6, 0, 7, 7, 2, 4, 8, 2, 0, 2, 0, 6, 7, 9, 8, 5, 7, 1]
};

const vValueA = {
    vValue: [1, 0, 9, 8, 5, 4, 7, 4, 1, 7, 8, 2, 2, 7, 9, 7, 7, 4]
};

const vValueB = {
    vValue: [3, 2, 3, 4, 1, 9, 5, 4, 4, 2, 4, 7, 3, 5, 5, 5, 4, 2]
};

const vValueC = {
    vValue: [7, 7, 3, 8, 5, 5, 3, 1, 9, 4, 3, 5, 8, 2, 9, 1, 3, 5]
};

const vValueD = {
    vValue: [6, 6, 6, 4, 6, 8, 2, 2, 1, 1, 1, 4, 5, 2, 8, 0, 1]
};

const vValueE = {
    vValue: [5, 6, 8, 0, 5, 4, 0, 5, 8, 0, 7, 6, 5, 6, 4, 9, 9, 9, 9]
};

const vValueF = {
    vValue: [5, 0, 4, 2, 7, 6, 7, 1, 3, 6, 0, 9, 9, 6, 7, 6, 8, 7]
};

const vValueG = {
    vValue: [9, 7, 5, 9, 5, 1, 7, 1, 6, 5, 1, 0, 2, 3, 7, 9, 0]
};

const vValueH = {
    vValue: [9, 6, 0, 7, 7, 2, 4, 8, 2, 0, 2, 0, 6, 7, 9, 8, 1, 1]
};

// === 2. 模拟 require 的行为（把变量赋值）===
const e = { kValueA }; // e.kValueA.kValue[0]
const u = { kValueB }; // u.kValueB.kValue[1]
const a = { kValueC }; // a.kValueC.kValue[2]
const l = { kValueD }; // l.kValueD.kValue[3]
const V = { kValueE }; // V.kValueE.kValue[4]
const v = { kValueF }; // v.kValueF.kValue[5]
const k = { kValueG }; // k.kValueG.kValue[6]
const r = { kValueH }; // r.kValueH.kValue[7]

const i = { vValueA }; // i.vValueA.vValue[0]
const s = { vValueB }; // s.vValueB.vValue[1]
const t = { vValueC }; // t.vValueC.vValue[2]
const n = { vValueD }; // n.vValueD.vValue[3]
const q = { vValueE }; // q.vValueE.vValue[4]
const j = { vValueF }; // j.vValueF.vValue[5]
const C = { vValueG }; // C.vValueG.vValue[6]
const p = { vValueH }; // p.vValueH.vValue[7]

// === 3. 引入 CryptoJS ===
const CryptoJS = require('crypto-js');

// === 4. 加密函数 ===
function encrypt(E) {
    // 拼接 key (16 个数字转字符串)
    var o =
        e.kValueA.kValue[0] +
        "" + u.kValueB.kValue[1] +
        a.kValueC.kValue[2] +
        l.kValueD.kValue[3] +
        V.kValueE.kValue[4] +
        v.kValueF.kValue[5] +
        k.kValueG.kValue[6] +
        r.kValueH.kValue[7] +
        e.kValueA.kValue[8] +
        "" + u.kValueB.kValue[9] +
        a.kValueC.kValue[10] +
        l.kValueD.kValue[11] +
        V.kValueE.kValue[12] +
        v.kValueF.kValue[13] +
        k.kValueG.kValue[14] +
        r.kValueH.kValue[15];

    // 拼接 iv (16 个数字转字符串)
    var A =
        i.vValueA.vValue[0] +
        "" + s.vValueB.vValue[1] +
        t.vValueC.vValue[2] +
        n.vValueD.vValue[3] +
        q.vValueE.vValue[4] +
        j.vValueF.vValue[5] +
        C.vValueG.vValue[6] +
        p.vValueH.vValue[7] +
        i.vValueA.vValue[8] +
        "" + s.vValueB.vValue[9] +
        t.vValueC.vValue[10] +
        n.vValueD.vValue[11] +
        q.vValueE.vValue[12] +
        j.vValueF.vValue[13] +
        C.vValueG.vValue[14] +
        p.vValueH.vValue[15];

    console.log("KEY:");
    console.log(o);
    console.log("IV:");
    console.log(A);
    // 使用 CryptoJS 进行 AES-CBC 加密
    const ciphertext = CryptoJS.AES.encrypt(E, CryptoJS.enc.Latin1.parse(o), {
        iv: CryptoJS.enc.Latin1.parse(A),
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });

    return ciphertext.toString(); // Base64 输出
}

// === 5. 测试 ===
const data = {
    "openidCode": "0e1R5z0w3xTqm53YOH1w3e6F7Q2R5z09",
    "phoneCode": "9b0e75d50c2af9c3beece2bd53f5dbfcc8417055594a2ace100a5579785223c2"
};
const data2=JSON.stringify(data)
console.log('明文:', data2);

console.log('密文 (Base64):', encrypt(data2));