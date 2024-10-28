#include <stdio.h> 

int main() {
    int a;
    int k;
    int resultat; 
    scanf("%d", &a);
    scanf("%d", &k);
    resultat = (a << k) | ((1 << k) -1);
    printf("%d\n", resultat);
    

}
