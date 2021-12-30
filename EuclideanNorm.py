import numpy as np

def EuclideanNorm(InputMatrix):
    
    # Multiply InputMatrix element-wise and perform sum along 1 axis, finally take square root of sum
    RowwiseNorm = np.sqrt(np.sum(InputMatrix*InputMatrix, axis = 1))
    
    return RowwiseNorm


Matrix = np.array([[0,1,2],[3,4,5],[6,7,8]])
EuclideanNorm(Matrix)