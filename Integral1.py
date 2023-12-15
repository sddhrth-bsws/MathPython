import sympy as sp

# Define the symbolic variable
t2 = sp.Symbol('t2')
t = sp.Symbol('t')
T = sp.Symbol('T')
L = sp.Symbol('L')

# Define the function to be integrated
f = ((t - T) * (1 + (t + T) * L/2)) - ((t2-T)*(1+(t2+T)*L/2))

# Define the integration limits
a = t2
b = T

# Calculate the definite integral
definite_integral = sp.integrate(f, (t, a, b))
print("Definite integral:", definite_integral)