#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 09:27:54 2020

@author: randon
"""
import matplotlib.pyplot as plt


def fit(x,y):
    
    m = len(x)
    slop = (m * (x*y).sum() - x.sum()*y.sum()) / (m*(x**2).sum() - (x.sum())**2)
    inter = ((x**2).sum()*y.sum() - x.sum() * (x*y).sum()) / (m * (x**2).sum() - (x.sum())**2)

    return slop, inter

def predict(x, slop, inter):
    return slop * x + inter

def make_regression(x,y):
    slop, inter = fit(x,y)
    line = predict(x, slop, inter)

    plt.grid()
    plt.scatter(x, y)
    plt.plot(x, line, c='r')
    plt.show()

def r2_show(x,y):
    slop, inter = fit(x,y)
    ya = predict(x, slop, inter)
    yb = sum(y)/len(y)
    SST = sum((y- yb)**2)
    SSreg = sum((ya - yb)**2)

    R2 = SSreg/SST
    print("R2 : %s" % R2)
