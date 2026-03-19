# Phase 3 CAT: House Price Prediction

## Objective
Build and evaluate a machine learning model to predict house prices.

## Dataset
Use the [Ames Housing Dataset](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data) or a local equivalent.

## Tasks

### Task 1: Data Exploration (20 points)
- Explore the target variable (`SalePrice`) distribution
- Identify the top 10 features correlated with price
- Visualize at least 5 key relationships

### Task 2: Preprocessing Pipeline (25 points)
Build a sklearn `Pipeline` that handles:
- Missing value imputation (separate strategies for numerical and categorical)
- Categorical encoding (OneHot or Target Encoding)
- Numerical scaling
- Feature selection

### Task 3: Model Development (30 points)
Train and compare at least 4 models:
1. Linear Regression (baseline)
2. Ridge/Lasso Regression
3. Random Forest
4. Gradient Boosting (XGBoost or LightGBM)

Use 5-fold cross-validation. Report RMSE and R² for all models.

### Task 4: Hyperparameter Tuning (15 points)
Tune your best model using `GridSearchCV` or `RandomizedSearchCV`.
Document the search space and best parameters found.

### Task 5: Model Interpretation (10 points)
- Feature importance plot for your best model
- 3 key insights: which features matter most and why?

## Submission
- Jupyter Notebook (`.ipynb`)
- GitHub repository with clean code
- Final model test RMSE (evaluated on 20% holdout set)

## Grading
| Task | Points |
|------|--------|
| EDA | 20 |
| Pipeline | 25 |
| Model comparison | 30 |
| Hyperparameter tuning | 15 |
| Interpretation | 10 |
| **Total** | **100** |
