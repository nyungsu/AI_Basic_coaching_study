import numpy as np

class LinearRegression():
    def __init__(self,fit_intercept=True, copy_X = True):
        self.fit_intercept = fit_intercept
        self.copy_X = copy_X
        
        self._coef = None
        self._intercept = None
        self._new_X = None 
        
    def fit(self, X, y):
        self._new_X = np.array(X)
        y = y.reshape(-1,1)
        
        if self.fit_intercept:
            intercept_vector = np.ones([len(self._new_X), 1])
            self._new_X = np.concatenate(
                (intercept_vector, self._new_X), axis=1
            )
        
        weights = np.linalg.inv(
            self._new_X.T.dot(self._new_X)).dot(
                self._new_X.T.dot(y)).flatten()                   