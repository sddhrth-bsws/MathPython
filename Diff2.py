import sympy as sp

# Define the symbolic variable
T = sp.Symbol('T')
t2 = sp.Symbol('t2')
L = sp.Symbol('L')

# Define the function to be differentiated
f = L * ((T - t2)**2)

# Differentiate the function with respect to x
derivative = sp.diff(f, T)
print("Derivative:", derivative)
