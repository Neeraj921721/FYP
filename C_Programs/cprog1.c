#include <stdio.h>

int main(){
    int x = 50 ;
    int y = 100 ;
    if( x<10 && y<10 )
    {
      printf("less-less\n");
    }
    else if( x>10 && y<10 ){
        printf("more-less\n");
    }
    else if( x<10 && y>10 )
    {
        printf("less-more\n");
    }
    else if( x>10 && y>10 )
    {
        printf("more-more\n");
    }
}
