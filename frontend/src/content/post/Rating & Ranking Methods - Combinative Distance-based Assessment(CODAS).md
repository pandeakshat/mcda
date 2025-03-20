---
title: Rating & Ranking Methods - Combinative Distance-based Assessment(CODAS)
description: Rating & Ranking Methods - Combinative Distance-based Assessment(CODAS)
tags:
  - CODAS
pubDate: 2025-01-07
draft: false
---
# Combinative Distance-based Assessment (CODAS)

## Overview
The **Combinative Distance-based Assessment (CODAS)** is a multi-criteria decision analysis method that evaluates alternatives based on their distances from a negative ideal solution using dual distance measures (Euclidean and Manhattan). CODAS is designed to be robust, particularly when dealing with complex datasets that contain noise or outliers.

## Inputs
- **Alternatives:** Entities such as firms, banks, cities, or countries.
- **Criteria:** Measures used for evaluating alternatives (financial, sustainability, economic).
- **Attributes:** Values linked to each criterion, categorized as:
  - **Beneficial (maximize)**
  - **Non-beneficial (minimize)**

## Steps

### Step 1: Criteria Weighting
Assign a single set of weights reflecting criteria importance, ensuring the total weights equal 1.

### Step 2: Data Normalization
Normalize alternative performances:
- **Beneficial criteria:** Divide each score by the highest criterion score.
- **Non-beneficial criteria:** Divide the lowest criterion score by each alternative’s score.

### Step 3: Compute Negative Ideal Solution
Create a negative ideal benchmark:
- Use the lowest normalized values for beneficial criteria and highest normalized values for non-beneficial criteria.

### Step 4: Compute CODAS Scores
Calculate distances to the negative ideal solution using two metrics:
- **Euclidean distance:** Measures overall distance.
- **Manhattan (Taxicab) distance:** Highlights deviations in specific criteria.

CODAS Score calculation combines both distances and incorporates a threshold function to address minor differences:
- Higher CODAS scores indicate greater distance from the negative ideal solution, thus better alternatives.

### Step 5: Ranking Alternatives
Rank alternatives from best to worst based on descending CODAS scores.

## Implementation Decisions
- **Normalization Methods:** Vector Normalization, Linear Scale Transformation (Max-Min, Max, Sum), Non-monotonic Normalization.
- **Weighting Schemes:** Equal weights, Centroid weights, Regression-based weights, Analytic Hierarchy Process (AHP), SMART, SMARTER, SWING.
- **Distance Threshold (τ):** Set typically between 0.01 and 0.05 to ensure robust rankings.

## Key Features of CODAS
- **Dual Distance Measures:** Uses Euclidean for overall evaluation and Manhattan for specific criteria deviations.
- **Threshold Function:** Enhances ranking robustness by reducing sensitivity to minor differences.
- **Criteria Importance:** Weights explicitly reflect criteria priorities.
- **Outlier Robustness:** Less sensitive to extreme values compared to simpler methods.

## Advantages of CODAS
- **Balanced Evaluation:** Combines overall and criterion-specific assessments.
- **Robust Rankings:** Minimizes rank instability from minor variations in data.
- **Complex Problems:** Suitable for evaluating multi-dimensional and conflicting criteria.
- **Flexibility:** Capable of handling quantitative and qualitative criteria.

## Disadvantages of CODAS
- **Weight Dependency:** Results sensitive to subjective criteria weights.
- **Normalization Impact:** Choice of normalization method can affect rankings.
- **Computational Complexity:** Requires dual-distance calculations, making it computationally heavier than simpler methods.
- **Additivity Assumption:** Assumes linear trade-offs among criteria.

## CODAS vs. Other MCDA Methods

| Feature            | CODAS                               | ARAS                               | OCRA                                   |
|--------------------|-------------------------------------|------------------------------------|----------------------------------------|
| **Core Concept**   | Distance-based (Euclidean & Manhattan)| Utility-based                      | Aggregation-based                      |
| **Normalization**  | Explicit, criterion-specific        | Ratio-based                        | Criterion-type specific normalization  |
| **Criteria Treatment** | Combined, unified weighting      | Combined, unified weighting        | Separate weighting for criteria types  |
| **Trade-offs**     | Robust linear, additive             | Simple linear, additive            | Linear additive, separately aggregated |
| **Sensitivity**    | High robustness to minor variations | Moderate sensitivity               | Moderate sensitivity                   |

## When to Use CODAS
- Complex multi-criteria decision-making scenarios
- Data with significant noise or outliers
- Situations needing robust distance-based evaluation
- Cases where small differences in criteria values are critical

## Conclusion
CODAS is a robust, distance-based MCDA method that excels in complex, noisy datasets. Its dual-distance approach combined with threshold adjustments makes it highly reliable and suitable for sophisticated decision-making contexts.

## References
- Ghorabaee, K. M., Zavadskas, E.K., Turskis, Z., and Antucheviciene, J. (2016). A new combinative distance-based assessment (CODAS) method for multi-criteria decision-making, Economic Computation and Economic Cybernetics Studies and Research, 3(50), 24-44.

