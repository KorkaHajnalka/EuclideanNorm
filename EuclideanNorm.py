import numpy as np

def EuclideanNorm(InputMatrix):

    RowwiseNorm = [np.dot(InputMatrix[i],InputMatrix[i]) for i in range(len(InputMatrix))]
    
    return RowwiseNorm


Matrix = np.array([[0,1,2],[3,4,5],[6,7,8]])
EuclideanNorm(Matrix)