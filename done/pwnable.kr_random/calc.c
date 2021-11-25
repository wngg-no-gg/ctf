#include <stdlib.h>
#include <stdio.h>

int main()
{
    unsigned int random;
    random = rand();
    unsigned int key = random ^ 0xdeadbeef;
    printf("%d\n", key);
    return 0;
}