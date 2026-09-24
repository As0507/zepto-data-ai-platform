# Analytics Pipeline

## Steps
1. Load Titanic dataset once via `sns.load_dataset("titanic")` → saved as `titanic.csv`.
2. Profiling: missing values %, threshold rule (<5% drop, 5–30% impute, >30% drop/encode).
3. EDA: histograms, boxplots, outlier counts, skewness check, survival breakdowns, correlation heatmap.
4. Modeling: stratified train/test split, preprocessing pipeline (imputer + encoder + scaler).
5. Classifiers: Logistic Regression, Decision Tree (visualized), Random Forest (with GridSearchCV + OOB score).
6. Evaluation: confusion matrix, accuracy, precision, recall, F1, ROC/AUC.
7. Imbalance handling: baseline vs class_weight vs SMOTE.
8. Regression side‑task: predict `fare` with linear regression, report MAE, RMSE, R², Adjusted R².
9. Comparison table + final recommendation.
10. Saved pipeline: `best_pipeline.joblib`.

## Design Decisions
- Stratified split to preserve class balance.
- Median imputation for age, mode for categorical.
- Random Forest chosen as final model (best balance of metrics).
