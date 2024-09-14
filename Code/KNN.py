from os import path
import pandas as pd
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
