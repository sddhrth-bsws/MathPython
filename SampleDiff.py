import sympy as sp

# Define the variables and constants
t = sp.symbols('t')
q = sp.Function('q')(t)
B, D, S, T = sp.symbols('B D S T')

# Define the differential equation
diff_eq = sp.Eq(q.diff(t) + B*q, -D)

# Solve the differential equation
sol = sp.dsolve(diff_eq, q)

# Apply the boundary conditions q(0) = S and q(T) = 0
sol_with_bcs = sol.subs(t, 0).subs(q, S), sol.subs(t, T).subs(q, 0)

# Solve for the constants of integration
constant = sp.solve(sol_with_bcs, sp.Symbol('C'))

# Substitute the constants of integration in the solution
solution = sol.subs(constant).simplify()

# Final solution with boundary conditions
final_solution = solution.subs({q: S, t: T})

# Print the solution
print("The solution to the differential equation dq/dt + Bq = -D with boundary conditions q(0) = S and q(T) = 0 is:")
print("q(t) =", final_solution)
print(constant)
