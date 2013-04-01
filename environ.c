#include <stdio.h>

int main() {
extern **environ;
int i=0;
for(i; environ[i]!=NULL;i++)
    printf("%s\n",environ[i]);
return 0;
        }
