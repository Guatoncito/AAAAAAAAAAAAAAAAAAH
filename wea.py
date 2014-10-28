from numpy import *
G=zeros((19,281903))
w=open('web-Stanford.txt')
n=0
c=19
for linea in w:
	lista=linea.strip().split('\t')
	if int(lista[0])>19:
		continue
	G[int(lista[0])-1,int(lista[1])-1]=1
w.close()
        

