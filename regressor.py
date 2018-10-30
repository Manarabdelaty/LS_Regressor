# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 13:57:20 2018

@author: Dell
"""
import numpy  as np
import matplotlib.pyplot as plt 
from numpy.linalg import inv

        
class Regressor:
   
    
    def __init__(self):
        print("")
               
    def poly_fit(self, Xtr, Ytr, M):
        Xtrain = Xtr
        for i in range(2,M+1):
            X_i = np.power(Xtr, i)
            Xtrain = np.append(Xtrain , X_i , axis = 1)
        X  = np.append(Xtrain, np.ones((Xtrain.shape[0], 1)) , axis = 1)    
        # X  = Xtr                       # Design Matrix. One row --> [X1 X2 X3 ...Xd 1]
        Xt = np.transpose(X)           
        W  = np.matmul(Xt , X)
        Winv = inv(W)
        W = np.matmul(Winv,Xt)
        W = np.matmul(W,Ytr)                  # W --> [W1, W2,.., Wd, W0] . d is the number of features
        #W = np.append( W[-1], W[:len(W)-1])   # W --> [W0, W1, W2, W3, ... ,Wd]
        #W = W[::-1]                  
        return W 
    
    def predict(self, Xtr, W, M):   # y(x) = Wtranspose * X
        Xtrain = Xtr
        for i in range(2,M+1):
            X_i = np.power(Xtr, i)
            Xtrain = np.append(Xtrain , X_i , axis = 1)
        Xtrain  = np.append(Xtrain, np.ones((Xtrain.shape[0], 1)) , axis = 1) 
        X = np.transpose(Xtrain)
        y_predicted = np.matmul(np.transpose(W), X)
        return y_predicted
    
    def error_rms(self, y , y_pred):
        N = len(y)
        err = y_pred - y
        err_square = np.power(err, 2)
        err_sum  = np.sum(err_square, axis  = 0)
        err_sum  = 0.5 * err_sum
        err_rms  = np.sqrt((2*err_sum) / N )
        return (err_rms)
   
        
    def plot(self, X, Y, W, fig_num=0):
        plt.figure(fig_num)
        plt.figure(figsize=(6*3.13,4*3.13))
        plt.title("LS Model")
        print("x  " , X[:, 0])
        print("Y  " , Y[:, 0])
        plt.plot(X[:, 0], Y[:, 0], 'ro')
        x= np.linspace(30, 80, 100)
        y= W[0]
        for i in range (1, len(W)):
            y = y + (W[i] *x**(i))
        plt.plot(x,y,'co')
        plt.show()
        