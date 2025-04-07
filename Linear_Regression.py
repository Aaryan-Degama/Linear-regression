import numpy as np

class LinearReg:

    # The fit function trains the Model on the vecotrs X and y
    def fit(self, X, y):
        self.X = X
        self.y = y

        # This is the equations that follows the Linear regression Model
        x_mean = np.mean(X)
        y_mean = np.mean(y)
        numerator = np.sum((X - x_mean) * (y - y_mean))
        denominator = np.sum((X - x_mean) ** 2)
        self.m = numerator / denominator
        self.c = y_mean - self.m * x_mean

        # To make a string which follows he mathematical equation of the Linear Regression Model Trained on X and y
        self.equ = f"y = {self.m:.3f}x + {self.c:.3f}"
    

    # The predict function predicts the values according to the data trained by the fir function
    def predict(self,X_test) -> np.ndarray :
        return self.m * X_test + self.c
    

    # The getEquation functions gets the linear equation for the regression on the data X and y
    def getEquation(self) ->str :
        return self.equ