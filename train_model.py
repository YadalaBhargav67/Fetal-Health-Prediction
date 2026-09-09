import pandas as pd

# ==========================================
# 1. Load Dataset
# ==========================================

data = pd.read_csv("data/fetal_health.csv")

# ==========================================
# 2. Basic Dataset Information
# ==========================================

print("Dataset Shape:", data.shape)

print("\nMissing Values:")
print(data.isnull().sum())

print("\nFetal Health Distribution:")
print(data["fetal_health"].value_counts())

print("\nData Types:")
print(data.dtypes)

# # ==========================================
# # 3. Check Duplicates
# # ==========================================

print("\nDuplicate Rows:", data.duplicated().sum())

# # ==========================================
# # 4. Remove Duplicates
# # ==========================================

data = data.drop_duplicates()

print("Shape after removing duplicates:", data.shape)

# ==========================================
# 5. Separate Features and Target
# ==========================================

X = data.drop("fetal_health", axis=1)
y = data["fetal_health"]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

from sklearn.model_selection import train_test_split

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Features:", X_train.shape)
print("Testing Features:", X_test.shape)
print("Training Target:", y_train.shape)
print("Testing Target:", y_test.shape)

from sklearn.preprocessing import StandardScaler

# Feature Scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nScaled Training Features:", X_train_scaled.shape)
print("Scaled Testing Features:", X_test_scaled.shape)

# ==========================================
# 6. Train Logistic Regression
# ==========================================

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nLogistic Regression Accuracy:", accuracy)

# Detailed evaluation
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ==========================================
# 8. Train Decision Tree
# ==========================================

from sklearn.tree import DecisionTreeClassifier

decision_tree = DecisionTreeClassifier(random_state=42)

# Train
decision_tree.fit(X_train, y_train)

# Predict
y_pred_dt = decision_tree.predict(X_test)

# Accuracy
accuracy_dt = accuracy_score(y_test, y_pred_dt)

print("\nDecision Tree Accuracy:", accuracy_dt)

# ==========================================
# 9. Train Random Forest
# ==========================================

from sklearn.ensemble import RandomForestClassifier

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train
random_forest.fit(X_train, y_train)

# Predict
y_pred_rf = random_forest.predict(X_test)

# Accuracy
accuracy_rf = accuracy_score(y_test, y_pred_rf)

print("\nRandom Forest Accuracy:", accuracy_rf)
# ==========================================
# 10. Train K-Nearest Neighbors
# ==========================================

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)

# Train
knn.fit(X_train_scaled, y_train)

# Predict
y_pred_knn = knn.predict(X_test_scaled)

# Accuracy
accuracy_knn = accuracy_score(y_test, y_pred_knn)

print("\nKNN Accuracy:", accuracy_knn)

# ==========================================
# 11. Train Support Vector Machine (SVM)
# ==========================================

from sklearn.svm import SVC

svm = SVC(kernel="rbf", random_state=42)

# Train
svm.fit(X_train_scaled, y_train)

# Predict
y_pred_svm = svm.predict(X_test_scaled)

# Accuracy
accuracy_svm = accuracy_score(y_test, y_pred_svm)

print("\nSVM Accuracy:", accuracy_svm)

# ==========================================
# 12. Train Naive Bayes
# ==========================================

from sklearn.naive_bayes import GaussianNB

naive_bayes = GaussianNB()

# Train
naive_bayes.fit(X_train_scaled, y_train)

# Predict
y_pred_nb = naive_bayes.predict(X_test_scaled)

# Accuracy
accuracy_nb = accuracy_score(y_test, y_pred_nb)

print("\nNaive Bayes Accuracy:", accuracy_nb)

# ==========================================
# 13. Train XGBoost
# ==========================================

from xgboost import XGBClassifier

xgb_model = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    random_state=42,
    eval_metric="mlogloss"
)

# Train
xgb_model.fit(X_train, y_train - 1)

# Predict
y_pred_xgb = xgb_model.predict(X_test) + 1

# Accuracy
accuracy_xgb = accuracy_score(y_test, y_pred_xgb)

print("\nXGBoost Accuracy:", accuracy_xgb)

# ==========================================
# 14. Compare Model Accuracy
# ==========================================

models = {
    "Logistic Regression": accuracy,
    "Decision Tree": accuracy_dt,
    "Random Forest": accuracy_rf,
    "KNN": accuracy_knn,
    "SVM": accuracy_svm,
    "Naive Bayes": accuracy_nb,
    "XGBoost": accuracy_xgb
}

print("\n========== MODEL COMPARISON ==========")

for model_name, model_accuracy in models.items():
    print(f"{model_name}: {model_accuracy:.4f}")

# ==========================================
# 15. Detailed Model Evaluation
# ==========================================

from sklearn.metrics import classification_report

predictions = {
    "Logistic Regression": y_pred,
    "Decision Tree": y_pred_dt,
    "Random Forest": y_pred_rf,
    "KNN": y_pred_knn,
    "SVM": y_pred_svm,
    "Naive Bayes": y_pred_nb,
    "XGBoost": y_pred_xgb
}

print("\n========== DETAILED MODEL EVALUATION ==========")

for model_name, predictions_value in predictions.items():
    print(f"\n--- {model_name} ---")
    print(classification_report(y_test, predictions_value))

# ==========================================
# 16. XGBoost Hyperparameter Tuning
# ==========================================

from sklearn.model_selection import GridSearchCV

xgb_tuning = XGBClassifier(
    random_state=42,
    eval_metric="mlogloss"
)

param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [3, 5, 7],
    "learning_rate": [0.05, 0.1]
}

grid_search = GridSearchCV(
    estimator=xgb_tuning,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid_search.fit(X_train, y_train - 1)

print("\nBest XGBoost Parameters:")
print(grid_search.best_params_)

print("\nBest Cross-Validation Accuracy:")
print(grid_search.best_score_)

# ==========================================
# 17. Final XGBoost Model
# ==========================================

best_xgb = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    random_state=42,
    eval_metric="mlogloss"
)

# Train final model
best_xgb.fit(X_train, y_train - 1)

# Predict on unseen test data
final_pred = best_xgb.predict(X_test) + 1

# Final accuracy
final_accuracy = accuracy_score(y_test, final_pred)

print("\n========== FINAL XGBOOST RESULT ==========")
print("Final Test Accuracy:", final_accuracy)

print("\nFinal Classification Report:")
print(classification_report(y_test, final_pred))

print("\nFinal Confusion Matrix:")
print(confusion_matrix(y_test, final_pred))

import joblib

# Save final model
joblib.dump(best_xgb, "fetal_health_model.pkl")

# Save scaler
joblib.dump(scaler, "scaler.pkl")

print("\nModel and scaler saved successfully!")

