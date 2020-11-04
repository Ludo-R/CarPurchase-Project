#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:31:10 2020

@author: randon
"""


import numpy as np
import matplotlib.pyplot as plt

def model(X, theta):
    return X.dot(theta)

def cost_function(X,y,theta):
    m = len(y)
    return 1/(2*m) * np.sum((model(X, theta) - y)**2)

def grad(X, y, theta):
    m = len(y)
    return 1/m * X.T.dot(model(X,theta) - y)

def gradient_descent(X,y,theta, learning_rate, n_iterations):
    cost_history = np.zeros(n_iterations)
    for i in range(0, n_iterations):
        theta = theta - learning_rate * grad(X, y, theta)
        cost_history[i] = cost_function(X, y, theta)
    return theta, cost_history

def coef_determination(y, pred):
    u = ((y - pred)** 2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v

def make_regression(x,y):  
    x = x.reshape(x.shape[0],1)
    y = y.reshape(y.shape[0],1)

    X = np.hstack((x, np.ones(x.shape)))

    theta = np.random.randn(2,1)
    
    theta_final, cost_history = gradient_descent(X, y, theta, learning_rate=0.001, n_iterations=1000)

    predictions = model(X, theta_final)
    plt.scatter(x,y)
    plt.plot(x, predictions, c='r')

    print(coef_determination(y, predictions))