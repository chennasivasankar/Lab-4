#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 19:49:46 2019

@author: chenna
"""
import numpy as np
import cmath as c
j=c.sqrt(-1)
def npt_dft(x):
    l=len(x)
    X=[]
    for n in range(0,l):
        a=0
        for k in range(0,l):
            a+=x[k]*np.exp((-j)*2*np.pi*n*k/l)  
        X.append(a)
    return X

