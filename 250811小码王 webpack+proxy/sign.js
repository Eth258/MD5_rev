require('./proxy2.js')
require('./load.js')
require('./mod1.js')
require('./mod2.js')
require('./mod3.js')
require('./mod4.js')
require('./mod5.js')
require('./mod6.js')

s = window.loader("jeHg")
c = window.loader("HaE+")
i = window.loader("o0o1"), r = window.loader.n(i)
g = s.getSign
u = s.getSha512KeyString

R = window.loader("PJO1")
O = window.loader.n(R)
l = function() {
    var e = Object(c.a)(r.a.mark((function e(t) {
        var A, n, o;
        return r.a.wrap((function(e) {
            for (; ; )
                switch (e.prev = e.next) {
                case 0:
                    return e.next = 2,
                    u();
                case 2:
                    return A = e.sent,
                    n = O.a.hmac(A),
                    o = n.finalize(t),
                    e.abrupt("return", o.toString("hex"));
                case 6:
                case "end":
                    return e.stop()
                }
        }
        ), e)
    }
    )));
    return function(t) {
        return e.apply(this, arguments)
    }
}()

// I=g("" + a, JSON.stringify(i));

//"" + a=  '1754917693'
timestamp='1754992337'
//JSON.stringify(i)='{"adBizId":null,"adType":0,"content":"可以","targetId":"p4db666J","targetType":1,"timestamp":1754917693,"type":1,"uuid":"6f7dea6e75a74615"}'
params='{"adBizId":null,"adType":0,"content":"可以","targetId":"p4db666J","targetType":1,"timestamp":1754992337,"type":1,"uuid":"4d78b3d874c84b92"}'

g(timestamp,params).then(res=>{
    console.log(res)
    l(res.signString).then(
        sign=>{
            console.log(sign)
        }
    )
})

// m = I.signString;
// sign=l(m);