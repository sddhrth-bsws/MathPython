import numpy as np

# Define the cost function (example: quadratic function)
def cost_function(theta):
    return np.sum((theta - 3) ** 2)

# Gradient of the cost function
def gradient(theta, x):
    return 2 * (theta - 3) * x

def stochastic_gradient_descent(initial_theta, learning_rate, num_iterations, batch_size, data):
    theta = initial_theta.copy()

    for i in range(num_iterations):
        # Shuffle the dataset
        np.random.shuffle(data)

        for j in range(0, len(data), batch_size):
            # Select mini-batch
            mini_batch = data[j:j+batch_size]

            # Compute the gradient using the mini-batch
            grad = np.mean([gradient(theta, x) for x in mini_batch], axis=0)

            # Update decision variables
            theta -= learning_rate * grad

        # Print progress
        if i % 10 == 0:
            cost = cost_function(theta)
            print(f'Iteration {i}, Cost: {cost:.2f}, Theta: {theta}')

    return theta

# Example usage
initial_theta = np.array([0.0, 0.0])  # Initial values
learning_rate = 0.1
num_iterations = 100
batch_size = 32

# Sample data (replace with your dataset)
data = np.random.rand(100, 2)

final_theta = stochastic_gradient_descent(initial_theta, learning_rate, num_iterations, batch_size, data)
print('Final Decision Variables:', final_theta)
print('Final cost', cost_function(final_theta))
