# simple ml model

from sklearn.linear_model import LinearRegression
import numpy as np

class SimpleLinearModel:
    def __init__(self):
        self.model = LinearRegression()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
    
ML_model=SimpleLinearModel()
X_train=np.array([[2,1],[4,2],[8,3]])
y_train=np.array([[7],[14],[27]])
ML_model.fit(X_train,y_train)


print(ML_model.predict([[5,7]]))
