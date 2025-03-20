---
title: Rating & Ranking Methods - The Weighted Sum Model (WSM)
description: Rating & Ranking Methods - The Weighted Sum Model (WSM)
tags:
  - MCDA
  - WSM
pubDate: 2025-01-02
draft: false
---
# Weighted Sum Model (WSM)

## Overview
The **Weighted Sum Model (WSM)** is a multi-criteria decision analysis method used for rating and ranking multiple alternatives based on specified criteria.

## Inputs
- **Alternatives:** Entities such as firms, banks, cities, or countries.
- **Criteria:** Measures used to evaluate alternatives (e.g., financial, sustainability, economic).
- **Attributes:** Values linked to each criterion, categorized as:
  - **Beneficial (maximize)**
  - **Non-beneficial (minimize)**

## Steps

### Step 1: Criteria Weighting
Assign weights reflecting criteria importance, ensuring total weights equal 1.

### Step 2: Data Normalization
Normalize performances of alternatives:

- **Beneficial criteria:** Divide each criterion score by the highest score.
- **Non-beneficial criteria:** Subtract each criterion score divided by the highest score from 1.

### Step 3: Calculate WSM Scores
Calculate the WSM score for each alternative by summing the products of criteria weights and normalized scores. Higher scores indicate better alternatives.

### Step 4: Ranking Alternatives
Rank alternatives from best to worst based on their WSM scores.

## Implementation Decisions
- **Normalization Methods:** Vector Normalization, Linear Scale (Max-Min, Max, Sum), Non-monotonic Normalization.
- **Weighting Schemes:** Equal weights, Centroid weights, Regression-based weights, Analytic Hierarchy Process (AHP).

## Aim of Data Normalization
Normalization ensures comparability across criteria, preventing biases from differences in measurement units.

## Notes on Data Normalization
- Normalization method selection depends on data characteristics and decision-maker preferences.
- Some methods may alter data interpretation, affecting outcomes.

## Criticisms of WSM

### Assumptions and Simplifications
- **Additivity & Compensatory Nature:** Assumes weaknesses in one criterion can always be offset by strengths in another.
- **Linear Preferences:** Assumes linear relationships between criteria scores and overall value.

### Sensitivity and Robustness
- **Weight Sensitivity:** Small changes in weights significantly impact rankings.
- **Outlier Sensitivity:** Extreme values can disproportionately affect outcomes.

### Interdependencies and Scaling Issues
- **Ignoring Criteria Interdependencies:** Treats criteria independently, ignoring interactions.
- **Normalization Sensitivity:** Different normalization methods can lead to different rankings.

### Handling Complexity and Qualitative Data
- **Uncertainty Handling:** Does not effectively handle uncertainty or incomplete data.
- **Qualitative Data Limitations:** Requires quantitative data, limiting effectiveness with qualitative inputs.
- **Oversimplification:** Insufficient for complex or dynamic scenarios.

### Stability and Scalability
- **Rank Reversal:** Rankings may change if alternatives are added or removed.
- **Limited Scalability:** Less practical for a large number of alternatives or criteria.

## Conclusion
WSM is straightforward and efficient for simple scenarios but limited in complexity, uncertainty, or qualitative assessments, requiring alternative methods for robust decision-making.