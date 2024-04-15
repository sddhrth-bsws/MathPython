import pulp

# Create the model
prob = pulp.LpProblem("Product_Mix", pulp.LpMaximize)

# Define decision variables
x = pulp.LpVariable("Product_A", lowBound=0, cat="Integer")
y = pulp.LpVariable("Product_B", lowBound=0, cat="Integer")

# Define the objective function
prob += 50 * x + 75 * y

# Define the constraints
prob += 2 * x + 3 * y <= 120
prob += x + 2 * y <= 80

# Solve the problem
prob.solve()

# Print the results
print("Optimal solution:")
print("Product A:", x.varValue)
print("Product B:", y.varValue)
print("Maximum profit:", pulp.value(prob.objective))
