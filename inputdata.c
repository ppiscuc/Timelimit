#include <stdio.h>

int main() {
    int i, nc;

    nc = 0;
    i=getchar();
    while(i != EOF) {
        printf("%d ",nc);
        nc++;
        i = getchar();
    }
    printf("Numar caractere: %d\n", nc);
    return 0;
}

