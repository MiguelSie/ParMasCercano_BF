# -*- coding: utf-8 -*-
"""Closest Pair BF

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IUOhdPtHJeCVZdSJudp8LhTAd3V78bUJ
"""

import numpy as np
import sys
from math import ceil
from math import log10
import random
import time
import matplotlib.pyplot as plt

def BF(quad):
  dmin = sys.maxsize
  c = 0
  for i in range(len(quad)-1):
    for j in range(i+1, len(quad)):
        d = (quad[i][0] - quad[j][0])**2 + (quad[i][1] - quad[j][1])**2
        c+=1
        if (d<dmin):
          pos1 = quad[i]
          pos2 = quad[j]
          dmin = d
  dmin = np.sqrt(dmin)
  return(pos1, pos2, dmin, c)

timelapse = []
nOperations = []

for i in range(10, 400):
  Ps = []
  for j in range(i):
    Ps.append((random.randint(1, 100), random.randint(1, 100)))

  c = 0
  cOp = 0
  for ii in range(100):
    start = time.time()
    Px = sorted( Ps, key = lambda t: (t[0], t[1]) )
    Py = sorted( Ps, key = lambda t: (t[1], t[0]) )
    #Dado que las funciones construidas por Python utilizan el Timsort, se suma el # de operaciones promedio de este algoritmo
    cOp += (len(Px)*log10(len(Px))) + (len(Py)*log10(len(Py)))

    Lx = Px[ 0 : ceil(len(Ps) / 2) ]
    Rx = Px[ ceil(len(Ps) / 2) : len(Ps) ]

    Ly = sorted(Lx, key = lambda t: (t[1], t[0]))
    Ry = sorted(Rx, key = lambda t: (t[1], t[0]))
    cOp += (len(Ly)*log10(len(Ly))) + (len(Ry)*log10(len(Ry)))

    Lyup = Ly[ 0 : ceil(len(Ly) / 2) ]
    Lydown = Ly[ ceil(len(Ly) / 2) : len(Ly) ]

    Ryup = Ry[ 0 : ceil(len(Ry) / 2) ]
    Rydown = Ry[ ceil(len(Ry) / 2) : len(Ry) ]

    posLyu1, posLyu2, Dlyup, c1 = BF(Lyup)
    posLyd1, posLyd2, Dlydown, c2 = BF(Lydown)
    posRyu1, posRyu2, Dryup, c3 = BF(Ryup)
    posRyd1, posRyd2, Drydown, c4 = BF(Rydown)

    cOp+= c1+c2+c3+c4

    Phalfx = Px[ ceil(len(Px)/4) : ceil(len(Px)*3/4) ]
    Phalfy = Py[ ceil(len(Py)/4) : ceil(len(Py)*3/4) ]
    posPhx1, posPhx2, Dphalfx, c5 = BF(Phalfx)
    posPhy1, posPhy2, Dphalfy, c6 = BF(Phalfy)
    cOp+=c5+c6

    cOp += 6 + (6*log10(6))
    dminfin = min(Dlyup, Dlydown, Dryup, Drydown, Dphalfx, Dphalfy)
    if (dminfin == Dphalfx):
      posmin1 = posPhx1
      posmin2 = posPhx2
    elif (dminfin == Dlyup):
      posmin1 = posLyu1
      posmin2 = posLyu2
    elif (dminfin == Dlydown):
      posmin1 = posLyd1
      posmin2 = posLyd2
    elif (dminfin == Dryup):
      posmin1 = posRyu1
      posmin2 = posRyu2
    elif (dminfin == Drydown):
      posmin1 = posRyd1
      posmin2 = posRyd2
    elif (dminfin == Dphalfy):
      posmin1 = posPhy1
      posmin2 = posPhy2

    end = time.time()
    c += end-start
  timelapse.append(c/100)
  nOperations.append(cOp/100)
print(timelapse)
print(nOperations)

avrgTime = 0
avrgOps = 0
for i in range(len(timelapse)):
  avrgTime+= timelapse[i] 
  avrgOps+= nOperations[i]
avrgTime = avrgTime/len(timelapse)
avrgOps = avrgOps/len(nOperations)

print(avrgTime, avrgOps)

n = [i for i in range (10, 400)]
plt.scatter(n, timelapse)
plt.title("Número de elementos vs tiempo")
plt.xlabel("Elementos")
plt.ylabel("Tiempo")
plt.xlim([0, 400])
plt.ylim([0, 0.12])
plt.show()