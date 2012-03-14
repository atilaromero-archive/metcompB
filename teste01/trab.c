#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void imprime(float *lista, int size){
  int i;
  for (i=0;i<size;i++){
    printf("%f\n",lista[i]);
  }
  printf("\n");
}
int ordena(float *lista, int size){
  int i;
  float temp;
  int troca=1;
  int passos=0;
  while(troca){
    troca=0;
    for(i=0;i<(size-1);i++){
      if (lista[i]>lista[i+1]){
	temp=lista[i];
	lista[i]=lista[i+1];
	lista[i+1]=temp;
	troca=1;
	passos++;
      }
    }
  }
  return passos;
}

int ordena2(float *lista, int size){
  int i;
  float temp;
  int troca=size-1;
  int newtroca;
  int passos=0;
  while(troca){
    for(i=0;i<troca;i++){
      if (lista[i]>lista[i+1]){
	temp=lista[i];
	lista[i]=lista[i+1];
	lista[i+1]=temp;
	newtroca=i;
	passos++;
      }
    }
    troca=newtroca;
  }
  return passos;
}

void main(){
  float a[5];
  a[0]=410;
  a[1]=20;
  a[2]=510;
  a[3]=310;
  a[4]=10;
  int size=5;
  printf("passos: %i\n",ordena2(a,size));
  imprime(a,size);
}
