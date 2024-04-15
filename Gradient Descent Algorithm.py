import numpy as np

# Define the cost function (example: quadratic function)
def cost_function(theta):
    return np.sum((theta - 3) ** 2)

# Gradient of the cost function
def gradient(theta):
    return 2 * (theta - 3)

def gradient_descent(initial_theta, learning_rate, num_iterations):
    theta = initial_theta.copy()

    for i in range(num_iterations):
        cost = cost_function(theta)
        grad = gradient(theta)

        # Update decision variables
        theta -= learning_rate * grad

        theta = np.round(theta,2)

        # Print progress
        if i % 10 == 0:
            print(f'Iteration {i}, Cost: {cost}, Theta: {theta}')

    return theta

# Example usage
initial_theta = np.array([10.0, 10.0])  # Initial values
learning_rate = 0.1
num_iterations = 100

final_theta = gradient_descent(initial_theta, learning_rate, num_iterations)

print('Final Decision Variables:', final_theta)
print('Final cost', cost_function(final_theta))