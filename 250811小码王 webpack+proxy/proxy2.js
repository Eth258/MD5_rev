let setProxyArr = function (proxyObjArr) {
  for (let i = 0; i < proxyObjArr.length; i++) {
    const handler = `{
    get:function(target,property,receiver){
    console.log("方法:","get","对象","${proxyObjArr[i]}","属性:",
property,"属性类型:",typeof property,"属性值:",target[property],"属性值类型:",typeof target[property]);
return Reflect.get(...arguments)
debugger
    },
    set:function(target,property,value,receiver){
    console.log("方法:","set","对象:","${proxyObjArr[i]}","属性:",
property,"属性类型:",typeof property,"属性值:",value,"属性值类型:",typeof target[property]);
    return Reflect.set(...arguments);
    }
  }`;
    eval(`try{
        ${proxyObjArr[i]};
        ${proxyObjArr[i]} = new Proxy(${proxyObjArr[i]},${handler});
        } catch (e){
         ${proxyObjArr[i]} = {};
         ${proxyObjArr[i]} = new Proxy(${proxyObjArr[i]},${handler});
         }`);
  }
}
function watch(object) {
  const handler = {
    get: function (target, property, receiver) {
      if (property !== 'isNaN' && property !== 'encodeURI' && property !== "Uint8Array" && property !== 'undefined' && property !== 'JSON') {
        console.log("方法:", "get", "对象", target, "属性:",
          property, "属性类型:", typeof property, "属性值:", target[property], "属性值类型:", typeof target[property]);
      }
      return Reflect.get(...arguments)

    },
    set: function (target, property, value, receiver) {
      console.log("方法:", "set", "对象:", target, "属性:",
        property, "属性类型:", typeof property, "属性值:", value, "属性值类型:", typeof target[property]);
      return Reflect.set(...arguments);
    }
  }
  return new Proxy(object, handler)
}
window = global
window.Buffer = Buffer
delete global
delete Buffer

function Element(name){
    this.nodeName=name
    this.childNodes=[]

    this.appendChild=function (node){
        this.childNodes.push(node)
    }

}

function HTMLDocument() {
this.head=new Element("head")
    this.currentScript=null
}

HTMLDocument.prototype.createElement=function (name){
  return new Element(name)
}
document = new HTMLDocument()
window.Document = HTMLDocument

function Navigator() {

}
navigator = new Navigator()
window.Navigator = Navigator

function Screen() {

}
screen = new Screen()
window.Screen = Screen

function History() {

}
history = new History()
window.History = History

function Location() {
 this.origin='https://world.xiaomawang.com'
}
location = new Location()
window.Location = Location
// setProxyArr(['window', 'document', 'location', 'history', 'screen', 'navigator'])
