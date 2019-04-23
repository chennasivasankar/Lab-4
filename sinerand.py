#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:01:13 2019

@author: chenna
"""

import numpy as np
import random
import matplotlib.pyplot as plt
n=np.linspace(0,100,100)
x=np.sin(2*np.pi*n)
fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
def Rand(10,100,200):
    a=[]
    for j in range(200):
        a.append(random.radiant(0,100))
    return res
ax1.stem(n,x)
ax2.stem(z,a)
plt.show()