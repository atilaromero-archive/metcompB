#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "ranmar.c"

int randi(float *ran,int max,int min){
  ranmar1_(ran);
  return (int)(*ran*(max-min)+min);
}

int moeda(float *ran){
  return randi(ran,0,2)*2-1;
}

int findbar(int min, int max, int numbars,int x){
  float dx;
  float pos;
  dx=((float)(max-min))/(float)numbars;
  pos=((x-min)/dx);
  return (int)pos;
}

void makehist(float ran, int N, int M, int numbars){
  int ij=0;
  int kl=0;
  int i,j,sum,jog;
  int data[10000]; 
  int hist[10000]; 
  rmarin_(ij,kl);
  //zera dados e histograma
  for (i=0;i<N;i++){
    data[i]=0;
    hist[i]=0;
  }
  //joga as moedas
  for (i=0;i<N;i++){
    sum=0;
    for (j=0;j<M;j++){
      sum+=(moeda(&ran));
    }
    data[i]=sum;
    hist[findbar(-M,M,numbars,sum)]+=1;
  }
  for (i=0;i<N;i++){
    printf("%d\n",hist[i]);
  }
}

void main(int argc, char* argv[]){
  if (argc!=5){
    printf("args: ran N M numbars\n");
    return;
  }
  float ran=atof(argv[1]);
  int N=atoi(argv[2]);
  int M=atoi(argv[3]);
  int numbars=atoi(argv[4]);
  makehist(ran,N,M,numbars);
}
