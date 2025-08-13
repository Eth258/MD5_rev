const CryptoJS = require('crypto-js');

function get_x_tif_timestamp(){
     return  Math.ceil((new Date).getTime() / 1e3)
}

function get_x_tif_nonce(){

            var e, t, n, i = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", r = "0123456789";
            return e = o(6, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"),
            t = o(1, i),
            n = o(1, r),
            t + n + e;
            function o(e, t) {
                e = e || 32;
                for (var n = "", i = 0; i < e; i++)
                    n += t.charAt(Math.ceil(1e3 * Math.random()) % t.length);
                return n
            }

}

function get_x_tif_signature(){
    let time=get_x_tif_timestamp()
    let random=get_x_tif_nonce()
    console.log(random)
    let f = time + random + time
    return CryptoJS.SHA256(f).toString()
}
// console.log(get_x_tif_signature())

function t(t) {
    return t < 0 ? NaN : t <= 30 ? 0 | Math.random() * (1 << t) : t <= 53 ? (0 | Math.random() * (1 << 30)) + (0 | Math.random() * (1 << t - 30)) * (1 << 30) : NaN
}
function e(t, e) {
    for (var n = t.toString(16), r = e - n.length, i = "0"; r > 0; r >>>= 1,
    i += i)
        1 & r && (n = i + n);
    return n
}
function get_n(n) {
    var r = "-";
    return n && (r = ""),
    e(t(32), 8) + r + e(t(16), 4) + r + e(16384 | t(12), 4) + r + e(32768 | t(14), 4) + r + e(t(48), 12)
}
// console.log(get_n())

function get_X_Tingyun(){
    var n = get_n(true).substring(0, 16)
    // console.log(n)
    return "c=B|4Nl_NnGbjwY;x="+n
}
// console.log(get_X_Tingyun())

function header_params(){
    return{
        'x-tif-nonce':get_x_tif_nonce(),
        'x-tif-signature':get_x_tif_signature(),
        'x-tif-timestamp':get_x_tif_timestamp(),
        'X-Tingyun':get_X_Tingyun()
    }
}

// console.log(header_params())