#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 19:14:33 2019

@author: chenna
"""
import numpy as np
x=[1,2,3,4,0,0,0]
h=[1,2,3,4,0,0,0]
y=[0,0,0,0,0,0,0]
for n in range(0,7,1):
    sum=0
    for k in range(0,7,1):
        sum=sum+(x[k]*h[n-k])
    y[n]=sum
print y