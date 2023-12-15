import pandas as pd


# Define your function
def my_function(x, y, z):
    # Replace this with your actual function
    result = x ** 2 + y ** 2 + z ** 2
    return result


# Load data from an Excel file (assuming you have 'input_data.xlsx' with columns 'x', 'y', 'z')
# data = pd.read_excel('input_data.xlsx')
# data = pd.read_excel('input_data.xlsx', usecols=['x', 'y', 'z'])

data = pd.read_excel('C:\\Users\\SID\\Desktop\\input_data.xlsx')

# Iterate through rows in the DataFrame and compute the results
for index, row in data.iterrows():
    x = row['x']
    y = row['y']
    z = row['z']

    result = my_function(x, y, z)

    print(f"The function result for row {index + 1}: x={x}, y={y}, z={z} is: {result}")
