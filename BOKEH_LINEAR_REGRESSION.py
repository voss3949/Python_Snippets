from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from sklearn.linear_model import LinearRegression
import numpy as np

# Create some sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Fit a linear regression model to the data
model = LinearRegression().fit(x.reshape((-1, 1)), y)

# Predict the y values for the original data using the model
y_pred = model.predict(x.reshape((-1, 1)))

# Create a Bokeh data source from the original and predicted data
data = ColumnDataSource(data=dict(x=x, y=y, y_pred=y_pred))

# Create a figure
fig = figure(title="Linear Regression Example")

# Add a scatter plot to the figure
fig.scatter(x='x', y='y', source=data, size=10, color='blue')

# Add a line plot of the predicted values to the figure
fig.line(x='x', y='y_pred', source=data, color='red')

# Set the output file name
output_file("C:\\Users\\12245\\OneDrive\\Documents\\Python_Projects\\Data\\linear_regression.html")

# Show the plot
show(fig)
