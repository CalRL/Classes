#include <stdio.h>
/*
int main ()
{
printf ("Bonjour");
   getchar ();
printf ("Merci d'avoir appuyé sur une touche, Appuie à nouveau sur une touche pour quitter le programme");
   return 0;
}
*/
/*
#include <stdio.h>

int main ()
{
int i;
   int j;
   i=22;
   j=i;
   printf ("i vaut %d\n", i);
   printf ("i+j vaut %d\n", i+j);
getchar ();
   return 0;
}
*/


/*
#include <stdio.h>
int main ()
{
char car;
   char f;
car='E';
   f='e';
   printf("car=%c f=%c\n",car,f);
getchar ();
return 0;
}
*/
/*
int main ()
{
    int i;
    i='U';
    printf("Le caractere %d est %c",i,i);
    getchar();
    return 0;
}
*/
/*
#include <stdio.h>
int main ()
{
    printf("Calculatrice :\n\n");
    printf("Valeur de a :\n");
    int a;
    a=36;
    getchar();
    printf("Valeur de b :\n");
    int b;
    b=54;
    getchar();
    printf("Valeur de a + b :\n%d", a+b);
}
*/
/*
#include <stdio.h>
int main()
{
    int a;
    printf ("Valeur de a :\n");
scanf ("%d", &a);
    getchar();
    printf("Valeur de b:\n");
    int b;
    scanf("%d", &b);
    printf("Valeur de a + b :\n%d", a+b);

}
*/
/*
int main() {
    int a;
    a=0;
    int b;
    b=0;
    int c;
    c=0;
    printf("Saisie de a: ");
    scanf("%d", &a);
    getchar();
    printf("Saisie de b: ");
    scanf("%d", &b);
    c=a/b;
    printf("Valeur de a %% b = %d", c);
    getchar();
    return 0;

}
*/
/*
int main() {
    int i2=0;
    int a=0;
    scanf("%d", &a);
    if(a<i2) {
        printf("Negative");
    } else if(a>i2) {
        printf("Positive");
        } else if(a==i2) {
            printf("Null");
            }
}
*/
/*
int main () {
   double i=1;
   do {
      printf(" i=%d \n",i);
      i=i+100000001;
}
while (i>0); //Test toujours vrai !
   return 0;
}
*/



/*#include <stdio.h>
int calculatrice() {
int a;
int b;
int c;
int d;

printf("saisir un chiffre");
scanf("%d", &a);
printf("que voulez vous faire de ce chiffre \n 1) + \n 2) - \n 3) * \n 4) / ");
scanf("%d", &b);
printf("choisir un deuxieme chiffre !!");
scanf("%d", &c);
if(b == 1){
    d =  add(a,c);
}
if(b == 2){
    d =  sous(a,c);
}
if(b == 3){
    d =  multi(a,c);
}
if(b == 4){
    d =  div(a,c);
}

 printf("yey %d", d);
}
int add(int x, int y){
    int r;
    r = x + y;
    return r;
}
int sous(int x, int y){
    int r;
    r = x - y;
    return r;
}
int multi(int x, int y){
    int r;
    r = x * y;
    return r;
}
int div(int x, int y){
    int r;
    r = x / y;
    return r;
}

*/
/*
int main () {

    int i, j, t, rows, k = 0;
    printf (" Enter a number to define the rows: \n");
    scanf ("%d", &rows);

    for ( i =1; i <= rows; i++)
    {
        for ( j = 1; j <= rows - i; j++)
        {
            printf (" ");
        }
        // use for loop where k is less than equal to (2 * i -1)
        for ( k = 1; k <= ( 2 * i - 1); k++)
        {
            printf ("*"); // print the Star
        }
        printf ("\n");
    }
for (t=1; t<=4; t++) {
        printf("      @@@\n");
    }
    getch();

}
*/
/*
#include <stdio.h>
int main(){

    int chose;
    int r;
    int i;
    int fin;

    printf("tu cherche ?\n 1) tension\n 2) courant \n 3) resistence ");
    scanf("%d", &chose);
    if(chose = 1){
        printf("rentre l intensiter");
        scanf("%d", &i);
        printf("rentre la resistance");
        scanf("%d", &r);
        fin = tension(i,r);
    }
    if(chose = 2){
        printf("rentre la tension");
        scanf("%d", &i);
        printf("rentre la resistance");
        scanf("%d", &r);
        fin = courant(i,r);
    }
    if(chose = 3){
        printf("rentre l intensiter");
        scanf("%d", &i);
        printf("rentre la tension");
        scanf("%d", &r);
        fin = resi(i,r);
    }
    printf(" %d", fin);
}
*/
