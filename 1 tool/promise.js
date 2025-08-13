const deasync = require("deasync");

function get_data(data) {
    let done = false;
    let result;
    let error;

    // 调用异步函数
    L(data)
        .then(res => {
            result = res;
            done = true;
        })
        .catch(err => {
            error = err;
            done = true;
        });

    // 阻塞等待异步完成
    while (!done) {
        deasync.sleep(100); // 非阻塞 sleep
    }

    if (error) throw error;
    return result;
}