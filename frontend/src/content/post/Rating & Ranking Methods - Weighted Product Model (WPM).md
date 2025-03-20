---
title: Rating & Ranking Methods - Weighted Product Model (WPM)
description: Rating & Ranking Methods - Weighted Product Model (WPM)
tags:
  - WPM
  - MCDA
pubDate: 2025-01-03
draft: false
---

# Weighted Product Model (WPM)

## Overview
The **Weighted Product Model (WPM)** is a multi-criteria decision analysis method for rating and ranking alternatives based on specified criteria. Unlike additive models, WPM multiplies criterion scores, making it suitable for handling non-compensatory decision-making scenarios.

## Inputs
- **Alternatives:** Entities such as firms, banks, cities, or countries.
- **Criteria:** Measures for evaluating alternatives (financial, sustainability, economic).
- **Attributes:** Values linked to each criterion, categorized as:
  - **Beneficial (maximize)**
  - **Non-beneficial (minimize)**

## Steps

### Step 1: Criteria Weighting
Assign weights reflecting criteria importance, ensuring the total weights equal 1.

### Step 2: Data Normalization (Optional)
Normalize alternative performances:

- **Beneficial criteria:** Divide each alternative’s score by the highest score.
- **Non-beneficial criteria:** Divide the lowest score by each alternative’s score.

### Step 3: Calculate WPM Scores
Calculate the WPM score for each alternative by multiplying normalized scores raised to the power of their corresponding weights:

- Multiply each criterion's normalized score, raised to its weight.
- Higher WPM scores indicate better alternatives.

### Step 4: Ranking Alternatives
Rank alternatives from best to worst based on descending WPM scores.

## Implementation Decisions
- **Normalization Methods:** Ratio Normalization (default), Vector Normalization, Linear Scale (Max-Min, Max, Sum).
- **Weighting Schemes:** Equal weights, Centroid weights, Regression-based weights, Analytic Hierarchy Process (AHP).

## Purpose of Data Normalization
- Ensures dimensionless comparison across criteria.
- Standardizes criteria scales to avoid bias from varying measurement units or ranges.
- Preserves the relative importance assigned through weights.

## When is Normalization Needed?
- Heterogeneous units or scales.
- Large variations in magnitudes among criteria.
- Coexistence of beneficial and non-beneficial criteria.
- Presence of outliers that may skew results.

## When Can Normalization Be Skipped?
- Criteria have uniform units or scales.
- Data is pre-normalized (ratios, percentages).
- Minimal variability among criteria scales.

## Risks of Skipping Normalization
- Potential unintended bias from disproportionate influence of certain criteria.
- Misinterpretation of assigned weights.

## Strengths of WPM
- **Non-additive:** Ideal for non-compensatory criteria.
- **Scale Handling:** Reduced sensitivity to scale differences due to multiplicative nature.
- **Relative Evaluation:** Consistent rankings based on relative rather than absolute scores.
- **Simplicity:** Straightforward implementation and computation.

## Weaknesses of WPM
- **Amplification of Differences:** Small criterion differences can disproportionately affect results.
- **Weight Dependency:** Heavily reliant on subjective weight assignments.
- **Difficulty with Zero/Negative Values:** Cannot process zero or negative criteria values.
- **Interpretability:** Multiplicative aggregation less intuitive compared to additive methods.
- **Assumption of Independence:** Treats criteria as independent, ignoring possible interdependencies.
- **Rank Reversal:** Rankings may shift when alternatives are added or removed.

## Comparison with WSM

### Advantages over WSM:
- Better suited for non-compensatory scenarios.
- Less sensitive to scaling methods.
- Maintains consistent relative comparisons.

### Limitations compared to WSM:
- Cannot handle zero or negative values without adjustments.
- Less intuitive interpretability.
- Amplifies minor criterion differences.

## Conclusion
WPM is robust for relative, non-compensatory decision contexts but has limitations in handling zero values, interpretability, and potential rank reversal. The choice between WPM and WSM should align with the specific decision-making scenario, data characteristics, and stakeholder preferences.