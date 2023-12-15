import numpy as np
from scipy.optimize import differential_evolution

# Define the cost function to minimize
def cost_function(x):
    return x[0]**2 + x[1]**2

# Define the constraint function
def constraint(x):
    return x[0] + x[1] - 2  # Example constraint: x0 + x1 - 2 = 0

# Define the bounds for each variable
bounds = [(-10, 10), (-10, 10)]  # Example bounds

# Define the constraint as a dictionary with the 'type' and 'fun'
constraints = [{'type': 'eq', 'fun': constraint}]

result = differential_evolution(cost_function, bounds, constraints=constraints)

# Extract the optimized parameters and the minimum value of the objective function
optimized_params = result.x
min_cost = result.fun

print("Optimized parameters:", optimized_params)
print("Minimum cost:", min_cost)
