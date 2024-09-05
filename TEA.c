#include <stdio.h>

int main(void) {
    int t;
    scanf("%d",&t);
    while(t--){
    int x,y,z;
    scanf("%d%d%d",&x,&y,&z);
    int jars=(x+y-1)/y;
    int cost=jars*z;
    printf("%d\n",cost);
    }
}
