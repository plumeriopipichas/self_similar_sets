# -*- coding: utf-8 -*-
#!/usr/bin/env python

from ejemplos_autosimilares import sierpinski_T_mod

import sys

import scipy as sp

from scipy import linalg 

import matplotlib as mp

from matplotlib import pylab as pl

from collections import deque

import base_as 

from base_as import compacto, contraccion


P = [sp.array([0,3],dtype=float),sp.array([-2,0],dtype=float),sp.array([2,0],dtype=float)]
M = sierpinski_T_mod(P[0],P[1],P[2],0.37,7)	
M.mostrar(0.03,.7)
