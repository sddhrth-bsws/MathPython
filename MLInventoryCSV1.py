import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the data
hobby_data = pd.read_excel('/Users/sid/Desktop/abc.xlsx')

# Extract lower and upper bounds from 'Demand' column
hobby_data[['Demand_Lower', 'Demand_Upper']] = hobby_data['Demand'].str.split('-', expand=True)

# Convert the lower and upper bounds to numeric values
hobby_data[['Demand_Lower', 'Demand_Upper']] = hobby_data[['Demand_Lower', 'Demand_Upper']].apply(pd.to_numeric)

# Encode categorical features
label_encoder = LabelEncoder()
hobby_data['Month'] = label_encoder.fit_transform(hobby_data['Month'])

# Separate features (X) and target variable (y)
X = hobby_data[['Month']]
y_lower = hobby_data['Demand_Lower']
y_upper = hobby_data['Demand_Upper']

# Split the data into training and testing sets
X_train, X_test, y_lower_train, y_lower_test, y_upper_train, y_upper_test = train_test_split(X, y_lower, y_upper,
                                                                                             test_size=0.20,
                                                                                             random_state=42)

# Modeling: Decision Tree Regressor for lower bounds
model_lower = DecisionTreeRegressor()
model_lower.fit(X_train, y_lower_train)

# Modeling: Decision Tree Regressor for upper bounds
model_upper = DecisionTreeRegressor()
model_upper.fit(X_train, y_upper_train)

# Make predictions for all 12 months
months_to_predict = range(1, 13)

for month in months_to_predict:
    X_test_new = pd.DataFrame({'Month': [month]})
    X_test_new['Month'] = label_encoder.transform(X_test_new['Month'])

    prediction_lower = model_lower.predict(X_test_new)
    prediction_upper = model_upper.predict(X_test_new)

    # Predict the midpoint of the range
    predicted_value = (prediction_lower[0] + prediction_upper[0]) / 2

    print(f"Month {month}: Predicted Value: {predicted_value}")
