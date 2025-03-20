---
title: Rating & Ranking Methods - Techniques for Order Preference by Similarity to an Ideal Solution (TOPSIS)
description: Rating & Ranking Methods - Techniques for Order Preference by Similarity to an Ideal Solution (TOPSIS)
tags:
  - TOPSIS
  - MCDA
pubDate: 2025-01-10
draft: false
---
# Techniques for Order Preference by Similarity to an Ideal Solution (TOPSIS)

## Overview
The **TOPSIS** method is a multi-criteria decision analysis tool that ranks alternatives based on their closeness to an ideal solution and their distance from a negative ideal solution. It provides a straightforward and balanced approach by evaluating both best and worst-case scenarios.

## Inputs
- **Alternatives:** Entities such as firms, banks, cities, or countries.
- **Criteria:** Measures used to evaluate alternatives (financial, sustainability, economic).
- **Attributes:** Values linked to each criterion, categorized as:
  - **Beneficial (maximize)**
  - **Non-beneficial (minimize)**

## Steps

### Step 1: Criteria Weighting
Assign weights reflecting criteria importance, ensuring total weights equal 1.

### Step 2: Data Normalization
Normalize performances:
- **Beneficial criteria:** Divide each score by the root of the sum of squared scores across all alternatives.
- **Non-beneficial criteria:** Use the same normalization as beneficial, followed by transformation to reflect minimization (1 minus normalized score).

### Step 3: Compute Virtual Benchmarks
Calculate two virtual benchmarks:
- **Positive Ideal Solution (PIS):** Best values of all beneficial criteria and worst values of all non-beneficial criteria.
- **Negative Ideal Solution (NIS):** Worst values of all beneficial criteria and best values of all non-beneficial criteria.

### Step 4: Compute Distances
Calculate distances from each alternative to both PIS and NIS using a distance measure (commonly Euclidean).

### Step 5: Calculate TOPSIS Scores
Compute the relative closeness of each alternative to the ideal solutions:
- Higher scores indicate greater closeness to PIS and greater distance from NIS, signifying better alternatives.

### Step 6: Ranking Alternatives
Rank alternatives from best to worst based on descending TOPSIS scores.

## Implementation Decisions
- **Normalization Methods:** Vector Normalization, Linear Scale Transformation (Max-Min, Max, Sum), Non-monotonic Normalization.
- **Weighting Schemes:** Equal weights, Centroid weights, Regression-based weights, Analytic Hierarchy Process (AHP), SMART, SMARTER, SWING.
- **Distance Metrics:** Euclidean (common), Manhattan, or others.

## Key Features of TOPSIS
- **Distance-Based Evaluation:** Uses Euclidean or other distance measures to evaluate alternatives.
- **Ideal Solutions:** Evaluates alternatives based on proximity to both best and worst scenarios.
- **Explicit Criteria Differentiation:** Clearly distinguishes between beneficial and non-beneficial criteria.

## Advantages of TOPSIS
- **Intuitive Concept:** Clear and understandable logic of choosing the best alternative closest to the ideal and farthest from the worst.
- **Balanced Evaluation:** Considers both best and worst reference points.
- **Comprehensive Handling:** Capable of managing beneficial and non-beneficial criteria explicitly.

## Disadvantages of TOPSIS
- **Criteria Independence Assumption:** Ignores correlations among criteria.
- **Linear Distance Assumption:** Assumes linear relationships, potentially oversimplifying real-world scenarios.
- **Rank Reversal Sensitivity:** Adding or removing alternatives can alter rankings significantly.
- **Qualitative Data Handling:** Requires numerical input data or transformations from qualitative judgments.

## TOPSIS vs. Other MCDA Methods

| Aspect               | TOPSIS                                  | EDAS                                  | VIKOR                                 |
|----------------------|-----------------------------------------|---------------------------------------|---------------------------------------|
| **Core Concept**     | Distance to ideal and negative solutions | Distance to average solution          | Compromise solutions                  |
| **Normalization**    | Required                                | Required                              | Required                              |
| **Sensitivity**      | Sensitive to extremes                   | Robust to outliers                    | Focused on compromise                 |
| **Criteria Handling**| Explicit beneficial/non-beneficial      | Explicit beneficial/non-beneficial    | Explicit beneficial/non-beneficial    |

## When to Use TOPSIS
- Problems needing intuitive and balanced distance-based evaluations.
- Scenarios where clarity in best and worst alternatives is helpful.
- Decisions involving both beneficial and non-beneficial criteria explicitly.

## When NOT to Use TOPSIS
- Situations with highly interdependent or correlated criteria.
- Decision problems involving primarily qualitative data without clear numerical conversion.
- Scenarios highly sensitive to rank reversals.

## Conclusion
TOPSIS remains a popular and intuitive decision-making tool, effective for various applications where balanced, distance-based evaluations are needed. Its strengths outweigh its limitations, especially when used with careful consideration of its assumptions and potential adjustments.

## References
- Hwang, C. L., & Yoon, K. P. (1981). Multiple attribute decision making: Methods and applications. New York: Springer-Verlag.

