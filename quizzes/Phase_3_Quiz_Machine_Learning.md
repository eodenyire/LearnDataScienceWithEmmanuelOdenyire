# Phase 3 Quiz: Machine Learning

**Instructions**: 30 questions. Open book.

---

## Section A: Concepts (Multiple Choice, 1 point each)

**1.** The bias-variance tradeoff describes:
- a) The tradeoff between model accuracy and speed
- b) The tradeoff between underfitting (high bias) and overfitting (high variance)
- c) The tradeoff between training data size and test performance
- d) The tradeoff between precision and recall

**2.** What does L2 regularization (Ridge) add to the loss function?
- a) Sum of absolute values of coefficients
- b) Sum of squared coefficients
- c) Number of non-zero coefficients
- d) Entropy of the target variable

**3.** In a confusion matrix, False Positive means:
- a) The model predicted negative, actual was negative
- b) The model predicted positive, actual was negative
- c) The model predicted negative, actual was positive
- d) The model predicted positive, actual was positive

**4.** Which metric is most appropriate for imbalanced classification?
- a) Accuracy
- b) F1-Score / ROC-AUC
- c) MSE
- d) R²

**5.** Random Forest reduces overfitting compared to a single Decision Tree by:
- a) Using deeper trees
- b) Averaging predictions from many diverse trees (bagging + feature randomness)
- c) Using a single decision boundary
- d) Removing features with low importance

---

## Section B: Algorithms (3 points each)

**6.** Explain how K-Means clustering works. What is its main limitation?

**7.** What is the kernel trick in SVMs and why is it useful?

**8.** Describe gradient descent. What is the role of the learning rate?

**9.** How does a Decision Tree decide which feature to split on?

**10.** Compare precision and recall. When would you prioritize one over the other?

---

## Section C: Practical (5 points each)

**11.** Write a complete sklearn pipeline that: imputes missing values, encodes categoricals, scales numericals, and fits a RandomForestClassifier. Include GridSearchCV for tuning.

**12.** You trained a model with 99% training accuracy and 62% test accuracy. What is happening and how would you fix it?

---

*Total: 30 points*
