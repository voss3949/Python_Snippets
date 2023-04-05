import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create some sample data
X = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
y = np.array([2, 4, 5, 4, 5])

# Create a linear regression model and fit it to the data
model = LinearRegression()
model.fit(X, y)

# Predict the y values for the original data using the model
y_pred = model.predict(X)

# Plot the original data and the predicted values
plt.scatter(X, y)
plt.plot(X, y_pred, color='red')
plt.show()
