function dec_data(base64Str) {
    const binaryStr = atob(base64Str); // base64解码成binary string
    const len = binaryStr.length;
    const bytes = new Uint8Array(len);
    for (let i = 0; i < len; i++) {
        bytes[i] = binaryStr.charCodeAt(i);
    }
    const arrayBuffer = bytes.buffer;  // 转为 ArrayBuffer
    return N(arrayBuffer);             // 调用 N 进行解密
}