# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

import scipy as sp

from scipy import linalg 

import matplotlib as mp

from matplotlib import pylab as pl

from collections import deque

class contraccion(object):
	def __init__(self,a,p): 	#a factores de contraccion, p el vector fijo
		self.fdc = a
		self.fijo = p 

	def eval(self,x): 		#evaluar en un vector x 
		return self.fdc*(x-self.fijo)+self.fijo
	
	def evalist(self,x,m):		#evaluar en los primeros m elementos de una lista
		valores=[]
		for k in range(m):
			valores.append(self.eval(x[k]))	
		return valores

class compacto(object):
	def __init__(self,lista_de_puntos):
		self.puntos = lista_de_puntos
	#Tomar un compacto y generar su imagen por lista de contracciones:
	def siguiente(self,contracciones):	
		m = len(self.puntos)		
		for f in contracciones:
			self.puntos = self.puntos + f.evalist(self.puntos,m)
		self.puntos = deque(self.puntos)		
		for i in range(m):
			self.puntos.popleft()		
		#self.puntos = self.puntos[m:]		
		self.puntos = list(self.puntos)		
		return self

N=-1
while (N<1 or N<>int(N)):
	try:
		N=int(raw_input('Dame el numero de contracciones > '))
	except:
		print ('El valor deberia ser un entero positivo') 
		print "\n"

contracciones = []
K = []		# Creando lista vacia de compactos
K.append([])	# Inicializar el K[0] como vacio

# Se crea la lista de contracciones y el K[0] como el conjunto inicial de puntos fijos
for f in range(N):
	a_1 = float(raw_input("Factor de contraccion horizontal > "))
	a_2 = float(raw_input("Factor de contraccion vertical > "))
	print "\n"
	p1=float(raw_input("Primera coordenada del punto fijo > "))
	p2=float(raw_input("Segunda coordenada del punto fijo > "))
	contracciones.append(contraccion(sp.array([a_1,a_2]),sp.array([p1,p2])))	
	K[0].append(sp.array([p1,p2]))	
	print "\n"
	
iter = raw_input("Cuantas iteraciones? ")
iter = int(iter)

K[0] = compacto(K[0])	# Especificamos que K[0] es un "objeto compacto"

for i in range(iter-1):
	K.append([])
	K[i+1] = compacto([])
	K[i+1].puntos = K[i].puntos
	K[i+1] = compacto.siguiente(K[i+1],contracciones)

#print "El conjunto inicial de puntos es %r" % K[0].puntos
#print "La ultima iteracion da los puntos %r" % K[iter-1].puntos

x = [] 
y = []

for punto in K[iter-1].puntos:
	x.append(punto[0])
	y.append(punto[1])

pl.scatter(x,y, s = 0.01, alpha = 0.8)
pl.show()
