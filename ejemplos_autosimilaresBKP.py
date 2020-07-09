import scipy as sp

from scipy import linalg 

import matplotlib as mp

from matplotlib import pylab as pl

from collections import deque

import base_as 

from base_as import compacto, contraccion

from base_as import generar_aproximacion as gen

class sierpinski_app(compacto):
	def __init__(self,p0,p1,p2,veces):
		fijos = [p0,p1,p2]		
		self.puntos = compacto(fijos).puntos
		contracciones = [contraccion(sp.array([0.5,0.5]),p) for p in fijos]	
		self.puntos = gen(self,contracciones,veces).puntos


P = [sp.array([0,0]),sp.array([2,1]),sp.array([2,-1])]
SG = sierpinski_app(P[0],P[1],P[2],8)	

SG.mostrar(0.08,.7)

"""x = [] 
y = []

for punto in SG.puntos:
	x.append(punto[0])
	y.append(punto[1])

pl.scatter(x,y, s = 0.01, alpha = 0.8)
pl.show()
"""
