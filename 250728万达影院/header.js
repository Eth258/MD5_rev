


function setMxHead(e, t, n) {
    t.default = {
        clientKey: "B3AA12B0145E1982F282BEDD8A3305B89A9811280C0B8CC3A6A60D81022E4903",
        saleSubjectCode: "Wanda",
        cCode: "1_3",
        mxAPIVer: "1.0.0",
        appId: "3",
        httpsImg: "https://picagent-prd-mx.wandafilm.com/picture/cut_picture?uri=",
        miscBaseUrl: "https://misc-api-prd-mx.wandafilm.com",
        cinemaBaseUrl: "https://cinema-api-prd-mx.wandafilm.com",
        userBaseUrl: "https://user-api-prd-mx.wandafilm.com",
        ticketBaseUrl: "https://ticket-api-prd-mx.wandafilm.com",
        paymentBaseUrl: "https://payment-api-prd-mx.wandafilm.com",
        activityBaseUrl: "https://mkt-activity-api-prd-mx.wandafilm.com",
        cmsActivityBaseUrl: "https://cms-activity-api-prd-mx.wandafilm.com",
        cardBaseUrl: "https://card-api-prd-mx.wandafilm.com",
        couponBaseUrl: "https://coupon-api-prd-mx.wandafilm.com",
        snackBaseUrl: "https://snack-api-prd-mx.wandafilm.com",
        cdspBaseUrl: "https://cdsp-api-prd-mx.wandafilm.com",
        commonURI: "https://misc-api-prd-mx.wandafilm.com",
        mallUrl: "" + window.location.origin,
        gatewayUrl: "https://front-gateway-c.wandafilm.com"
    }
    var i = {
        ver: "7.0.0",
        sCode: this.saleSubjectCode,
        _mi_: e,
        width: 1280,
        json: !0,
        cCode: this.cCode,
        check: n,
        ts: t,
        heigth: 720,
        appId: this.appId
    };
    return JSON.stringify(i)
}

e=''
t= (new Date).getTime()
n=''