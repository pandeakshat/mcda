---
title: Data Normalisation Approaches & Methods in MCDA
description: Data Normalisation Approaches & Methods in MCDA
tags:
  - CMDA
  - Normalization
pubDate: 2025-01-15
draft: false
---

# Data Normalization Methods in Multi-Criteria Decision Analysis (MCDA)

## Overview
Data normalization is a critical step in MCDA, ensuring comparability among criteria with different units or scales. It eliminates biases from measurement disparities and enhances the reliability and fairness of decision-making processes.

## Primary Purposes of Normalization
- **Ensuring Comparability:** Converts criteria to a common scale.
- **Handling Value Range Differences:** Prevents dominance by criteria with larger values.
- **Managing Beneficial and Non-Beneficial Criteria:** Appropriately scales maximization and minimization criteria.
- **Improving Numerical Stability:** Avoids computational issues with very large or small numbers.
- **Facilitating Fair Weight Assignment:** Ensures weights reflect criteria importance accurately.

## Types of Measurement Scales in MCDA
- **Nominal Scale:** Categorical, qualitative data (e.g., product types).
- **Ordinal Scale:** Ordered data without equal intervals (e.g., satisfaction levels).
- **Interval Scale:** Numeric, equal intervals, no true zero (e.g., temperature).
- **Ratio Scale:** Numeric with absolute zero (e.g., cost, efficiency).
- **Absolute Scale:** Count data (e.g., number of customers).
- **Log-Interval Scale:** Exponential growth data (e.g., Richter scale).
- **Fuzzy Scale:** Linguistic, fuzzy variables (e.g., qualitative ratings).
- **Composite Scale:** Hybrid combinations of multiple scales.

## Normalization Approaches
- **Homogeneous (Single Treatment):** Same normalization applied across all criteria.
- **Heterogeneous (Mixed Treatment):** Different normalization methods applied per criterion based on characteristics.

## Types of Transformations

### Linear Transformations
- **Min-Max Normalization:** Scales data to [0,1]; used in OCRA, VIKOR.
- **Max Normalization:** Scales beneficial criteria to [0,1], adjusts non-beneficial accordingly; used in WPM, CODAS.
- **Vector (Euclidean, L-2 Norm) Normalization:** Maintains proportionality, scales criteria to [0,1]; used in TOPSIS, DRPM.
- **Sum-Based Normalization:** Criteria scaled proportionally based on sum totals; used in COPRAS.

### Non-Linear Transformations
- **Logarithmic Normalization:** Compresses skewed data distributions.
- **Z-Score Normalization:** Standardizes data to handle outliers.
- **Power Transformations:** Adjust distributions for symmetry (e.g., Box-Cox).
- **Fuzzy-Based Normalization:** Suitable for handling qualitative or uncertain data.
- **Stepwise Transformations:** Categorize continuous data based on thresholds.

## Desirable Properties of Normalization Methods
- **Unit Invariance:** Not dependent on measurement units.
- **Scale Invariance:** Stable under proportional scaling of data.
- **Preservation of Ordering:** Maintains relative ranking of alternatives.
- **Range-Boundedness:** Keeps data within defined bounds, typically [0,1].
- **Proportionality:** Preserves relative differences between values.
- **Robustness to Outliers:** Minimally affected by extreme values.
- **Additive & Multiplicative Consistency:** Rankings stable under additive/multiplicative transformations.

## Choosing the Right Normalization Method

| Scenario | Recommended Transformations | Example Methods |
|----------|-----------------------------|-----------------|
| Similar distributions, different units | Min-Max, Vector, Sum-Based | OCRA, WSM, WPM, WASPAS, TOPSIS, DRPM |
| Extreme values present (outliers) | Logarithmic, Z-Score | Statistical MCDA, Robust Models |
| Emphasize large values | Exponential, Softmax | Growth-oriented models |
| Skewed data distributions | Logarithmic, Power-Based | Environmental MCDA, Entropy-Based MCDA |
| Proportional conversion needed | Sum-Based (Ratio-Based) | COPRAS, Proportional MCDA |
| Uncertainty and fuzziness | Fuzzy-Based Normalization | Fuzzy TOPSIS, Fuzzy VIKOR |

## Conclusion
Normalization is crucial in MCDA to achieve accurate, fair, and comparable evaluations across diverse criteria. Selecting appropriate normalization techniques depends significantly on the context, data properties, and decision-maker priorities, influencing the outcomes and effectiveness of decision-making models.

