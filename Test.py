import numpy as np
from scipy.optimize import minimize


Co = 10
Cp = 50
Ch = 0.5
Cb = 20
Cd = 50
Cl = 10
Theta = 0.05
Lambda = 0.35
Ts = 0.5
Beta = 0.007
K = 0.9
a = 60
b = 0.5
p = 60

AbP = a - (b*p)
LB = Lambda + Beta
LBTh = Lambda + Beta + Theta
Const = AbP / (LB)


# Define the cost function
def cost_function(variables):
    T1, T = variables

    return ((1/T)(Co + Cp*(Const/LBTh)*((Theta*np.exp(LB*Ts)) -(LBTh) - (LB)*np.exp(Lambda*T1 + Beta*Ts) + (AbP)*((2*np.exp(Lambda * T1))/(LBTh) + (K/Lambda)*(np.exp(Lambda*T1)+np.exp(Lambda*T)))) + Ch*((Const)*((1/Lambda) - (np.exp(Lambda*Ts))/Lambda) + ((Const/LBTh)*((Theta*np.exp(LB*Ts)) -(LBTh) - (LB)*np.exp(Lambda*T1 + Beta*Ts)))*((1-np.exp(-Beta*Ts))/Beta) + (Const)*((1-np.exp(-Beta*Ts))/Beta)) + Cd*(Const)((np.exp(Lambda*T1))*(T1 - Ts) + ((np.exp(Lambda*T1) - np.exp(Lambda*Ts))/Lambda) - np.exp(Lambda*Ts) - np.exp(Lambda*T1)) + Cb*((K*AbP/Lambda)*((np.exp(Lambda*T) - np.exp(Lambda*T1))/Lambda) - (K*AbP*np.exp(Lambda*T)/Lambda)*(T - T1) + (AbP)*(T-T1)*((2*(np.exp(Lambda*T1))/LBTh)) + (K * (T - T1) * ((np.exp(Lambda*T1)) + np.exp(Lambda*T))/Lambda)) + Cl*(AbP)*(1 - K)*(np.exp(T) - np.exp(T1))))


def constraint1(variables):
    T1, T = variables
    return T - T1

def constraint2(variables):
    T1, T = variables
    return T - Ts

def constraint3(variables):
    T1, T = variables
    return T1

def constraint4(variables):
    T1, T = variables
    return T


# Initial guess for the parameters
initial_guess = [1,15]
#initial_guess = np.zeros(3)

bounds = [(None, None), (None, None)]

constraints = [{'type': 'ineq', 'fun': constraint1},
                {'type': 'ineq', 'fun': constraint2},
                {'type': 'ineq', 'fun': constraint3},
                {'type': 'ineq', 'fun': constraint4}]

# Call the optimization function
#result = minimize(cost_function, initial_guess, method='BFGS')  # You can choose a different method
result = minimize(cost_function, initial_guess, bounds=bounds, constraints=constraints, method='SLSQP')


# Extract the optimized parameters
optimized_params = result.x

print("Optimized parameters:", optimized_params)
print("Minimum cost:", result.fun)