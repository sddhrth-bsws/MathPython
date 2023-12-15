def my_function(x, y, z):
    # Replace this with your actual function
    result = x ** 2 + y ** 2 + z ** 2
    return result


# Define lists of input values
x_values = [2.0, 3.0, 4.0]
y_values = [1.0, 2.0, 3.0]
z_values = [0.0, 1.0, 2.0]

# Iterate through the lists and compute the results
for x, y, z in zip(x_values, y_values, z_values):
    result = my_function(x, y, z)
    print(f"The function result for x={x}, y={y}, z={z} is: {result}")
