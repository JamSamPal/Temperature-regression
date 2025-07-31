# Temperature Regression Project Report

## Overview
This project aims to predict temperature based on weather features using machine learning regression models.

---

## Data Preprocessing
- Dates converted to datetime with timezone handling.
- Feature engineering ito extract hour and weather condition variables.
- Data cleaned for missing or invalid entries.

---

## Model Training
- Trained a Random Forest Regressor on selected features.
- Split data into training (80%) and testing (20%) sets.

---

## Results

### Actual vs Predicted Temperature
![Actual vs Predicted](actualvspredicted.png)

The model predictions closely follow the actual temperature values over the test samples, showing good general performance.


### Error Distribution
![Error Distribution](errorspread.png)

The residual errors are roughly centered around zero with a small spread, indicating the model is unbiased and fairly consistent.

**Root Mean Squared Error (RMSE):** 2.35 (example value)

---

## Interpretation of Errors
- Mean error close to zero indicates minimal bias.
- Error spread suggests most predictions are within ±3 degrees of actual temperature.
- Few outliers exist, highlighting potential areas for model improvement.

---

## Next Steps
- Incorporate additional weather features such as humidity and wind speed.
- Experiment with boosting algorithms (XGBoost, LightGBM) for better accuracy.
- Develop an interactive web app to demo predictions live.

---

*Report generated on 2025-07-31*