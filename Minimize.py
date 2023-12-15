from scipy.optimize import differential_evolution
import numpy as np

OR = 500
a = 70
b = 0.5
CP = 35
CHO = 1
CHR = 2
CS = 24
LAMDA = 0.9
ALPHA = 0.01
BETA = 0.05
SR = 150
p = 50
ETA = 5
IP = 0.07
IC = 0.5
L = 0.5
Q = 500 # Change
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


# Define your equation based on all 10 variables
def objective_func(variables):
    #x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = variables
    T1, T2, T, = variables

    # Define your equation based on all 10 variables
    #equation_result = x1 + x2 + x3 + x4 + x5 + x6 + x7 - (x8 + x9 + x10)  # Example equation

    #to maximize multiply with -1
    return ((-1/T)*(OR + CP - (0.5) * CHR * (1 + (1 / BETA)) * ((a - b * p) / (LAMDA + BETA)) * (
            (LAMDA * T1 + 2) ** 2) + CHO * SR * T1 * (1 - (ALPHA * T1 * 0.5))) +CHO * (ALPHA + LAMDA) * (
                      T2 * (T2 - T1) - 0.5 * (T2 - T1) ** 2 + (0.5 * (ALPHA + LAMDA) ** 2) * (T2 ** 2) * (T2 - T1) -
                      ALPHA * T2 * 0.5 * (T2 - T1) ** 2 - ALPHA * 0.5 * (ALPHA + LAMDA) ** 2 * (T2 ** 2) * 0.5 * (
                                  T2 - T1) ** 2) +CS * ETA * (a - b * p) * (((1 / 6) * LAMDA * T ** 3) - ((1 / 6) * LAMDA * T2 ** 3)
                                                                            + 0.5 * T ** 2 - T * (
                        0.5 * LAMDA * T2 ** 2 + T2) -
                                    0.5 * T2 ** 2 + T2 * (0.5 * LAMDA * T2 ** 2 + T2))+ ((0.5) * (n + 1) * (1 / n) * IC * L * SIGMA * CP * Q)
                       + 8 * (C1 + (2 * D * TV * C2) + (D * TV * C3 * M * Q) + (2 * D * E1 + D * E2 * Q) * (
                        1 - ZETA * (1 - np.exp(-X * G)))) + G * T)

# Define constraint(s) connecting the unknown variables
'''constraints = [
    {'type': 'ineq', 'fun': lambda variables: variables[0] - variables[1]},  # x8 >= x9
    {'type': 'ineq', 'fun': lambda variables: variables[1] - variables[2]},
    {'type': 'ineq', 'fun': lambda variables: variables[0]}, # x10 >= 0
    {'type': 'ineq', 'fun': lambda variables: variables[1]},
    {'type': 'ineq', 'fun': lambda variables: variables[2]}
]'''

def penalty_function(variables):
    T1, T2, T, = variables
    penalty = 0.0

    # Constraint: x8 >= x9
    if T2 < T1:
        penalty += (T2 - T1) ** 2  # You can customize the penalty term as needed

    if T < T2:
        penalty += (T - T2) ** 2

    # Constraint: x10 >= 0
    if T1 < 0:
        penalty += (T1 ** 2)  # You can customize the penalty term as needed

    if T2 < 0:
        penalty += (T2 ** 2)

    if T < 0:
        penalty += (T ** 2)

    return penalty

# Define bounds for all 10 variables (assuming lower and upper bounds)
variable_bounds = [(1,10), (10, 100),
                   (100,1000)]

# Create a bounds tuple for use in differential_evolution
bounds = tuple(variable_bounds)

# Define the optimization problem

result = differential_evolution(lambda x: objective_func(x) + penalty_function(x), bounds)

T1, T2, T = result.x

# Print the solutions
print(f"T1 = {T1}, T2 = {T2}, T = {T}")
