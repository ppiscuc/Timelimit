#include <stdio.h>
#include <stdlib.h>

int main() {
    char buf[256];
    sprintf(buf,"/bin/cat /proc/cpuinfo");
    system(buf);
    return 0;
}
