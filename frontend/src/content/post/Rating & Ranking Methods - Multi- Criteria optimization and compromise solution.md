---
title: Rating & Ranking Methods - Multi- Criteria optimization and compromise solution
description: Rating & Ranking Methods - Multi- Criteria optimization and compromise solution
tags:
  - MCDA
  - Optimization
  - Compromise
pubDate: 2025-01-14
draft: false
---
# VIKOR (Multi-criteria Optimization and Compromise Solution)

## Overview
The **VIKOR** method (VlseKriterijumska Optimizacija I Kompromisno Resenje) is a multi-criteria decision analysis tool that ranks alternatives by finding a compromise solution closest to the ideal solution, balancing overall performance (utility) and the worst-case scenario (regret).

## Inputs
- **Alternatives:** Entities such as firms, banks, cities, or countries.
- **Criteria:** Measures used for evaluating alternatives (financial, sustainability, economic).
- **Attributes:** Values linked to each criterion, categorized as:
  - **Beneficial (maximize)**
  - **Non-beneficial (minimize)**

## Steps

### Step 1: Criteria Weighting
Assign weights reflecting the importance of each criterion, ensuring total weights equal 1.

### Step 2: Compute Ideal and Anti-Ideal Solutions
Calculate two virtual benchmarks:
- **Positive Ideal Solution (Best):** Optimal values for beneficial criteria and minimal values for non-beneficial criteria.
- **Negative Ideal Solution (Worst):** Minimal values for beneficial criteria and optimal values for non-beneficial criteria.

### Step 3: Compute VIKOR Scores
For each alternative, calculate two types of deviations:
- **Overall Performance (Sᵢ):** Weighted sum of standardized deviations from the ideal solution.
- **Worst-case Performance (Rᵢ):** Maximum weighted standardized deviation from the ideal solution.

Compute combined VIKOR scores (Qᵢ) using a compromise parameter (α):

- \[ Q_i = α \frac{S_i - S^*}{S^- - S^*} + (1 - α) \frac{R_i - R^*}{R^- - R^*} \]

where:
- \(S^*\) and \(R^*\) are minimum deviations (best performance).
- \(S^-\) and \(R^-\) are maximum deviations (worst performance).
- \(α\) (0 ≤ α ≤ 1) balances utility and regret.
- Lower Qᵢ indicates better performance.

### Step 4: Ranking Alternatives
Rank alternatives from best to worst based on ascending VIKOR scores (Qᵢ).

## Implementation Decisions
- **Normalization Methods:** Vector Normalization, Linear Scale Transformation (Max-Min, Max, Sum), Non-monotonic Normalization.
- **Weighting Schemes:** Equal weights, Centroid weights, Regression-based weights, Analytic Hierarchy Process (AHP), SMART, SMARTER, SWING.
- **Compromise Parameter (α):** Select based on decision context:
  - α = 0 emphasizes the worst-case scenario (pessimistic).
  - α = 1 emphasizes overall performance (optimistic).
  - α between 0 and 1 balances both approaches.

## Key Features of VIKOR
- **Compromise Solution:** Balances between the ideal (best) and worst-case scenarios.
- **Utility and Regret:** Considers both overall performance and the worst-performing criterion.
- **Flexible Parameter (α):** Allows customized weighting between overall utility and worst-case regret.

## Advantages of VIKOR
- **Balanced Decision-Making:** Finds a compromise solution suitable when no alternative is superior across all criteria.
- **Flexible Evaluation:** Adaptable through parameter α for different decision-making scenarios.
- **Explicit Handling:** Clearly differentiates beneficial and non-beneficial criteria.

## Disadvantages of VIKOR
- **Sensitivity to Parameter (α):** Results significantly depend on the chosen value.
- **Requires Numerical Data:** Not suitable for purely qualitative data without conversion.
- **Potential Rank Instability:** Introducing or removing alternatives can alter rankings.
- **Criteria Independence Assumption:** Assumes no interdependencies between criteria.

## VIKOR vs. Other MCDA Methods

| Aspect                   | VIKOR                               | TOPSIS                              | DRPM                                 |
|--------------------------|-------------------------------------|-------------------------------------|--------------------------------------|
| **Core Concept**         | Compromise solution (utility & regret)| Distance to ideal solutions          | Dual reference points (reservation/aspiration)|
| **Normalization**        | Required                            | Required                            | Context-dependent                    |
| **Sensitivity**          | Sensitive to parameter (α)           | Sensitive to extremes               | Robust to variations                 |
| **Criteria Handling**    | Explicit beneficial/non-beneficial  | Explicit beneficial/non-beneficial  | Category-based weighting             |

## When to Use VIKOR
- Decision problems requiring a balanced trade-off between overall performance and the worst-case criterion.
- When no clear dominant alternative exists.
- Situations requiring explicit handling of beneficial and non-beneficial criteria.

## When NOT to Use VIKOR
- Situations predominantly qualitative in nature.
- Highly interdependent criteria.
- When strict dominance or threshold-based comparisons are required.

## Conclusion
VIKOR provides an effective compromise approach to multi-criteria decision-making, suitable for situations requiring a balance between overall utility and worst-case regret. By adjusting the compromise parameter (α), decision-makers can flexibly prioritize these aspects. Despite its sensitivity to parameter choice and assumptions of criteria independence, VIKOR remains valuable across various practical scenarios.

## References
- Opricovic, S., & Tzeng, G.-H. (2004). Compromise solution by MCDM methods: A comparative analysis of VIKOR and TOPSIS. *European Journal of Operational Research*, 156(2), 445-455.