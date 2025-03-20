---
title: Rating & Ranking Methods - Additive Ratio Assessment (ARAS) Model
description: Rating & Ranking Methods - Additive Ratio Assessment (ARAS) Model
tags:
  - MCDA
  - ARAS
pubDate: 2025-01-05
draft: false
---

# Additive Ratio Assessment (ARAS)

## Overview
The **Additive Ratio Assessment (ARAS)** is a multi-criteria decision analysis method that evaluates alternatives by comparing their performance directly against an ideal solution. ARAS calculates the overall utility of alternatives using additive weighted scores.

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
Normalize alternative performances:
- **Beneficial criteria:** Divide each alternative’s score by the sum of scores across all alternatives.
- **Non-beneficial criteria:** Divide the minimum criterion score by each alternative's score.

### Step 3: Compute Absolute Performance
Calculate the absolute performance (weighted sum) for each alternative:
- Multiply each criterion's normalized score by its assigned weight and sum them.

### Step 4: Compute Relative Performance (ARAS Score)
Compute ARAS scores by comparing each alternative’s absolute performance to the ideal alternative (the highest absolute performance):
- ARAS Score = (Alternative's Absolute Performance) / (Ideal Absolute Performance)
- Higher ARAS scores indicate better alternatives.

### Step 5: Ranking Alternatives
Rank alternatives from best to worst based on descending ARAS scores.

## Implementation Decisions
- **Normalization Methods:** Linear Scale Transformation (Max, Max-Min, Sum), Vector Normalization, Non-monotonic Normalization.
- **Weighting Schemes:** Equal weights, Centroid weights, Regression-based weights, Analytic Hierarchy Process (AHP), SMART, SMARTER, SWING.

## Key Features of ARAS
- **Additive Model:** Simple computation based on weighted sums.
- **Ideal Alternative:** Directly compares each alternative with the ideal solution (best possible performance).
- **Critical Role of Weights:** Highlights the importance assigned to each criterion.

## Advantages of ARAS
- **Simplicity:** Easy computational process and implementation.
- **Transparency:** Straightforward additive calculation method.
- **Versatility:** Capable of handling both beneficial and non-beneficial criteria clearly.

## Disadvantages of ARAS
- **Sensitivity to Weights:** Outcomes significantly depend on criteria weights.
- **Normalization Dependency:** Choice of normalization impacts results and may cause rank reversals.
- **Linearity Assumption:** Assumes linear relationships between criteria and utility.

## ARAS vs. WSM
| Aspect | ARAS | WSM |
|--------|------|-----|
| **Comparison Basis** | Relative to an ideal solution | Individual evaluation without explicit ideal |
| **Normalization** | Ratio-based normalization | Scaled uniformly or directly weighted |
| **Utility Calculation** | Relative performance to an ideal | Direct weighted sum calculation |
| **Ideal Solution** | Explicitly incorporates an ideal solution | No explicit ideal needed |
| **Flexibility** | Handles beneficial/non-beneficial criteria explicitly | Requires scaling or transformations |

## When to Use ARAS vs. WSM
- **Use ARAS:** When comparing alternatives against an ideal solution or emphasizing relative performance.
- **Use WSM:** When direct absolute scores and simplicity are sufficient without referencing an ideal solution.

## Conclusion
ARAS provides a clear, transparent, and actionable decision-making approach by evaluating alternatives relative to an ideal solution. Its straightforward methodology makes it suitable for various practical applications, though careful attention must be given to criteria weights and normalization methods to avoid sensitivity issues.