import sys

import scipy as sp

from scipy import linalg 

import matplotlib as mp

from matplotlib import pylab as pl

from collections import deque


class contraccion(object):
	def __init__(self,a,fijo,rot = None, pendiente = None): 	#a un escalar, p el vector fijo
		self.fdc = a
		self.fijo = fijo 
		self.rot = rot
		self.ref = pendiente
	
	def eval(self, x): 		#evaluar en un vector x 
		parcial = self.fdc*(x-self.fijo)+self.fijo			
		if self.rot == None:		
			return self.fdc*(x-self.fijo)+self.fijo
		if (self.ref == None and self.rot != None):
			A = sp.array([[sp.cos(self.rot),-sp.sin(self.rot)],[sp.sin(self.rot),sp.cos(self.rot)]])
			eval_rot = A.dot(parcial.T)+self.fijo 				
			return eval_rot
		if (self.rot != None and self.ref != None):
			A = sp.array([[sp.cos(self.rot),-sp.sin(self.rot)],[sp.sin(self.rot),sp.cos(self.rot)]])
			B = sp.array([[1-(self.ref)^2,2*self.ref],[2*self.ref,-(1-(self.ref)^2)]])
			B = 1/(1+(self.ref)^2)*B
			C = A.dot(B)				 			
			return C.dot(parcial.T)+self.fijo 

	def evalist(self, x, m):		#evaluar en los primeros m elementos de una lista
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
	def genera(self,contracciones,itera):
		K = []	
		K.append(self)
		for i in range(itera-1):
			K.append([])
			K[i+1] = compacto([])
			K[i+1].puntos = K[i].puntos
			K[i+1] = compacto.siguiente(K[i+1],contracciones)
		return K[itera-1]
	def mostrar(self,area,alfa):
		x = [] 
		y = []
		for punto in self.puntos:
			x.append(punto[0])
			y.append(punto[1])

		pl.scatter(x,y, s = area, alpha = alfa)
		pl.show()

#inicial es un compacto, contracciones una lista de contracciones

"""
def generar_aproximacion(inicial,contracciones,itera):
	K = []	
	K.append(inicial)
	for i in range(itera-1):
		K.append([])
		K[i+1] = compacto([])
		K[i+1].puntos = K[i].puntos
		K[i+1] = compacto.siguiente(K[i+1],contracciones)
	return K[itera-1]

"""
