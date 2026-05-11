# 📊 AI Model Evaluation Metrics

## Overview

Proper evaluation is crucial for understanding model performance. This guide covers metrics for classification, regression, clustering, and ranking tasks.

## Classification Metrics

### Confusion Matrix

```
                Predicted
               Pos    Neg
Actual  Pos   TP     FN
        Neg   FP     TN

TP (True Positive): Correctly predicted positive
TN (True Negative): Correctly predicted negative
FP (False Positive): Incorrectly predicted positive
FN (False Negative): Incorrectly predicted negative
```

### Accuracy

**Formula**: (TP + TN) / (TP + TN + FP + FN)

**Use**: Overall correctness, balanced datasets

**Range**: 0 to 1 (higher is better)

**Note**: Can be misleading with imbalanced data

### Precision

**Formula**: TP / (TP + FP)

**Use**: When false positives are costly

**Example**: Email spam filter - minimize false positives

### Recall (Sensitivity)

**Formula**: TP / (TP + FN)

**Use**: When false negatives are costly

**Example**: Disease detection - catch all cases

### F1-Score

**Formula**: 2 * (Precision * Recall) / (Precision + Recall)

**Use**: Balanced metric between precision and recall

**Range**: 0 to 1 (higher is better)

### Specificity

**Formula**: TN / (TN + FP)

**Use**: True negative rate

**Example**: Medical testing - true negative rate

### ROC-AUC Curve

**What**: Receiver Operating Characteristic - Area Under Curve

**Range**: 0 to 1 (higher is better)
- 0.5 = random classifier
- 1.0 = perfect classifier
- 0.7-0.8 = acceptable
- 0.8-0.9 = excellent
- >0.9 = outstanding

### Precision-Recall Curve

**Use**: When classes are imbalanced

**Advantage**: More informative than ROC-AUC for imbalanced data

## Regression Metrics

### Mean Absolute Error (MAE)

**Formula**: (1/n) * Σ|y_true - y_pred|

**Use**: Average absolute difference

**Advantage**: Interpretable, robust to outliers

### Mean Squared Error (MSE)

**Formula**: (1/n) * Σ(y_true - y_pred)²

**Use**: Penalizes large errors

**Note**: Not in original units

### Root Mean Squared Error (RMSE)

**Formula**: √MSE

**Use**: Same units as target variable

**Advantage**: More interpretable than MSE

### R-Squared (R²)

**Formula**: 1 - (SS_res / SS_tot)

**Range**: -∞ to 1 (higher is better)
- 1.0 = perfect fit
- 0.0 = mean baseline
- <0 = worse than mean

### Mean Absolute Percentage Error (MAPE)

**Formula**: (1/n) * Σ|((y_true - y_pred) / y_true)| * 100

**Use**: Percentage error

**Caution**: Undefined when y_true = 0

## Clustering Metrics

### Silhouette Score

**Range**: -1 to 1
- Close to 1: Well clustered
- Close to 0: Overlapping
- Close to -1: Wrong cluster

**Formula**: (b - a) / max(a, b)
- a = mean distance to points in same cluster
- b = mean distance to nearest cluster

### Davies-Bouldin Index

**Range**: 0 to ∞ (lower is better)

**Use**: Cluster separation and compactness

### Calinski-Harabasz Index

**Range**: 0 to ∞ (higher is better)

**Use**: Ratio of between-cluster to within-cluster dispersion

## Cross-Validation

### K-Fold Cross-Validation

**Process**:
1. Split data into k folds
2. Train on k-1 folds
3. Test on 1 fold
4. Repeat k times
5. Average results

**Common**: k = 5 or 10

**Advantage**: Uses all data for both training and validation

### Stratified K-Fold

**Use**: Imbalanced classification

**Benefit**: Maintains class distribution in each fold

### Time Series Split

**Use**: Time series data

**Process**: Forward chaining - train on past, test on future

## Hyperparameter Tuning

### Grid Search

**Method**: Test all combinations of parameters

**Advantage**: Exhaustive search

**Disadvantage**: Computationally expensive

### Random Search

**Method**: Random sample of parameter combinations

**Advantage**: Often finds good parameters faster

**Advantage**: More computationally efficient

### Bayesian Optimization

**Method**: Use probabilistic model to guide search

**Advantage**: More efficient than grid/random search

## Model Comparison

### Learning Curves

**Plot**: Training and validation loss vs. training samples

**Diagnose**:
- **High bias** (underfitting): Both curves high and flat
- **High variance** (overfitting): Gap between curves
- **Good**: Both curves converging and low

### Validation Curves

**Plot**: Training and validation score vs. hyperparameter

**Use**: Understand hyperparameter effect

## Best Practices

### 1. Choose Right Metrics
- Classification: Accuracy, Precision, Recall, F1, AUC
- Regression: MAE, RMSE, R²
- Clustering: Silhouette, Davies-Bouldin

### 2. Always Use Validation Set
- Never evaluate on training data
- Use proper train/val/test split
- Use cross-validation for small datasets

### 3. Consider Class Imbalance
- Don't use accuracy alone
- Use precision, recall, F1
- Use stratified sampling
- Consider SMOTE or class weights

### 4. Document Everything
- Metric definitions
- Thresholds used
- Cross-validation strategy
- Hyperparameter values

### 5. Baseline Comparison
- Compare to simple baseline
- Compare to state-of-the-art
- Document why you chose metrics

## Common Pitfalls

❌ **Data Leakage**: Evaluating on training data

❌ **Wrong Metric**: Using accuracy for imbalanced data

❌ **No Cross-Validation**: Single train/test split

❌ **Ignoring Baselines**: Not comparing to simple models

❌ **Cherry-picking**: Selecting metrics that look good

✅ **Best Practice**: Use multiple metrics, proper validation, and compare baselines

---

Last Updated: 2026-05-10
