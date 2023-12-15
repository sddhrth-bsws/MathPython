import sympy as sp

# Define the symbolic variable
x = sp.Symbol('x')

# Define the function to be differentiated
f = x**3 + 2*x**2 - 5*x + 1

# Differentiate the function with respect to x
derivative = sp.diff(f, x)
print("Derivative:", derivative)
