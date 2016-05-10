'''
Created on May 4, 2016

@author: Edielson
'''
import numpy as np

DEFAULT_MAX_ITERATIONS = 4

class Scaling(object):
    '''
    classdocs
    '''
    

    def __init__(self, max_iterations = None):
        '''
        Constructor
        '''
        
        # Define the maximum number of iterations. 
        # If not specified by the user, use the default number of iterations. 
        if max_iterations == None:
            self.__max_it = DEFAULT_MAX_ITERATIONS
        else:
            self.__max_it = max_iterations
            
    def GeometricMean(self,A):
        '''
        Constructor
        '''
        
        #number of rows in the matrix X
        m = len(A)
        n = len(A.transpose())
        
        r = np.zeros(m)
        s = np.zeros(n)
        
        t=0
        X = A
                
        while t < self.__max_it:
            print('iteration: %s'%(t+1))
            for i in xrange(m):
                #get the maximum value at row i
                max_x = np.asscalar(np.max(X[i,:], 1))
                #get the minimum value at row i
                min_x = np.asscalar(np.min(X[i,:], 1))
                #calculate the geometric mean
                r[i]=np.nan_to_num(1.0*np.sqrt(1.0/(max_x*min_x)))

            #mount the respective diagonal matrix for r
            R = np.diag(r)
            #scale matrix X based on R
            X=R*X 
                        
            for j in xrange(n):
                #get the maximum value at column j
                max_x = np.asscalar(np.max(X[:,j], 0))
                #get the minimum value at column j
                min_x = np.asscalar(np.min(X[:,j], 0))
                #calculate the geometric mean
                s[j]=np.nan_to_num(1.0*np.sqrt(1.0/(max_x*min_x)))    
            
            #mount the respective diagonal matrix for s
            S = np.diag(s)
            #scale matrix X based on S
            X=X*S
            t=t+1
            
        return X
    
    def ArithmeticMean(self,A):
        
        #number of rows in the matrix X
        m = len(A)
        n = len(A.transpose())
        
        r = np.zeros(m)
        s = np.zeros(n)
        
        t=0
        X = A
                
        while t < self.__max_it:
            print('iteration: %s'%(t+1))
            for i in xrange(m):
                #get the sum of the values at row i
                sum_x = np.asscalar(np.sum(X[i,:], 1))
                #calculate the arithmetic mean
                r[i]=np.nan_to_num(1.0*n/sum_x)

            #mount the respective diagonal matrix for r
            R = np.diag(r)
            #scale matrix X based on R
            X=R*X 
                        
            for j in xrange(n):
                #get the sum of the values at column j
                sum_x = np.asscalar(np.sum(X[:,j], 0))
                #calculate the arithmetic mean
                s[j]=np.nan_to_num(1.0*m/sum_x)    
            
            #mount the respective diagonal matrix  s
            S = np.diag(s)
            #scale matrix X based on S
            X=X*S
            t=t+1
            
        return X    
    
    def Equilibration(self,X):
        
        #number of rows in the matrix X
        m = len(X)
        n = len(X.transpose())
        
        for i in xrange(m):
            #get the maximum value at row i
            max_x = np.asscalar(np.max(X[i,:], 1))
            X[i,:]=[X[i,j]/max_x for j in range(n)]
            
        for j in xrange(n):
            #get the maximum value at column j
            max_x = np.asscalar(np.max(X[:,j], 0))
            X[:,j]=np.matrix([X[i,j]/max_x for i in range(m)]).transpose()
                
        return X    