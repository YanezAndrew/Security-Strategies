'''
Skeleton code for finding security strategies.
Please do not change the filename or the function names!
'''

import numpy as np

def ComputeValue(M):
    '''
    Computes the value and security strategies of a two-player, two-move, zero-sum game. Refer to the HW assignment for details on P1, P2, V1, V2, and M.
    '''

    ### WRITE YOUR CODE BELOW
    P1 = None
    P2 = None
    V1 = None
    V2 = None

    # Find the maximum value in each row
    row0Min = min(M[0])
    row1Min = min(M[1])
    
    col0Max = max(row[0] for row in M)
    col1Max = max(row[1] for row in M)
    # Find the minimum of the maximum values
    P1 =  [[row0Min],[row1Min]]
    P2 = [[col0Max],[col1Max]]

    V1= 2
    V2 = 2
    



    ### DO NOT EDIT BELOW THIS LINE
    return P1, P2, V1, V2