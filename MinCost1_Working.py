from scipy.optimize import minimize
import numpy as np
OR = 500
a = 70
b = 0.5
CP = 35
CHO = 1
CHR = 2
CS = 24
LAMDA = 0.5
ALPHA = 0.01
BETA = 0.05
SR = 150
p = 500
ETA = 5
IP = 0.07
IC = 0.5
L = 0.5
Q = 5000# Change
SIGMA = 7
n = 5
C1 = 0.1
C2 = 0.75
C3 = 2.4
D = 100
TV = 0.1
M =5
E1 = 2.35
E2 = 1.3
G = 4
ZETA = 0.5
X = 0.7

# Define the objective function
'''def objective(x):
    # Replace this with your actual objective function
    return x[0]**2 + x[1]**2 + x[2]**2
'''
def objective(variables):
    T1, T2, T = variables

    return ((1 / T) * (OR + (CP*Q) - (((a-(b*p))/(LAMDA+BETA))*((1.5*LAMDA*((T1)**2))+(0.5*BETA*((T1)**2))+(2*T1)))*CHR
                       + CHO * SR * T1 * (1 - (ALPHA * T1 * 0.5))) + CHO * (ALPHA + LAMDA) * (T2 * (T2 - T1)
                        - 0.5 * (T2 - T1) ** 2 + (0.5 * (ALPHA + LAMDA) ** 2) * (T2 ** 2) * (T2 - T1) -
             ALPHA * T2 * 0.5 * (T2 - T1) ** 2 - ALPHA * 0.5 * (ALPHA + LAMDA) ** 2 * (T2 ** 2) * 0.5 * (T2 - T1) ** 2)
            + CS * ETA * (a - b * p) * (((1 / 6) * LAMDA * T ** 3) - ((1 / 6) * LAMDA * T2 ** 3) + 0.5 * T ** 2
            - T * (0.5 * LAMDA * T2 ** 2 + T2) -0.5 * T2 ** 2 + T2 * (0.5 * LAMDA * T2 ** 2 + T2)) +
            ((0.5) * (n + 1) * (1 / n) * IC * L * SIGMA * CP * Q)+ 8 * (C1 + (2 * D * TV * C2) + (D * TV * C3 * M * Q)
            + (2 * D * E1 + D * E2 * Q) * (1 - ZETA * (1 - np.exp(-X * G)))) + G * T)

# Initial guess for the decision variables
initial_guess = [1,2,5]

# Define any constraints if needed (replace this with your actual constraints)
def constraint1(variables):
    T1, T2, T = variables
    return T1 - T2

def constraint2(variables):
    T1, T2, T = variables
    return T2 - T

def constraint3(variables):
    T1, T2, T = variables
    return T1 - T

def constraint4(variables):
    T1, T2, T = variables
    return T1

def constraint5(variables):
    T1, T2, T = variables
    return T2

def constraint6(variables):
    T1, T2, T = variables
    return T

'''def constraints6(variables):
    T1,T2,T = variables
    return objective(variables)
#constraint_non_negative = {'type': 'ineq', 'fun': lambda x: objective(x)}
'''

constraints = [{'type': 'ineq', 'fun': constraint1},
                {'type': 'ineq', 'fun': constraint2},
                {'type': 'ineq', 'fun': constraint3},
                {'type': 'ineq', 'fun': constraint4},
               {'type': 'ineq', 'fun': constraint5},
               {'type':'ineq','fun':constraint6},
               {'type': 'ineq', 'fun': objective}]

#bounds = [(None, None), (None, None), (None, None)]


# Perform the optimization
result = minimize(objective, initial_guess, constraints=constraints,method='SLSQP')

# Print the optimization result
print("Optimal solution:", result.x)
print("Optimal value:", result.fun)
