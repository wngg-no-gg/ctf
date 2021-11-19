from pwn import *

# test = '\n'.join([
#     'push %d' % u32(b'/sh\0'),
#     'push %d' % u32(b'/bin'),
#     'xor edx, edx',
#     'xor ecx, ecx',
#     'mov ebx, esp',
#     'mov eax, 0xb',
#     'int 0x80',
# ])

# print(test)

print(asm('''
push 6845231
''').hex())