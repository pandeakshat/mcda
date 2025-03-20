---
title: Rating & Ranking Methods - Weighted Aggregated Sum Product Assessment (WASPAS) Model
description: Rating & Ranking Methods - Weighted Aggregated Sum Product Assessment (WASPAS) Model
tags:
  - WASPAS
  - MCDA
pubDate: 2025-01-04
draft: false
---
# Weighted Aggregated Sum Product Assessment (WASPAS)

## Overview
The **Weighted Aggregated Sum Product Assessment (WASPAS)** is a hybrid multi-criteria decision analysis method combining the additive Weighted Sum Model (WSM) and the multiplicative Weighted Product Model (WPM). It provides flexibility by balancing compensatory and proportional trade-offs.

## Inputs
- **Alternatives:** Entities such as firms, banks, cities, or countries.
- **Criteria:** Measures used for evaluating alternatives (financial, sustainability, economic).
- **Attributes:** Values linked to each criterion, categorized as:
  - **Beneficial (maximize)**
  - **Non-beneficial (minimize)**

## Steps

### Step 1: Criteria Weighting
Assign weights reflecting criteria importance, ensuring the total weights equal 1.

### Step 2: Data Normalization
Normalize performances:
- **Beneficial criteria:** Divide each alternative’s score by the highest score.
- **Non-beneficial criteria:** Subtract each alternative’s score divided by the highest score from 1.

### Step 3: Calculate WASPAS Scores
Compute the WASPAS score for each alternative by combining WSM and WPM scores:
- WASPAS Score = α × (WSM score) + (1 - α) × (WPM score)
- α ranges from 0 to 1:
  - α = 1: Pure WSM
  - α = 0: Pure WPM
  - α = 0.5: Equal contribution from WSM and WPM

Higher WASPAS scores indicate better alternatives.

### Step 4: Ranking Alternatives
Rank alternatives from best to worst based on descending WASPAS scores.

## Implementation Decisions
- **Normalization Methods:** Linear Scale (Max, Max-Min, Sum), Vector Normalization, Non-monotonic Normalization.
- **Weighting Schemes:** Equal weights, Centroid weights, Regression-based weights, Analytic Hierarchy Process (AHP), SMART, SMARTER, SWING.
- **Parameter α:** Adjustable to balance additive and multiplicative contributions based on the decision context.

## Key Features of WASPAS
- **Hybrid Approach:** Combines WSM’s compensatory properties and WPM’s proportionality.
- **Weighted Aggregation:** Uses weights reflecting criteria importance.
- **Flexibility:** Capable of managing both beneficial and non-beneficial criteria.
- **Parameterized Control:** Offers adjustable α for balancing additive and multiplicative methods.

## Advantages of WASPAS
- **Improved Accuracy:** Combines strengths of WSM and WPM, reducing individual limitations.
- **Flexibility:** Parameter α allows control over method contribution.
- **Simplicity:** Computationally easy to implement.
- **Broad Applicability:** Suitable for diverse decision-making contexts including engineering, economics, and environmental management.

## Disadvantages of WASPAS
- **Subjectivity in Weighting:** Dependent on subjective weight assignments.
- **Normalization Sensitivity:** Choice of normalization technique impacts results.
- **Parameter Sensitivity:** The choice of α can significantly influence outcomes, adding subjectivity.

## Conclusion
WASPAS is a flexible and computationally simple hybrid decision-making method. It leverages the complementary strengths of WSM and WPM to provide robust rankings across various decision scenarios, making it suitable for handling linear and non-linear criteria relationships.

