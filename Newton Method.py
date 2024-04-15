import numpy as np
from scipy.optimize import minimize


# Define the cost function (example: quadratic function)
def cost_function(theta):
    return np.sum((theta - 3) ** 2)


# Gradient of the cost function
def gradient(theta):
    return 2 * (theta - 3)


# Hessian matrix of the cost function
def hessian(theta):
    return np.array([[2, 0], [0, 2]])


# Newton's Method using scipy.optimize.minimize
def newtons_method(initial_theta, num_iterations):
    theta = initial_theta.copy()

    for i in range(num_iterations):
        # Compute the gradient and Hessian using minimize
        result = minimize(cost_function, theta, method='trust-exact', jac=gradient, hess=hessian)

        # Update decision variables using Newton's method
        theta = result.x

        # Print progress
        cost = result.fun
        print(f'Iteration {i}, Cost: {cost:.2f}, Theta: {theta}')

    return theta


# Example usage
initial_theta = np.array([0.0, 0.0])  # Initial values
num_iterations = 10

final_theta = newtons_method(initial_theta, num_iterations)
print('Final Decision Variables:', final_theta)
