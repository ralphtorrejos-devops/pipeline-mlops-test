import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load data
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

# Define feature columns explicitly
feature_columns = [
    'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
]

# Select features
X_train = train[feature_columns]
y_train = train['Outcome']
X_test = test[feature_columns]
y_test = test['Outcome']

print(f"Training with {len(feature_columns)} features: {feature_columns}")
print(f"Training data shape: {X_train.shape}")

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model.pkl')
print("Model saved to model.pkl")

# Evaluate
y_pred = model.predict(X_test)
print("\nModel Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Verify the model was saved correctly
loaded_model = joblib.load('model.pkl')
print(f"\nLoaded model expects {loaded_model.n_features_in_} features")