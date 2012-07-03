#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "moeda.c"

float finddx(int min, int max, int numbars){
  return ((float)(max-min))/((float)numbars);
}

int findbar(float dx, int min, int x){
  return (int)(((float)(x-min))/dx);
}

float findx(float dx, int min, int bar){
  return bar*dx+min;
}

float media(int *data, int numbars){
  int i;
  int sum;
  sum=0;
  for (i=0;i<numbars;i++){
    sum+=data[i];
  }
  return (float)sum/numbars;
}

float quad(int *data, int numbars){
  int i;
  float sum;
  sum=0;
  for (i=0;i<numbars;i++){
    sum+=data[i]*data[i];
  }
  return (float)sum/numbars;
}

void makehist(float ran, int N, int M, int numbars){
  int ij=0;
  int kl=0;
  int i,j,sum;
  int data[50000]; 
  int hist[50000];
  float dx,x1,x2;
  float desv,med;
  iniciaranmar(ij,kl);
  //zera dados e histograma
  for (i=0;i<N;i++){
    data[i]=0;
    hist[i]=0;
  }
  //joga as moedas
  dx=finddx(-M,M+1,numbars); //+1 para incluir o max 
  for (i=0;i<N;i++){
    sum=0;
    for (j=0;j<M;j++){
      sum+=(moeda(&ran));
    }
    data[i]=sum;
    //fprintf(stderr,"%d\n",sum); //imprime os dados
    hist[findbar(dx,-M,sum)]+=1;
  }
  //imprime o histograma
  dx=finddx(-M,M,numbars);  //sem o +1 para fazer o grafico
  for (i=0;i<numbars;i++){
    x1=findx(dx,-M,i)/M;
    x2=findx(dx,-M,i+1)/M;
    printf("%f\t%d\n",x1,0);
    printf("%f\t%f\n",x1,(float)hist[i]/N);
    printf("%f\t%f\n",x2,(float)hist[i]/N);
    printf("%f\t%d\n",x2,0);
  }
  //imprime media e desvio padrao em stderr
  fprintf(stderr,"N: %d\n",N);
  fprintf(stderr,"M: %d\n",M);
  med=media(data,numbars);
  desv=sqrt(quad(data,numbars)-(med*med));
  fprintf(stderr,"media: %f\n",med);
  fprintf(stderr,"desvio padrao: %f\n",desv);
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
