#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:51:05 2019

@author: aravind
"""
#dtft
import numpy as np
import matplotlib.pyplot as plt
import cmath as c
fig=plt.figure()      #creating subplots
plt.subplots_adjust(left=0.125,right=0.9,bottom=0.1,top=0.9,wspace=0.5,hspace=0.8)#adjusting size of the subplots
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)
j=c.sqrt(-1)
n=np.linspace(0,10,50)
w=np.linspace(-np.pi,np.pi,1000)
x=np.sin(2*np.pi*(20.0/100.0)*n)
X=[]
A=[]
p=[]
for k in range(0,1000,1):
    W=w[k]
    a=0
    for i in range(0,len(x),1):
        a+=x[i]*np.exp(-j*W*i)
    X.append(a)
    A.append(np.abs(a))
    p.append(np.angle(a))
ax1.plot(w,X)
ax2.plot(w,A)
ax3.plot(w,p)
plt.show()