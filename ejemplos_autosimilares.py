# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

import scipy as sp

from scipy import linalg 

import matplotlib as mp

from matplotlib import pylab as pl

from collections import deque

import base_as 

from base_as import compacto, contraccion

class sierpinski_T(compacto):
	def __init__(self, p0, p1, p2, veces):
		fijos = [p0,p1,p2]		
		self.puntos = compacto(fijos).puntos
		contracciones = [contraccion(sp.array([0.5,0.5]),p) for p in fijos]	
		self.puntos = compacto.genera(self,contracciones,veces).puntos
	
class sierpinski_T_mod(compacto):
	def __init__(self, p0, p1, p2, alfa, veces):
		p3 = sp.array([p1[0]/2+p2[0]/2,p1[1]/2+p2[1]/2])		
		p4 = sp.array([p0[0]/2+p2[0]/2,p0[1]/2+p2[1]/2])
		p5 = sp.array([p0[0]/2+p1[0]/2,p0[1]/2+p1[1]/2])
		fijos = [p0,p1,p2,p3,p4,p5]		
		self.puntos = compacto(fijos).puntos
		contracciones = [contraccion(sp.array([alfa,alfa]),fijos[p]) for p in range(3)]
		contracciones2 = [contraccion(sp.array([1-2*alfa,1-2*alfa]),fijos[p+3]) for p in range (3)]
		contracciones = contracciones + contracciones2
		self.puntos = compacto.genera(self,contracciones,veces).puntos


class sierpinski_T_mod2(compacto):
	def __init__(self, x, beta, veces):
		p1 = sp.array([0,sp.sqrt(3)*x],dtype=float)
		p2 = sp.array([-x,0],dtype=float)
		p3 = sp.array([x,0],dtype=float)		
		p4 = (p2+p3)/2		
		p5 = (p1+p3)/2		
		p6 = (p1+p2)/2
		p7 = (p1+p2+p3)/3
		fijos = [p1,p2,p3,p4,p5,p6,p7]		
		self.puntos = compacto(fijos).puntos
		contracciones = [contraccion(sp.array([1-2*beta,1-2*beta]),fijos[p]) for p in range(6)]
		contracciones = contracciones + [contraccion(sp.array([1-3*beta,1-3*beta]),fijos[6])]
		self.puntos = compacto.genera(self,contracciones,veces).puntos



class carpeta(compacto):
	def __init__(self, esquina, v1, v2, veces):
		fijos = [0 for i in range(8)]		
		fijos[0] = esquina
		fijos[1] = fijos[0] + 0.5*sp.array(v1)
		fijos[2] = fijos[1] + 0.5*sp.array(v1)			
		fijos[3] = fijos[2] + 0.5*sp.array(v2)			
		fijos[4] = fijos[3] + 0.5*sp.array(v2)
		fijos[5] = fijos[4] + 0.5*sp.array(-v1)
		fijos[6] = fijos[5] + 0.5*sp.array(-v1)
		fijos[7] = fijos[6] + 0.5*sp.array(-v2)						
		self.puntos = compacto(fijos).puntos
		contracciones = [contraccion(sp.array([0.3333,0.3333]),p) for p in fijos]	
		self.puntos = compacto.genera(self,contracciones,veces).puntos

class carpeta_basica(carpeta):
	def __init__(self, esquina, lado, veces):
		self.puntos = carpeta(esquina,lado*sp.array([1,0]),lado*sp.array([0,1]),veces).puntos
		
class hexagasket(compacto):
	def __init__(self, x, inclinacion, veces):
		i = inclinacion	
		fijos = [x*sp.array([sp.cos(k*sp.pi/3+i),sp.sin(k*sp.pi/3+i)],dtype=float) for k in range(6)]
		self.puntos = compacto(fijos).puntos
		contracciones = [contraccion(sp.array([0.3333,0.3333],dtype=float),p) for p in fijos]	
		self.puntos = compacto.genera(self,contracciones,veces).puntos

class polygasket(compacto):
	def __init__(self, n, veces, x = 1, inclinacion = 1):
		if n % 2 == 1:
			i = inclinacion*(n-4)*sp.pi/(2*n)
		elif n % 2 == 0:
			i = inclinacion*sp.pi/n
		a = (1-sp.cos(2*sp.pi/n))/(1-sp.cos(2*(round(n/4,0)+1)*sp.pi/n)+sp.cos(2*(n-round(n/4,0))*sp.pi/n)-sp.cos(2*sp.pi/n))
		fijos = [x*sp.array([sp.cos(k*2*sp.pi/n+i),sp.sin(k*2*sp.pi/n+i)],dtype=float) for k in range(n)]
		self.puntos = compacto(fijos).puntos
		contracciones = [contraccion(sp.array([a,a],dtype=float),p) for p in fijos]	
		self.puntos = compacto.genera(self,contracciones,veces).puntos


class Hata_basico(compacto):
	def __init__(self, r, alfa,veces):
		self.puntos = compacto([sp.array([0,0],dtype=float),sp.array([1,0],dtype=float)]).puntos
		contracciones = [contraccion(sp.array([r,r]),sp.array([0,0]),alfa,0)]
		contracciones.append(contraccion(sp.array([1-r**2,1-r**2]),sp.array([1,0]),0,0))
		self.puntos = compacto.genera(self,contracciones,veces).puntos



#P = [sp.array([0,3]),sp.array([-2,1]),sp.array([2,-1])]
#SG = sierpinski_T(P[0],P[1],P[2],7)	
#SG.mostrar(0.08,.9)

"""
CS = carpeta(sp.array([2,3]),sp.array([1,1]),sp.array([-0.5,1.5]),5)
CS.mostrar(0.1,.9)
"""

H = Hata_basico(0.2,.15,5)
print H.puntos 

H.mostrar(0.2,0.95)

"""
P = [sp.array([0,3]),sp.array([-2,1]),sp.array([2,-1])]
SG = sierpinski_T(P[0],P[1],P[2],9)	
SG.mostrar(0.08,.9)


M2 = sierpinski_T_mod2(1,0.4,8)	
M2.mostrar(0.01,0.8)


P = polygasket(5,7)
P.mostrar(0.05,0.7)


P = [sp.array([0,3],dtype=float),sp.array([-2,0],dtype=float),sp.array([2,0],dtype=float)]
M = sierpinski_T_mod(P[0],P[1],P[2],0.37,7)	
M.mostrar(0.03,.7)
"""
