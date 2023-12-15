import sympy as sp

# Define symbolic variables
x, y, z, a, b, c = sp.symbols('x y z a b c')

# Define the function
f = x**a + y**b + z**c

# Compute the Hessian matrix
hessian_matrix = sp.hessian(f, (x, y, z))

# Evaluate the Hessian matrix
hessian_matrix_evaluated = hessian_matrix.doit()

# Display the Hessian matrix as a formatted matrix
print("Hessian Matrix:")
sp.pretty_print(sp.Matrix(hessian_matrix_evaluated))
