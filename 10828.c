#include <stdio.h>
#include <string.h>
#define MAX 100001

int stack[MAX];
int top = -1;

int main()
{
    int N;
    scanf("%d", &N);

    for(int i=0; i<N; i++)
    {
        char* input;
        scanf("%s", input);
        if( strcmp(input, "push") == 0 )
        {
            int num;
            scanf("%d", &num);
            stack[++top] = num;
        }
        
        else if( strcmp(input, "pop") == 0 )
        {
            if(top == -1) { printf("%d\n", -1); }
            else { printf("%d\n", stack[top--]); }
        }
        
        else if( strcmp(input, "size") == 0 )
        {
            printf("%d\n", top+1);
        }
        
        else if( strcmp(input, "empty") == 0 )
        {
            if(top == -1) { printf("%d\n", 1); }
            else { printf("%d\n", 0); }
        }

        else if( strcmp(input, "top") == 0 )
        {
            if(top == -1) { printf("-1\n"); }
            else { printf("%d\n", stack[top]); }
        }

        else{}
    }

    return 0;
}
