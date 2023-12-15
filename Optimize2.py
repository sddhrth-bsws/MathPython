from scipy.optimize import fsolve
import numpy as np

# Define your equation based on the known variables and the three unknown variables
# Provide the known values for the seven variables
OR = 500
a = 70
b = 0.5
CP = 35
CHO = 1
CHR = 2
LAMDA = 0.5
ALPHA = 0.01
BETA = 0.05
SR = 150
p = 50
def equation(variables):
    T1, T, X = variables

    # Define your equation based on the known variables and the 3 unknown variables
    equation_result =(T*X) - [OR + CP -(0.5)*CHR*(1+(1/BETA))*((a-b*p)/(LAMDA+BETA))*((LAMDA*T1+2)**2)+CHO*SR*T1*(1-(ALPHA*T1*0.5))] # Example equation

    return equation_result



# Calculate the known sum
#known_sum = value1 + value2 + value3 + value4 + value5 + value6 + value7

# Create bounds for the three unknown variables (if applicable)
# For simplicity, let's assume they are unconstrained
variable_bounds = [(0, 7), (0, 50), (5000, 10000)]

# Define a function to find solutions with different initial guesses
def find_multiple_solutions(initial_guesses):
    solutions = []
    for initial_guess in initial_guesses:
        result = fsolve(equation, initial_guess)
        # Check if the result is within bounds for each variable
        within_bounds = all(lower <= x <= upper for (lower, upper), x in zip(variable_bounds, result))
        if within_bounds:
            solutions.append(result)
    return solutions

# Provide your own initial guesses as a list of tuples
user_provided_initial_guesses = [(7.0,50.0,5000.0)]  # Add more as needed

# Find multiple solutions using user-provided initial guesses
multiple_solutions = find_multiple_solutions(user_provided_initial_guesses)

# Print the multiple solutions
for i, solution in enumerate(multiple_solutions):
    T1, T, X = solution
    print(f"Solution {i + 1}: T1 = {T1}, T = {T}, var10 = {X}")
