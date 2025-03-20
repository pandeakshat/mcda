---
title: Rating & Ranking Methods - Double Reference Point Method (DRPM)
description: Rating & Ranking Methods - Double Reference Point Method (DRPM)
tags:
  - DRPM
  - MCDA
pubDate: 2025-01-11
draft: false
---
# Double Reference Point Method (DRPM)

## Overview
The **Double Reference Point Method (DRPM)** is a multi-criteria decision analysis tool that evaluates alternatives using two reference points: reservation (minimum acceptable) and aspiration (desired) levels. It provides a nuanced assessment by balancing compensatory and non-compensatory criteria evaluation.

## Inputs
- **Alternatives:** Entities such as firms, banks, cities, or countries.
- **Criteria:** Measures categorized into multiple groups (e.g., financial, operational, market performance).
- **Attributes:** Values linked to each criterion, categorized as:
  - **Beneficial (maximize)**
  - **Non-beneficial (minimize)**

## Steps

### Step 1: Criteria Weighting
Assign weights to criteria categories reflecting their relative importance, ensuring total weights equal 1.

### Step 2: Compute Double Reference Points
Calculate three preliminary points:
- **Best Performance:** Optimal values for each criterion.
- **Worst Performance:** Least favorable values for each criterion.
- **Average Performance:** Mean values for each criterion.

Establish:
- **Reservation Point:** Midway between worst and average performances.
- **Aspiration Point:** Midway between average and best performances.

### Step 3: Compute Achievement Function
Evaluate alternatives relative to reservation and aspiration points:
- Scores range from -1 (below reservation) to 2 (above aspiration), with intermediate values indicating varying degrees of acceptability and desirability.

### Step 4: Calculate Category-Based Scores
For each criterion category:
- **Strong (non-compensatory) Performance Score:** Minimum achievement across criteria in the category.
- **Weak (compensatory) Performance Score:** Average achievement across criteria in the category.

### Step 5: Compute Overall DRPM Scores
Combine category scores into a mixed performance score:
- DRPM Score = α × (Weighted Sum of Weak Scores) + (1 - α) × (Minimum Weighted Strong Score)
- α parameter (0 ≤ α ≤ 1) adjusts the compensation level between criteria.
- Higher DRPM scores indicate better alternatives.

### Step 6: Ranking Alternatives
Rank alternatives from best to worst based on descending DRPM scores.

## Implementation Decisions
- **Weighting Schemes:** Equal weights, Centroid weights, Regression-based weights, Analytic Hierarchy Process (AHP), SMART, SMARTER, SWING.
- **Compensation Level (α):** Adjust according to decision-maker preferences or application context.

## Key Features of DRPM
- **Dual Reference Points:** Uses reservation and aspiration benchmarks.
- **Relative Scaling:** Performance evaluations are context-dependent, not absolute.
- **Flexible Compensation:** Customizable trade-off between compensatory and non-compensatory criteria evaluation.
- **Category-Based Weighting:** Allows prioritizing criteria groups separately.

## Advantages of DRPM
- **Nuanced Evaluation:** Clearly differentiates between minimally acceptable and desirable outcomes.
- **Flexible Adjustments:** Parameter α enables tailored compensatory evaluations.
- **Robustness:** Less sensitive to data fluctuations due to contextual benchmarks.
- **Balanced Trade-offs:** Effectively handles multiple conflicting criteria.

## Disadvantages of DRPM
- **Criteria Independence Assumption:** Assumes no interaction between criteria.
- **Linear Assumption:** May not capture complex or non-linear relationships.
- **Interpretation Complexity:** Intermediate achievement values can be challenging to interpret.
- **Subjective Parameter Selection:** Choosing the α parameter can be subjective and influential.
- **Limited Qualitative Data Handling:** Difficulty translating subjective assessments into numeric values.

## DRPM vs. Other MCDA Methods

| Aspect                  | DRPM                          | TOPSIS                                | COPRAS                                   |
|-------------------------|-------------------------------|---------------------------------------|------------------------------------------|
| **Core Concept**        | Double reference points       | Ideal and negative ideal solutions    | Proportional contributions               |
| **Normalization**       | Relative to reservation/aspiration| Absolute (best-worst) normalization| Proportional normalization               |
| **Criteria Handling**   | Separate by categories        | Combined                              | Explicit beneficial/non-beneficial       |
| **Compensation Level**  | Adjustable via α              | Fixed                                 | Fixed proportional contributions         |
| **Sensitivity**         | Robust to data variations     | Sensitive to extremes                 | Sensitive to weights and normalization   |

## When to Use DRPM
- Complex multi-criteria scenarios with clear minimum and desired performance thresholds.
- Situations requiring explicit differentiation between minimally acceptable and desirable outcomes.
- Decision contexts needing customizable criteria compensation.

## When NOT to Use DRPM
- Highly interdependent criteria.
- Problems predominantly qualitative or subjective.
- Decision scenarios requiring extensive non-linear modeling.

## Conclusion
DRPM is an effective decision-making framework offering balanced, customizable evaluations using dual reference points. It provides significant flexibility in criteria evaluation but requires careful consideration of assumptions, parameter choices, and application context.

## References
- Wierzbicki, A. P., Makowski, M., & Wessels, J. (Eds.). (2000). Model-Based Decision Support Methodology with Environmental Applications. Kluwer Academic Publishers, Dordrecht.

