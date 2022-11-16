#include<stdio.h>  
int main(){    

int x = 10000;

int z = 3;
for (;z<=x;z++){
    int y = 2;
    for (;y<=z;y++){
    //this for loop checks to see if x is prime

        if (z%y == 0 && z!=y){
            //printf("%d not prime \n",y);
            break;
        }
        if (z==y){
            printf("%d\n",z);
        }

    }
}
}
