#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "ranmar.c"

long double randi(int *seed){
  int a=1029;
  int b=221591;
  int c=1048576;
  *seed=(*seed*a+b)%c;
  return ((long double)*seed)/((long double)c);
}

void main(){
  int seed=0;
  printf("%Lf\n",randi(&seed));
  printf("%Lf\n",randi(&seed));
  printf("%Lf\n",randi(&seed));
  printf("%Lf\n",randi(&seed));
  int ij=0;
  int kl=0;
  float ran=0;
  rmarin_(ij,kl);
  printf("%f\n",ran);
  ranmar1_(&ran);
  printf("%f\n",ran);
  ranmar1_(&ran);
  printf("%f\n",ran);
}
