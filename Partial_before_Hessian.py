import sympy as sp

# Define symbolic variables
x, y, z, a, b, c = sp.symbols('x y z a b c')

# Define the function
f = x**2 + y**3 + z**4

# Compute the partial derivatives
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)
df_dz = sp.diff(f, z)

# Set up the system of equations
equations = [sp.Eq(df_dx, 0), sp.Eq(df_dy, 0), sp.Eq(df_dz, 0)]

# Solve the system of equations
solution = sp.solve(equations, (x, y, z))

# Display the partial derivatives and the solution
print("Partial Derivative with respect to x:")
print(df_dx)

print("\nPartial Derivative with respect to y:")
print(df_dy)

print("\nPartial Derivative with respect to z:")
print(df_dz)

print("\nSolution:")
print(solution)
