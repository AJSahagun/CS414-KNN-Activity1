import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from os import path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, confusion_matrix

# Get the project root
PROJECT_ROOT = path.abspath(path.dirname(path.dirname(__file__)))

# Define the data directory path
DATA_DIR = path.join(PROJECT_ROOT, "Dataset")

# Define the data file path
DATA_FILE = path.join(DATA_DIR, "Student-Employability-Datasets.xlsx")

# Load the Excel file
df = pd.read_excel(DATA_FILE, sheet_name='Data')

# Prepare data for classification using the best features
X_class = df[['GENERAL APPEARANCE', 'MANNER OF SPEAKING', 'SELF-CONFIDENCE']]
y_class = df['CLASS']  # Target column for classification

# Split the data into training and testing sets for classification
X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_class, y_class, test_size=0.2, random_state=40)

# Standardize the features
scaler = StandardScaler()
X_train_class_scaled = scaler.fit_transform(X_train_class)
X_test_class_scaled = scaler.transform(X_test_class)

# Define variables needed for plotting
X = scaler.fit_transform(X_class)
y_train_class_scaled = y_train_class.map({'Employable': 1, 'LessEmployable': 0}).to_numpy()
y_test_class_scaled = y_test_class.map({'Employable': 1, 'LessEmployable': 0}).to_numpy()
    
# Initialize the KNN classifier
knn_classifier = KNeighborsClassifier(n_neighbors=5)  # You can adjust n_neighbors if needed

# Train the classifier
knn_classifier.fit(X_train_class_scaled, y_train_class)

# Predict class labels for the test set
y_pred_class = knn_classifier.predict(X_test_class_scaled)

# Evaluate the classification model
confusion = confusion_matrix(y_test_class, y_pred_class)
print(f"\nConfusion Matrix:\n{confusion}")

class_report = classification_report(y_test_class, y_pred_class)
print("\nClassification Report:")
print(class_report)

accuracy = accuracy_score(y_test_class, y_pred_class)
print(f"Classification Accuracy: {accuracy * 100:.2f}%")

# Prepare data for regression using the best features
X_reg = df[['GENERAL APPEARANCE', 'MANNER OF SPEAKING', 'SELF-CONFIDENCE']]  # Feature column for regression
y_reg = df['Student Performance Rating']  # Target column for regression

# Split the data into training and testing sets for regression
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=40)

# Standardize the features for regression
scaler_reg = StandardScaler()
X_train_reg_scaled = scaler_reg.fit_transform(X_train_reg)
X_test_reg_scaled = scaler_reg.transform(X_test_reg)

# Initialize the KNN regressor
knn_regressor = KNeighborsRegressor(n_neighbors=4)

# Train the regressor
knn_regressor.fit(X_train_reg_scaled, y_train_reg)

# Predict the values for the test set
y_pred_reg = knn_regressor.predict(X_test_reg_scaled)

# Evaluate the regression model
mse = mean_squared_error(y_test_reg, y_pred_reg)
print(f"\nRegression Mean Squared Error: {mse:.2f}")

# Print actual vs. predicted values for regression
print("\nActual vs. Predicted (Regression):")
for actual, predicted in zip(y_test_reg[:5], y_pred_reg[:5]):  # Show first 5 predictions for simplicity
    print(f"Actual: {actual:.2f}, Predicted: {predicted:.2f}")

# Creating a mesh grid for 3D space
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
z_min, z_max = X[:, 2].min() - 1, X[:, 2].max() + 1
xx, yy, zz = np.meshgrid(np.linspace(x_min, x_max, 30),
                         np.linspace(y_min, y_max, 30),
                         np.linspace(z_min, z_max, 30))

# Predict class for each point in the meshgrid
grid_points = np.c_[xx.ravel(), yy.ravel(), zz.ravel()]
Z = knn_classifier.predict(grid_points)
Z = Z.reshape(xx.shape)
Z_numeric = np.where(Z == 'LessEmployable', 0, 1) #Converts the class to numerical values

# Plot the 3D scatter plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the decision boundaries using the meshgrid
ax.scatter(xx, yy, zz, c=Z_numeric, alpha=0.1, cmap='coolwarm', marker='.')

# Plot the actual data points
scatter_train = ax.scatter(X_train_class_scaled[:, 0], X_train_class_scaled[:, 1], X_train_class_scaled[:, 2], 
                          c=y_train_class_scaled, cmap='coolwarm', marker='o', edgecolor='k')
scatter_test = ax.scatter(X_test_class_scaled[:, 0], X_test_class_scaled[:, 1], X_test_class_scaled[:, 2], 
                         c=y_test_class_scaled, cmap='coolwarm', marker='^', edgecolor='k')

# Create a legend
handles = [
    Line2D([0], [0], marker='o', color='w', label='Training Employable',
           markerfacecolor='red', markersize=10, markeredgecolor='k'),
    Line2D([0], [0], marker='^', color='w', label='Test Employable',
           markerfacecolor='red', markersize=10, markeredgecolor='k'),
    Line2D([0], [0], marker='o', color='w', label='Training Less Employable',
           markerfacecolor='blue', markersize=10, markeredgecolor='k'),
    Line2D([0], [0], marker='^', color='w', label='Test Less Employable',
           markerfacecolor='blue', markersize=10, markeredgecolor='k')
]
ax.legend(handles=handles, loc='upper right')

# Labels and title
ax.set_xlabel('GENERAL APPEARANCE')
ax.set_ylabel('MANNER OF SPEAKING')
ax.set_zlabel('SELF CONFIDENCE')
ax.set_title('KNN Classification of Student Employability')

# Show the figure
plt.show()
