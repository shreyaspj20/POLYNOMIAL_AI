# POLYNOMIAL_AI
Assignment submission

## Problem
The dataset we use includes cell phone and accessory product reviews such as ratings, text, helpfulness votes. This dataset was obtained from http://jmcauley.ucsd.edu/data/amazon/. The original data was in json format. The json was imported and decoded for further processing. 
The goal is to develop a model to predict whether the reviews could be classified into specific classes namely "Positive" reviews, "Negative" reviews and "Neutral" reviews.

## Approach
1. Data Preprocessing.
2. Model training and Validation
3. Making predictions in real time.

## Model Architecture
Deep learning based sequential models could produce better results but due to time and computational constraints, we implement a SVM classifier with hyperparameters like C=1.0 and gamma = 1.0. We try a set of other ensemble classifiers like Xgboost and RandomForests but SVM seems to be the better performer. Hence we choose to store the weights of the SVM model for making further predictions.

## Model Performance

Accuracy :
Macro Accuracy :
Micro Accuracy :
Average Precision :
