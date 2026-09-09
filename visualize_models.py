import matplotlib.pyplot as plt

models = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest",
    "KNN",
    "SVM",
    "Naive Bayes",
    "XGBoost"
]

accuracies = [
    89,
    93,
    95,
    89,
    90,
    71,
    96
]

plt.figure(figsize=(10, 6))

plt.bar(models, accuracies)

plt.xlabel("Machine Learning Model")
plt.ylabel("Accuracy (%)")
plt.title("Fetal Health Model Accuracy Comparison")

plt.ylim(0, 100)

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "static/visualizations/model_accuracy.png",
    dpi=300
)

plt.show()

print("Model accuracy visualization created successfully.")