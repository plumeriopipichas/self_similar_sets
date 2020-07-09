# -*- coding: utf-8 -*-
#!/usr/bin/env python

from ejemplos_autosimilares import carpeta

import sys

import scipy as sp

from scipy import linalg 

import matplotlib as mp

from matplotlib import pylab as pl

from collections import deque

import base_as 

from base_as import compacto, contraccion


CS = carpeta(sp.array([0,0]),sp.array([1,0]),sp.array([0,1]),7)
CS.mostrar(0.1,.9)



