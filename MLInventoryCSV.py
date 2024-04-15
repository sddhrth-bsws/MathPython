#import libraries

import pandas as panda
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree

#loading CSV
hobby_data = pd.read_excel('/Users/sid/Desktop/abc.xlsx')
print(hobby_data.columns)


x = hobby_data.drop(['Demand'],axis=1)
y = hobby_data['Demand']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

# modelling Prediction
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

model.feature_names_ = list(x.columns)

# make prediction
x_test_new = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12]]
prediction = model.predict(x_test_new)
prediction
