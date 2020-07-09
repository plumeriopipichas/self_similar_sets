# -*- coding: utf-8 -*-
#!/usr/bin/env python

from ejemplos_autosimilares import sierpinski_T_mod2

import sys

import scipy as sp

from scipy import linalg 

import matplotlib as mp

from matplotlib import pylab as pl

from collections import deque

import base_as 

from base_as import compacto, contraccion

M2 = sierpinski_T_mod2(1,0.4,7)	
M2.mostrar(0.01,0.8)

