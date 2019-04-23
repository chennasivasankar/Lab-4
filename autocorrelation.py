#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 21:33:05 2019

@author: chenna
"""
import numpy as np
from conv import rev,conv
import matplotlib.pyplot as plt
n=np.arange(0,500)
x=np.sin(2*np.pi*(20.0/400.0)*n)
x1=np.sin(2*np.pi*(30.0/400.0)*n)
N=np.sin(2*np.pi*(50.0/400.0)*n)
N1=np.random.rand(x.shape[0])
x_N=x+N1
x_N1=x+x1+N1
#h=[1.0/3.0,1.0/3.0,1.0/3.0]
y1=conv(x,rev(x))
y2=conv(x_N,rev(x_N))
y3=conv(x+x1,rev(x+x1))
y4=conv(x_N1,rev(x_N1))
a2=plt.subplot(811)
a2.plot(x)
a1=plt.subplot(814)
a1.plot(y1)
a3=plt.subplot(812)
a3.plot(N1)
a4=plt.subplot(813)
a4.plot(x_N)
a5=plt.subplot(815)
a5.plot(y2)
a6=plt.subplot(818)
a6.plot(y4)
a7=plt.subplot(817)
a7.plot(x_N1)
a8=plt.subplot(816)
a8.plot(y3)