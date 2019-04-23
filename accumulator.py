#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 19:16:42 2019

@author: chenna
"""

import numpy as np
import matplotlib.pyplot as plt
n=np.linspace(0,100,100)
x=np.sin(2*np.pi*n)
fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
ax1.stem(n,x)
y=np.zeros(100)
for i in range(0,100,1):
        j=i
        while j>=0:
            y[i]+=x[j]
            j=j-1
ax2.stem(n,y)
plt.show()