# POLYNOMIAL_AI
Assignment submission

## Problem
The dataset we use includes cell phone and accessory product reviews such as ratings, text, helpfulness votes. This dataset was obtained from http://jmcauley.ucsd.edu/data/amazon/. The original data was in json format. The json was imported and decoded for further processing. 
The goal is to develop a model to predict whether the reviews could be classified into specific classes namely "Positive" reviews, "Negative" reviews and "Neutral" reviews.

## Approach
1. Data Preprocessing : Here we perform data cleaning and extract the data required to solve the problem. We create a new column named "Sentiment" using the ratings provided by the users. The new column would now be the dependent variable for the model to predict. The text reviews would be the independent variable.

2. Model training and Validation : We use a basic Machine Learning algorithm like SVM with some hyperparameters tuned.

3. Making predictions in real time by running the driver.py file

## Model Architecture
Deep learning based sequential models could produce better results but due to time and computational constraints, we implement a SVM classifier with hyperparameters like C=1.0 and gamma = 1.0. We try a set of other ensemble classifiers like Xgboost but SVM seems to be the better performer. Hence we choose to store the weights of the SVM model for making further predictions.

## Model Performance

Accuracy : 84%

Macro Accuracy : 70%

Weighted Accuracy : 83%

Average Precision : 73%
