# 🩺 Fetal Health Prediction

A Machine Learning based web application for predicting fetal health conditions using Cardiotocography (CTG) data.

The system analyzes 21 CTG features and classifies fetal health into three categories:

- Normal
- Suspect
- Pathological

The project also provides model performance visualizations and downloadable prediction reports.

---

# 📌 Project Pipeline

```text
                    ┌─────────────────────┐
                    │     CTG Dataset     │
                    │  Fetal Health Data   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Data Preprocessing│
                    │                     │
                    │ • Cleaning          │
                    │ • Feature Selection │
                    │ • Scaling           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Model Training    │
                    │                     │
                    │ • ML Algorithms     │
                    │ • Training Data     │
                    │ • Testing Data      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Model Evaluation    │
                    │                     │
                    │ • Accuracy          │
                    │ • Precision         │
                    │ • Recall            │
                    │ • F1-Score          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Trained Model     │
                    │ fetal_health_model  │
                    └──────────┬──────────┘
                               │
                               ▼
              ┌────────────────────────────────┐
              │       Flask Web Application     │
              └───────────────┬────────────────┘
                              │
                 ┌────────────┴─────────────┐
                 │                          │
                 ▼                          ▼
        ┌──────────────────┐       ┌──────────────────┐
        │  CTG Input Form  │       │ Model             │
        │                  │       │ Visualizations    │
        │  21 Features     │       │                  │
        └────────┬─────────┘       └──────────────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ ML Prediction    │
        └────────┬─────────┘
                 │
                 ▼
       ┌───────────────────────┐
       │ Fetal Health Result   │
       │                       │
       │ Normal                │
       │ Suspect               │
       │ Pathological          │
       └──────────┬────────────┘
                  │
          ┌───────┴────────┐
          │                │
          ▼                ▼
 ┌────────────────┐  ┌──────────────────┐
 │ Probability &  │  │ Download Report  │
 │ Confidence     │  │                  │
 └────────────────┘  │ PDF Report       │
                     └──────────────────┘
