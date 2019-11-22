#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char * defangIPaddr(char * address){
    int len = strlen(address);
    char* ret = (char*)malloc(len + 6 + 1);

    int j = 0;
    for (int i=0; i<len; i++) {
        if (address[i] == '.') {
            ret[j++] = '[';
            ret[j++] = '.';
            ret[j++] = ']';
            continue;
        }
        ret[j++] = address[i];
    }

    ret[j] = '\0';

    return ret;
}
int main()
{
    char s[]="1.1.1.1";
    char *ss;
    ss=defangIPaddr(s);

    for(int i=0;i<strlen(ss);i++)
    {
        printf("%c",ss[i]);
    }
    
    free(ss);
    return 0;
}
