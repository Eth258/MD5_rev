import websocket
import json
import time

# 目标 WebSocket 地址（替换为实际地址）
WS_URL = "ws://md5hashing.net/sockjs/851/lzsfscsz/websocket"


def main():
    ws = websocket.WebSocket()
    ws.connect(WS_URL)

    # Step 1: 发送 connect 消息
    connect_msg = ["{\"msg\":\"connect\",\"version\":\"1\",\"support\":[\"1\",\"pre2\",\"pre1\"]}"]
    ws.send(json.dumps(connect_msg))
    print("[*] Sent connect")

    # Step 2: 等待 connected
    while True:
        resp = ws.recv()
        print("[Recv]", resp)
        data = json.loads(resp)
        if data.get("msg") == "connected":
            print("[+] Connected with session:", data.get("session"))
            break

    # Step 3: 发送 method 请求
    method_msg = {
        "msg": "method",
        "method": "hash.get",
        "params": ["md5", "62cc0b4ebb0b57b40778179234246c38"],
        "id": "1"
    }
    ws.send(json.dumps(method_msg))
    print("[*] Sent method call")

    # Step 4: 接收方法返回
    while True:
        resp = ws.recv()
        print("[Recv]", resp)

if __name__ == "__main__":
    main()
