#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 1000

void imprime(float *lista, int size){
  int i;
  for (i=0;i<size;i++){
    printf("%f\n",lista[i]);
  }
  printf("%i linhas\n",size);
}
int ordena(float *lista, int size){
  int i;
  float temp;
  int troca=1;
  int passos=0;
  while(troca){
    troca=0;
    for(i=0;i<(size-1);i++){
      passos++;
      if (lista[i]>lista[i+1]){
	temp=lista[i];
	lista[i]=lista[i+1];
	lista[i+1]=temp;
	troca=1;
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
      passos++;
      if (lista[i]>lista[i+1]){
	temp=lista[i];
	lista[i]=lista[i+1];
	lista[i+1]=temp;
	newtroca=i;
      }
    }
    troca=newtroca;
  }
  return passos;
}

void main(){
  FILE *in;
  int i;
  float lista[N];
  float lista2[N];
  in=fopen("dados.txt","r");
  for(i=0; (!feof(in));i++){
    fscanf(in,"%f",&lista[i]);
    lista2[i]=lista[i];
  }
  imprime(lista,i);
  printf("passos: %i\n",ordena(lista,i));
  printf("passos: %i\n",ordena2(lista2,i));
}
