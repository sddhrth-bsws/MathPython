import pulp
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

# Create the model
prob = pulp.LpProblem("Product_Mix", pulp.LpMinimize)

# Define decision variables
T1 = pulp.LpVariable("Time 1", lowBound=0, cat="Integer")
T2 = pulp.LpVariable("Time 2", lowBound=0, cat="Integer")
T = pulp.LpVariable("Time", lowBound=0, cat="Integer")


# Define the objective function
#prob += 50 * x + 75 * y

prob += ((1 / T) * (OR + CP - (0.5) * CHR * (1 + (1 / BETA)) * ((a - b * p) / (LAMDA + BETA)) * (
            (LAMDA * T1 + 2) ** 2) + CHO * SR * T1 * (1 - (ALPHA * T1 * 0.5))) + CHO * (ALPHA + LAMDA) * (
             T2 * (T2 - T1) - 0.5 * (T2 - T1) ** 2 + (0.5 * (ALPHA + LAMDA) ** 2) * (T2 ** 2) * (T2 - T1) -
             ALPHA * T2 * 0.5 * (T2 - T1) ** 2 - ALPHA * 0.5 * (ALPHA + LAMDA) ** 2 * (T2 ** 2) * 0.5 * (
                     T2 - T1) ** 2) + CS * ETA * (a - b * p) * (((1 / 6) * LAMDA * T ** 3) - ((1 / 6) * LAMDA * T2 ** 3)
                                                                + 0.5 * T ** 2 - T * (
                                                                        0.5 * LAMDA * T2 ** 2 + T2) -
                                                                0.5 * T2 ** 2 + T2 * (0.5 * LAMDA * T2 ** 2 + T2)) + (
                 (0.5) * (n + 1) * (1 / n) * IC * L * SIGMA * CP * Q)
     + 8 * (C1 + (2 * D * TV * C2) + (D * TV * C3 * M * Q) + (2 * D * E1 + D * E2 * Q) * (
                    1 - ZETA * (1 - np.exp(-X * G)))) + G * T)

# Define the constraints
'''prob += 2 * x + 3 * y <= 120
prob += x + 2 * y <= 80
'''

prob += T1 < T2
prob += T2 < T


# Solve the problem
prob.solve()

# Print the results
print("Optimal solution:")
print("Time 1:", T1.varValue)
print("Time 2:", T2.varValue)
print("Time:", T.varValue)
print("Min Cost:", pulp.value(prob.objective))