// Model Accuracy Comparison

new Chart(document.getElementById("accuracyChart"), {
    type: "bar",

    data: {
        labels: [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "KNN",
            "SVM",
            "Naive Bayes",
            "XGBoost"
        ],

        datasets: [{
            label: "Accuracy",
            data: [
                0.89,
                0.93,
                0.95,
                0.89,
                0.90,
                0.71,
                0.96
            ]
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,

        scales: {
            y: {
                beginAtZero: true,
                max: 1
            }
        }
    }
});


// Precision, Recall and F1-Score

new Chart(document.getElementById("metricsChart"), {
    type: "bar",

    data: {
        labels: [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "KNN",
            "SVM",
            "Naive Bayes",
            "XGBoost"
        ],

        datasets: [
            {
                label: "Precision",
                data: [
                    0.82,
                    0.90,
                    0.95,
                    0.84,
                    0.87,
                    0.64,
                    0.96
                ]
            },
            {
                label: "Recall",
                data: [
                    0.76,
                    0.87,
                    0.88,
                    0.72,
                    0.77,
                    0.73,
                    0.90
                ]
            },
            {
                label: "F1 Score",
                data: [
                    0.79,
                    0.88,
                    0.91,
                    0.77,
                    0.81,
                    0.63,
                    0.93
                ]
            }
        ]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,

        scales: {
            y: {
                beginAtZero: true,
                max: 1
            }
        }
    }
});


// XGBoost Class Performance

new Chart(document.getElementById("xgboostChart"), {
    type: "bar",

    data: {
        labels: [
            "Normal",
            "Suspect",
            "Pathological"
        ],

        datasets: [
            {
                label: "Precision",
                data: [
                    0.96,
                    0.98,
                    1.00
                ]
            },
            {
                label: "Recall",
                data: [
                    1.00,
                    0.78,
                    0.94
                ]
            },
            {
                label: "F1 Score",
                data: [
                    0.98,
                    0.87,
                    0.97
                ]
            }
        ]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,

        scales: {
            y: {
                beginAtZero: true,
                max: 1
            }
        }
    }
});