#include <stdlib.h>
#include "ranmar.c"

void iniciaranmar(int ij, int kl){
  rmarin_(ij,kl);
}
int randi(float *ran,int max,int min){
  ranmar1_(ran);
  return (int)(*ran*(max-min)+min);
}

int moeda(float *ran){
  return randi(ran,0,2)*2-1;
}

