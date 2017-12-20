import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
class Estimator():
    def __init__(self):
        self.regression = LinearRegression()
        self.is_trained = False

    def train(self, train_x, train_y):
        self.regression.fit(train_x,train_y)
        self.is_trained = True
        return (self.x,self.y)

        '''
        A training function that wraps the call to your linear regression model,
        and does some basic checking of dimensionality (AKA dim(x) is compatible with dim(y))

        :param train_x:
        :param train_y:
        :return some indicator of success if you complete, otherwise, throw some sort of descriptive error:
        '''





    def predict(self, test_x):
        if self.is_trained:
            return self.regression.predict(test_x)
        else:
             print("Error! Mdel nt trained")
        '''

        :param test_x: a 2-d array modeling the variables/features of interest in our model. should be a compatible dimension as
        train_x from the train() call.
        :return: a vector/1-d array of predictions for each instance of test_x
        '''







def main():
    '''
    put your test loop here. It should create a new Estimator, train it, and predict some new dataset.

    '''

if __name__ == "__main__":
    '''
    the above is a common bit of code that will conditionally run whatever is within the conditional statement
    if the file it is in is the main entry point into the code
    IE: it is invoked like
    >: python basic_classes.py
    '''

    main()
