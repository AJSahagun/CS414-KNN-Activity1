import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, confusion_matrix
from itertools import combinations

# Correct file path
file_path = r'.\Dataset\Student-Employability-Datasets.xlsx'

# Load the Excel file
df = pd.read_excel(file_path, sheet_name='Data')

# Print the column names to verify
print("Column Names in DataFrame:", df.columns)

# Prepare data for classification
def evaluate_features(features):
    X_class = df[list(features)]  # Convert tuple to list
    y_class = df['CLASS']  # Target column for classification

    # Split the data into training and testing sets for classification
    X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_class, y_class, test_size=0.2, random_state=40)

    # Standardize the features
    scaler = StandardScaler()
    X_train_class_scaled = scaler.fit_transform(X_train_class)
    X_test_class_scaled = scaler.transform(X_test_class)

    # Hyperparameter Tuning using Grid Search
    param_grid = {
        'n_neighbors': [3, 5, 7, 9],
        'weights': ['uniform', 'distance']
    }
    grid_search = GridSearchCV(estimator=KNeighborsClassifier(), param_grid=param_grid, cv=5)
    grid_search.fit(X_train_class_scaled, y_train_class)

    # Best parameters from Grid Search
    print(f"Best Parameters: {grid_search.best_params_}")

    # Initialize the KNN classifier with the best parameters
    knn_classifier = KNeighborsClassifier(n_neighbors=grid_search.best_params_['n_neighbors'],
                                           weights=grid_search.best_params_['weights'])

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
    return accuracy

# List all features
all_features = ['GENERAL APPEARANCE', 'MANNER OF SPEAKING', 'PHYSICAL CONDITION', 
                 'MENTAL ALERTNESS', 'SELF-CONFIDENCE', 'ABILITY TO PRESENT IDEAS', 
                 'COMMUNICATION SKILLS']

# Evaluate all combinations of features
best_accuracy = 0
best_features = None

for r in range(2, 4):  # r will be 2, or 3
    for feature_set in combinations(all_features, r):
        print(f"\nEvaluating Features: {feature_set}")
        accuracy = evaluate_features(feature_set)
        
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_features = feature_set

# Print the best attributes
print("\nBest Attributes:")
print(f"Features: {best_features}")
print(f"Best Accuracy: {best_accuracy * 100:.2f}%")
