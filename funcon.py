#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 23:25:49 2019

@author: aravind
"""

import numpy as np
import matplotlib.pyplot as plt
from conv import conv,rev
l1=input("length of first signal:")
l2=input("length of first signal:")
l=l1+l2-1
A=np.zeros(l1)
B=np.zeros(l2)
C=np.zeros(l)
for i in range(0,l1,1):
    A[i]=input("enter an element for signal 1:")
for i in range(0,l2,1):
    B[i]=input("enter an element for signal 2:")
C=conv(A,B)
R=rev(B)
R1=conv(A,R)
ax1=plt.subplot(211)
ax1.stem(C)
ax2=plt.subplot(212)
ax2.stem(R1)
plt.show()