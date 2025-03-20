---
title: Rating & Rankimg Methods - Evaluation based on Distance to Average Solution (EDAS, EDMS)
description: Rating & Rankimg Methods - Evaluation based on Distance to Average Solution (EDAS, EDMS)
tags:
  - MCDA
  - EDAS
  - EDMS
pubDate: 2025-01-09
draft: false
---
# Evaluation based on Distance to Average Solution (EDAS)

## Overview
The **Evaluation based on Distance to Average Solution (EDAS)** method ranks alternatives based on their distances from an average (mean) reference point, emphasizing stability and robustness in multi-criteria decision analysis.

## Inputs
- **Alternatives:** Entities such as firms, banks, cities, or countries.
- **Criteria:** Measures used for evaluating alternatives (financial, sustainability, economic).
- **Attributes:** Values linked to each criterion, categorized as:
  - **Beneficial (maximize)**
  - **Non-beneficial (minimize)**

## Steps

### Step 1: Criteria Weighting
Assign weights reflecting criteria importance, ensuring total weights equal 1.

### Step 2: Reference Point Computation
Compute the average performance across all alternatives for each criterion, establishing a virtual benchmark.

### Step 3: Calculate Positive and Negative Deviations
For each criterion, calculate:
- **Positive Deviations (PDA):** How much an alternative positively deviates from the average.
- **Negative Deviations (NDA):** How much an alternative negatively deviates from the average.

### Step 4: Aggregate Deviations
Calculate overall positive and negative deviations for each alternative using weighted sums of individual deviations.

### Step 5: Normalize Deviations
Normalize aggregated deviations to ensure comparability and scaling between 0 and 1.

### Step 6: Compute EDAS Scores
Combine normalized positive and negative deviations equally to compute an EDAS score:
- Higher EDAS scores indicate better alternatives, reflecting balanced positive and negative deviations.

### Step 7: Ranking Alternatives
Rank alternatives from best to worst based on descending EDAS scores.

## Implementation Decisions
- **Normalization Methods:** Vector Normalization, Linear Scale Transformation (Max-Min, Max, Sum), Non-monotonic Normalization.
- **Weighting Schemes:** Equal weights, Centroid weights, Regression-based weights, Analytic Hierarchy Process (AHP), SMART, SMARTER, SWING.

## Key Features of EDAS
- **Distance-based Evaluation:** Evaluates alternatives based on deviations from the average.
- **Positive/Negative Deviations:** Explicitly considers both beneficial and non-beneficial deviations.
- **Reduced Sensitivity to Outliers:** Less influenced by extreme values compared to methods using ideal solutions.
- **Rank Stability:** Offers stable rankings due to using averages rather than extremes.

## Advantages of EDAS
- **Robustness:** Reduced sensitivity to extreme values and fluctuations.
- **Balanced Evaluation:** Equally considers positive and negative deviations.
- **Computational Efficiency:** Less computational complexity compared to pairwise comparison methods.

## Disadvantages of EDAS
- **Dependence on Mean:** Mean can be skewed by significant outliers.
- **Normalization Sensitivity:** Results may vary with normalization method choices.
- **Weight Dependency:** Subjective weighting significantly influences outcomes.
- **Linear Assumption:** Assumes linear relationships between criteria.

## EDAS vs. Other MCDA Methods

| Aspect               | EDAS                                    | TOPSIS                  | VIKOR                  |
|----------------------|-----------------------------------------|-------------------------|------------------------|
| **Core Concept**     | Distance to average solution             | Distance to ideal/anti-ideal| Compromise solutions    |
| **Normalization**    | Required                                | Required                 | Required                |
| **Sensitivity**      | Less sensitive to outliers              | Sensitive to extremes   | Compromise-oriented     |
| **Criteria Handling**| Beneficial/non-beneficial explicitly    | Beneficial/non-beneficial explicitly| Beneficial/non-beneficial explicitly|

## When to Use EDAS
- Preference for stability and robustness over sensitivity to extremes
- Situations where balanced evaluation of beneficial and non-beneficial criteria is crucial
- Decision-making scenarios prone to data fluctuations and outliers

## When NOT to Use EDAS
- If the problem emphasizes ideal/anti-ideal solutions
- In cases requiring explicit pairwise comparisons
- When dataset contains extreme outliers significantly affecting the mean

## Conclusion
EDAS provides a balanced, stable approach to ranking alternatives based on deviations from average performance. It is particularly useful for multi-criteria scenarios where data stability, robustness, and balanced criteria evaluation are paramount.

## References
- Keshavarz Ghorabaee, M., Zavadskas, E. K., Olfat, L., & Turskis, Z. (2015). Multi-Criteria Inventory Classification Using a New Method of Evaluation Based on Distance from Average Solution (EDAS). Informatica, 26(3), 435–451.