// script.js
function L(data) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(`Processed: ${data}`);
        }, 1000);
    });
}

async function get_data(data) {
    const result = await L(data);
    console.log(result); // 输出结果
    process.exit(0);     // 退出进程
}

// 从命令行接收参数
let a = process.argv[2] || "Hello from Python";
get_data(a);