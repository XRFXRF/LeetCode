#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char * removeDuplicates(char * S){
    if(!S){
        return "";
    }
    char* ss=(char*)malloc(strlen(S));
    ss[0]=S[0];
    int j=1;
    for(int i=1;i<strlen(S);i++)
    {
        ss[j]=S[i];
        if(ss[j-1]==ss[j])
            {
                ss[j-1]='\0';
                ss[j]='\0';
                j--;
            }
        else
        {
            j++;
        }
    }
    return ss;
}
int main()
{
    char p[]="abbaca";
    char* a=removeDuplicates(p);
        for(int i=0;i<strlen(a);i++)
    {
        printf("%c",a[i]);
    }
    
    free(a);

    return 0;
}