

const CryptoJS=require('crypto-js')

const q=CryptoJS

function K(a, d="XwKsGlMcdPMEhR1B") {
    const l = q.enc.Utf8.parse(d)
      , o = q.enc.Utf8.parse(a);
    return q.AES.encrypt(o, l, {
        mode: q.mode.ECB,
        padding: q.pad.Pkcs7
    }).toString()
}

function get_aes_sign(i,key){
    pointJson=K(JSON.stringify({x: i,y: 5}), key)
    return pointJson
}


