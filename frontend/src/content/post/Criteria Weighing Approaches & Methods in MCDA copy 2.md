---
title: Summary -- MCDA
description: Summary -- MCDA
tags:
  - MCDA
  - Summary
pubDate: 2025-01-17
draft: false
---
# Integrated Guide to Multi-Criteria Decision Analysis (MCDA)

Multi-Criteria Decision Analysis (MCDA) is essential for structured and rational decision-making involving multiple, often conflicting, criteria. Here's a concise summary connecting the crucial aspects of the MCDA process based on rating methods, normalization, and weighting techniques.

## 1. Importance of MCDA
MCDA provides frameworks to evaluate and prioritize alternatives considering multiple criteria, enabling balanced, transparent, and justified decision-making.

## 2. Rating & Ranking Methods Overview

- **WSM (Weighted Sum Model)**: Additive model suited for compensatory decision-making.
- **WPM (Weighted Product Model)**: Multiplicative, useful for non-compensatory contexts.
- **WASPAS**: Hybrid of WSM & WPM, offers flexibility by combining additive and multiplicative approaches.
- **ARAS (Additive Ratio Assessment)**: Compares alternatives against an ideal solution.
- **OCRA (Operational Competitiveness Ratings Analysis)**: Separately evaluates beneficial and non-beneficial criteria, ideal for operational performance benchmarking.
- **CODAS (Combinative Distance-based Assessment)**: Uses Euclidean and Manhattan distances from negative ideals, robust against noise and outliers.
- **COPRAS (Complex Proportional Assessment)**: Evaluates proportional contributions from beneficial and non-beneficial criteria.
- **EDAS (Evaluation based on Distance to Average Solution)**: Focuses on deviations from the average performance, promoting stability.
- **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)**: Balances distances from ideal and negative ideal solutions.
- **DRPM (Double Reference Point Method)**: Uses reservation and aspiration benchmarks, balancing minimum and desired outcomes.
- **VIKOR (Multi-criteria Optimization and Compromise Solution)**: Compromise solution balancing overall utility and worst-case regret.

## 3. Data Normalization Methods
Normalization ensures comparability among criteria by scaling data uniformly:
- **Linear Transformations**: Min-Max, Max Normalization, Vector Normalization, Sum-Based.
- **Non-Linear Transformations**: Logarithmic, Z-score, Fuzzy, Power-based.

Choosing the right normalization method depends on data characteristics, decision context, and desired properties like robustness to outliers, range-boundedness, and preservation of proportionality.

## 4. Criteria Weighting Approaches
Weights reflect criteria importance, affecting decision outcomes significantly:

### Subjective Methods
- Direct assignment (Simple Direct, Point Allocation, Fixed Ratio).
- Ranking-based methods (Rank Sum, Rank Order Centroid).
- Pairwise comparisons (AHP, BWM, Swing, MACBETH, SWARA).
- Group decision methods (Delphi, Consensus-Based, Social Choice Theory).

### Objective Methods
- Entropy-based (Shannon Entropy).
- Statistical & variance-based (CRITIC, CV Method, PCA, Factor Analysis).

### Hybrid Methods
Integrate subjective insights with objective data, offering balanced weighting (e.g., AHP-Entropy).

## 5. Interconnection of Methods, Normalization, and Weighting
- **MCDA Rating Methods** rely heavily on criteria weights and normalization for accurate and meaningful rankings.
- **Normalization** ensures fairness and comparability, directly impacting the outcomes and validity of rankings.
- **Weighting methods** determine criteria priorities, profoundly influencing final decision outcomes and reflecting stakeholder preferences.

## 6. Practical Decision-Making Considerations
- **Contextual Alignment**: Choose methods, normalization, and weighting techniques aligned with decision goals and data nature.
- **Consistency Checks**: Validate method consistency (e.g., AHP consistency ratios).
- **Sensitivity Analysis**: Essential for understanding how changes in weights or normalization approaches affect outcomes.
- **Robustness**: Prioritize methods and transformations that minimize sensitivity to outliers and subjective biases.

## 7. Recommended Decision Workflow

1. **Define Decision Context and Objectives:** Clearly articulate the decision problem, alternatives, and criteria.
2. **Choose MCDA Method:** Based on the decision context (compensatory/non-compensatory, complexity, etc.).
3. **Select Appropriate Normalization:** Matching data types, distributions, and decision goals.
4. **Assign Criteria Weights:** Combining subjective stakeholder insights with objective data-driven approaches.
5. **Perform Analysis and Ranking:** Apply selected MCDA method with normalized data and weighted criteria.
6. **Validate Results:** Conduct sensitivity analysis to ensure stability and robustness of rankings.
7. **Communicate and Implement Decision:** Provide transparent justification based on the comprehensive MCDA process.

## Conclusion
Integrating appropriate rating methods, normalization techniques, and weighting approaches is crucial for effective and reliable MCDA outcomes. Ensuring methodological consistency and robustness through sensitivity analysis further enhances decision quality and acceptance.

