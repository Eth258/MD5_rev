def hex_to_ascii(hex_str):
    """
    将十六进制字符串转换为 ASCII 字符串
    :param hex_str: 十六进制字符串（如 '48656C6C6F'）
    :return: 对应的 ASCII 字符串
    """
    try:
        # 确保输入的 hex 字符串长度是偶数
        if len(hex_str) % 2 != 0:
            raise ValueError("Hex string length must be even.")

        # 将 hex 每两个字符转换为一个字节，再转为 ASCII 字符
        ascii_str = bytes.fromhex(hex_str).decode('ascii')
        return ascii_str
    except ValueError as e:
        return f"[错误] 转换失败: {e}"
    except UnicodeDecodeError:
        return "[错误] 包含非 ASCII 字符（无法解码为纯 ASCII）"

if __name__ == "__main__":
    # 示例输入
    hex_input ="0a0570617065721206e59cb0e79083"
    result = hex_to_ascii(hex_input)
    print("转换结果:", result)