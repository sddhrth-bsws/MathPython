import sympy as sp

# Define the symbolic variable
x = sp.Symbol('x')
z = sp.Symbol('z')

# Define the function to be integrated
f = z*x**2

# Define the integration limits
a = 0
b = 1

# Calculate the definite integral
definite_integral = sp.integrate(f, (x, a, b))
print("Definite integral:", definite_integral)