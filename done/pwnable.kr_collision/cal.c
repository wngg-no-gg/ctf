#include <stdio.h>
#include <string.h>

unsigned long check_password(const char* p){
    int* ip = (int*)p;
    int i;
    int res=0;
    for(i=0; i<5; i++){
        res += ip[i];
        printf("now ip[%d] = 0x%x, res = 0x%x\n", i, ip[i], res);
    }
    return res;
}

int main()
{
    char str[] = {
        0x70, 0x31, 0x72, 0x36, 0x74, 0x31, 0x70, 0x37,
        0x78, 0x39, 0x7a, 0x39, 0x50, 0x3d, 0x3d, 0x3d,
        0x40, 0x30, 0x43, 0x3d, 0x00, 0x00, 0x00, 0x00,
    };
    printf("str = %s\n", str);
    printf("str'len = %ld\n", strlen(str));
    unsigned long ret = check_password(str);
    printf("ret = 0x%lx\n", ret);

    return 0;
}




