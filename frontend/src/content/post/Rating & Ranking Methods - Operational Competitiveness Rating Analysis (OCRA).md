---
title: Rating & Ranking Methods - Operational Competitiveness Rating Analysis (OCRA)
description: Rating & Ranking Methods - Operational Competitiveness Rating Analysis (OCRA)
tags:
  - OCRA
pubDate: 2025-01-06
draft: false
---

# Operational Competitiveness Ratings Analysis (OCRA)

## Overview
The **Operational Competitiveness Ratings Analysis (OCRA)** is a multi-criteria decision analysis method designed to evaluate and rank alternatives based on their operational efficiency. OCRA separately considers beneficial (maximize) and non-beneficial (minimize) criteria, making it suitable for operational benchmarking and efficiency analysis.

## Inputs
- **Alternatives:** Entities such as firms, banks, cities, or countries.
- **Criteria:** Measures for evaluating alternatives (financial, sustainability, economic).
- **Attributes:** Values linked to each criterion, categorized as:
  - **Beneficial (maximize)**
  - **Non-beneficial (minimize)**

## Steps

### Step 1: Criteria Weighting
Assign two separate weighting schemes:
- Beneficial criteria (weights sum to 1)
- Non-beneficial criteria (weights sum to 1)

### Step 2: Data Normalization
Normalize alternative performances:
- **Beneficial criteria:** Subtract the minimum criterion score from each score, then divide by the minimum score.
- **Non-beneficial criteria:** Subtract each score from the maximum criterion score, then divide by the minimum score.

### Step 3: Scaled Aggregate Performance (Non-beneficial Criteria)
Compute scaled aggregate performance scores for non-beneficial criteria:
- Calculate weighted sums for each alternative.
- Subtract the minimum aggregate score to scale the lowest alternative to zero.

### Step 4: Scaled Aggregate Performance (Beneficial Criteria)
Compute scaled aggregate performance scores for beneficial criteria:
- Calculate weighted sums for each alternative.
- Subtract the minimum aggregate score to scale the lowest alternative to zero.

### Step 5: Total OCRA Score
Combine scaled scores of beneficial and non-beneficial criteria:
- OCRA Score = (Scaled Beneficial Score) + (Scaled Non-beneficial Score) - Minimum combined score among alternatives
- Higher OCRA scores indicate better alternatives.

### Step 6: Ranking Alternatives
Rank alternatives from best to worst based on descending OCRA scores.

## Implementation Decisions
- **Normalization Methods:** Vector Normalization, Linear Scale Transformation (Max-Min, Max, Sum), Non-monotonic Normalization.
- **Weighting Schemes:** Equal weights, Centroid weights, Regression-based weights, Analytic Hierarchy Process (AHP), SMART, SMARTER, SWING.

## Key Features of OCRA
- **Dual Weighting Scheme:** Independent weighting for beneficial and non-beneficial criteria.
- **Flexible Normalization:** Adapts normalization based on criteria type and data nature.
- **Scaled Performance:** Ensures comparability by scaling scores, assigning zero to the least preferable alternative.

## Advantages of OCRA
- **Flexibility in Weighting:** Separate weights provide nuanced evaluation of beneficial and non-beneficial criteria.
- **Scalability:** Effective for large datasets.
- **Transparency:** Straightforward and intuitive method, easy for stakeholders to interpret.
- **Adaptability:** Suitable for diverse data units and applications.
- **Practical Relevance:** Ideal for operational benchmarking, efficiency analysis, and sustainability evaluations.

## Disadvantages of OCRA
- **Weight Dependency:** Results significantly depend on subjective weight assignments.
- **Scaling Sensitivity:** Outcomes sensitive to normalization and scaling choices.
- **Potential Rank Reversal:** Susceptible to rank changes when alternatives are added or removed.
- **Assumption of Additivity:** Assumes linear and additive relationships between criteria.

## OCRA vs. WSM & ARAS

| Aspect | OCRA | WSM | ARAS |
|--------|------|-----|------|
| **Weighting** | Dual weighting for beneficial/non-beneficial criteria | Single weight vector | Single weight vector |
| **Normalization** | Flexible, criteria-specific normalization | Optional or uniform scaling | Ratio-based normalization |
| **Score Calculation** | Combines scaled scores of beneficial and non-beneficial criteria | Weighted sum | Relative to ideal solution |
| **Scalability** | Handles diverse units effectively | Requires consistent units | Requires consistent units |
| **Sensitivity** | Sensitive to weights and normalization | Sensitive to weights/units | Sensitive to weights/normalization |
| **Rank Reversal** | Highly susceptible | Less susceptible | Moderately susceptible |

## When to Use OCRA
- **Operational Efficiency Focus:** Benchmarking operational performance of entities.
- **Distinct Criteria Types:** Separate consideration of beneficial and non-beneficial criteria.
- **Diverse Units of Measure:** When data involves different measurement units.
- **Relative Competitiveness:** Comparative evaluation of operational strengths and weaknesses.
- **Benchmarking:** Ideal for resource efficiency, sustainability, and performance evaluation.

## Conclusion
OCRA is a flexible and effective method for operational performance benchmarking, allowing nuanced evaluations through dual weighting schemes and flexible normalization. It is particularly suited to applications involving diverse units and operational efficiency metrics. However, careful consideration of weights and normalization methods is crucial to ensure reliable outcomes.