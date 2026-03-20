# Project 04: House Price Prediction

## Overview
Build a regression model to predict residential property prices using the Ames Housing Dataset.

## Dataset
[House Prices: Advanced Regression Techniques – Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)

## Project Phases

### Phase 1: EDA
- Target variable analysis (log transform justified?)
- Feature correlation analysis
- Handling missing values (80+ features, many with missing data)

### Phase 2: Feature Engineering
- Create new features (total sq ft, house age, etc.)
- Handle categorical features (neighborhood, quality ratings)
- Apply appropriate transformations

### Phase 3: Modeling
Compare:
- Linear Regression (baseline)
- Ridge/Lasso
- Random Forest
- XGBoost / LightGBM
- Stacking ensemble

### Phase 4: Deployment
- Save best model with `joblib`
- Build a Streamlit app for price prediction

## Success Metric
Target: RMSE < 0.12 on log-transformed prices (Kaggle leaderboard standard)

## Deliverables
- EDA notebook
- Modeling notebook
- Deployed Streamlit app (optional)
- GitHub repository
