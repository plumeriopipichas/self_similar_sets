# -*- coding: utf-8 -*-
#!/usr/bin/env python

from ejemplos_autosimilares import polygasket

import sys

import scipy as sp

from scipy import linalg 

import matplotlib as mp

from matplotlib import pylab as pl

from collections import deque

import base_as 

from base_as import compacto, contraccion

P = polygasket(5,7)

P.mostrar(0.03,0.7)
