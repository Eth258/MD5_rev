
//放到控制台运行
window.arrayBufferToHex=function (buffer){
  const view = new Uint8Array(buffer);
  let hex = '';
  for (let i = 0; i < view.length; i++) {
    const byte = view[i];
    hex += byte.toString(16).padStart(2, '0'); // 补零，例如 0x5 -> '05'
  }
  return hex;
}

// 创建一个测试用的 ArrayBuffer
const array = new Uint8Array([0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x57, 0x6f, 0x72, 0x6c, 0x64]); // "Hello World"
const buffer = array.buffer;

const hex = arrayBufferToHex(buffer);
console.log(hex); // 输出: 48656c6c6f20576f726c64
