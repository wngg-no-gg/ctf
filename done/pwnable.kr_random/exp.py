from pwn import *

session = ssh("random", "pwnable.kr", 2222, "guest")

io = session.process("random")
io.sendline("-1255736440")

io.interactive()