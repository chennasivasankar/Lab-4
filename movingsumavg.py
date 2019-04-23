#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:18:20 2019

@author: chenna
"""

import numpy as np
import matplotlib.pyplot as plt
n=np.linspace(0,200,200)
x=5*np.sin(2*np.pi*n)
fig=plt.figure()
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)
no=np.sin(2*np.pi*6000*n)
x1=x+no
p=input("Order of the system")
p=float(p)
y=np.zeros(200)
for i in range(0,200):
        j=i
        c=0
        while (j>=0 & c<=p-1):
            y[i]+=x1[j]
            j=j-1
            c+=1
        y[i]=y[i]/(p)   
        
ax1.plot(n,x)       
ax2.plot(n,y)
ax3.plot(n,y)