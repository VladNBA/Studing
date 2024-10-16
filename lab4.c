#include <stdio.h>

int main() {

    int a = 6;
        for (int i = 0; i <  8; i++){
                printf(" ");
                for ( int n = a; n > a-i; n--){
                        printf(" ");
                }
                for ( int j = 0; j < a-i; j++){
                        printf("$");
                }
                printf("\n");
        }
}
