# -*- coding: utf-8 -*-
#!/usr/bin/env python

from ejemplos_autosimilares import sierpinski_T

import sys

import scipy as sp

from scipy import linalg 

import matplotlib as mp

from matplotlib import pylab as pl

from collections import deque

import base_as 

from base_as import compacto, contraccion

P = [sp.array([0,1]),sp.array([1,0]),sp.array([-1,0])]
SG = sierpinski_T(P[0],P[1],P[2],10)	
SG.mostrar(0.055,.85)


