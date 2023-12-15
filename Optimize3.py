from scipy.optimize import fsolve
import numpy as np

OR = 500
a = 70
b = 0.5
CP = 35
CHO = 1
CHR = 2
LAMDA = 5
ALPHA = 0.01
BETA = 0.05
SR = 150
p = 50

def equation(T1,T,X):
    #T1, T, X = variables

# Define your equation here
    #equation_result =(T*X) - [OR + CP -(0.5)*CHR*(1+(1/BETA))*((a-b*p)/(LAMDA+BETA))*((LAMDA*T1+2)**2)+CHO*SR*T1*(1-(ALPHA*T1*0.5))] # Example equation

    return (T * X) - (OR + CP - (0.5) * CHR * (1 + (1 / BETA)) * ((a - b * p) / (LAMDA + BETA)) * (
                (LAMDA * T1 + 2) ** 2) + CHO * SR * T1 * (1 - (ALPHA * T1 * 0.5)))

solutions = []
# Replace 100 with the range you're interested in
for T1 in np.arange(0,10,0.01):
    for T in np.arange(0,100,1):
        for X in np.arange(0,1000,1):
            if equation(T1, T, X) == 0:  # or some small number if a floating point equation
                solutions.append((T1, T, X))
'''

if equation(T1, T, X)==0:
    solutions.append((T1, T, X))
    
'''
print("Solutions are:")
for solution in solutions:
    print("x={}, y={}, z={}".format(*solution))
