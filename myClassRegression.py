#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 12:09:22 2020

@author: randon
"""

import matplotlib.pyplot as plt

class LinearRegression:

    def __init__(self,x,y):
        self.x = x
        self.y = y
          
    def fit(self):    
        m = len(self.x)
        slop = (m * (self.x*self.y).sum() - self.x.sum()*self.y.sum()) / (m*(self.x**2).sum() - (self.x.sum())**2)
        inter = ((self.x**2).sum()*self.y.sum() - self.x.sum() * (self.x*self.y).sum()) / (m * (self.x**2).sum() - (self.x.sum())**2)

        return slop, inter

    def predict(self, slop, inter):
        return slop * self.x + inter

    def make_regression(self, line):

        plt.grid()
        plt.scatter(self.x, self.y)
        plt.plot(self.x, line, c='r')
        plt.show()

    def r2_show(self, slop, inter, predict):

        yb = sum(self.y)/len(self.y)
        SST = sum((self.y- yb)**2)
        SSreg = sum((predict - yb)**2)
        R2 = SSreg/SST
        print("R2 : %s" % R2)




