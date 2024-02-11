import numpy as np
from scipy.optimize import fsolve
'''
Skeleton code for finding security strategies.
Please do not change the filename or the function names!
'''

def solve_row(M):

    # Extract coefficients from the payoff matrix
    a = M[0, 0]
    b = M[1, 0]
    c = M[0, 1]
    d = M[1, 1]

    # Define the system of equations
    def equations(p):
        eq1 = a * p + b * (1 - p) - (c * p + d * (1 - p))
        return eq1

    # Solve the system of equations
    p_solution = fsolve(equations, 0.5)  # Initial guess: 0.5

    # Round the solution to two decimal places
    p_solution = round(p_solution[0], 2)

    return p_solution, round(a * p_solution + b * (1 - p_solution),2)

def solve_col(M):

    # Extract coefficients from the payoff matrix
    a = M[0, 0]
    b = M[0, 1]
    c = M[1, 0]
    d = M[1, 1]
    # Define the system of equations
    def equations(q):
        eq1 = a * q + b * (1 - q) - (c * q + d * (1 - q))
        return eq1

    # Solve the system of equations
    q_solution = fsolve(equations, 0.5)  # Initial guess: 0.5

    # Round the solution to two decimal places
    q_solution = round(q_solution[0], 2)

    return q_solution,  round(a * q_solution + b * (1 - q_solution), 2)


def ComputeValue(M):
    '''
    Computes the value and security strategies of a two-player, two-move, zero-sum game. Refer to the HW assignment for details on P1, P2, V1, V2, and M.
    '''

    ### WRITE YOUR CODE BELOW

    p,V1 = solve_row(M)
    q,V2 = solve_col(M)
    P1 = [[p], [1-p]]
    P2 = [[q], [1-q]]


    ### DO NOT EDIT BELOW THIS LINE
    return P1, P2, V1, V2

# Example usage:
payoff_matrix = np.array([[1, 3], [4, 2]])
print(payoff_matrix)
print(ComputeValue(payoff_matrix))


