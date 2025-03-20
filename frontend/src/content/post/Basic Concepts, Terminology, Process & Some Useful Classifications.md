---
title: Basic Concepts, Terminology, Process & Some Useful Classifications
description: Basic Concepts, Terminology, Process & Some Useful Classifications
tags:
  - MCDA
pubDate: 2025-01-01
draft: false
---

# MCDA/MCDM Documentation

## 1. Basic Concepts and Terminology

- **Decision Problem:** Evaluating multiple alternatives against criteria to achieve objectives.
- **Alternatives:** Available options (e.g., car models).
- **Criteria:** Evaluation standards:
  - Quantitative (e.g., price, weight).
  - Qualitative (e.g., aesthetics, brand).
  - Often conflicting (e.g., cost vs. quality).
- **Attributes:** Measurable properties of alternatives linked to criteria.
- **Objectives:** Goals to maximize (e.g., safety) or minimize (e.g., cost).
- **Goals:** High-level aspirations providing strategic context.
- **Aspirations:** Flexible, subjective performance targets.
- **Weights:** Importance of criteria based on preferences.
- **Utility Functions:** Numerical representation of preferences under uncertainty (e.g., MAUT).
- **Value Functions:** Preferences under certainty (e.g., MAVT).
- **Preference Elicitation:** Capturing preferences via surveys, interviews, rankings.
- **Preference Articulation:** Iterative refinement of preferences.
- **Performance Matrix:** Alternatives (rows) vs. criteria (columns) showing scores.
- **Decision Rules:** Methods to process data (e.g., additive weighting, pairwise comparisons).
- **Aggregation:** Combining criteria scores into a composite (e.g., weighted sum, outranking).
- **Dominance:** One alternative outperforms another across all criteria.
- **Pareto Optimality:** No alternative better in all criteria; improving one worsens another.
- **Trade-offs:** Balancing conflicting criteria (e.g., safety vs. cost).
- **Uncertainty:** Probabilistic or unknown factors, handled by stochastic/fuzzy models.
- **Robustness:** Stability under varying conditions.
- **Sensitivity Analysis:** Impact assessment of changes in weights/scores.
- **Consistency:** Logical alignment of preferences (e.g., checked in AHP).

## 2. General Classification of Decision Problems

### Classification Criteria
- **Number of Decision Makers:**
  - Single/Homogeneous Group: One entity decides.
  - Heterogeneous Group: Multiple stakeholders.

- **Nature of Decision Environment:**
  - Deterministic: Factors known with certainty.
  - Uncertain: Probabilistic elements present.
  - Fuzzy: Vague or imprecise criteria/preferences.

- **Type of Alternatives:**
  - Finite: Limited options (MCDA focus).
  - Continuous (Infinite): Range of choices (MCDM focus).

- **Type of Preference Elicitation Model:**
  - Compensatory: Allows trade-offs (AHP, Weighted Sum).
  - Non-Compensatory: No trade-offs; independent satisfaction (Lexicographic).

- **Decision-Making Tasks:**
  - Static: Fixed context (Weighted Product, TOPSIS).
  - Dynamic: Time-varying factors (Dynamic Multi-Objective Optimization).

### Types of Decision Problems

| Type                     | Description                                           | Output                     | Methods                                               |
|--------------------------|-------------------------------------------------------|----------------------------|-------------------------------------------------------|
| **Description Problems** | Analyze alternative performance                       | Insights/summaries         | Multi-Criteria Descriptive Models                     |
| **Choice/Selection**     | Pick best alternative                                 | Single chosen solution     | WPM, ATKOR, MAUT, PROMETHEE                           |
| **Design Problems**      | Create optimal alternative                            | Newly designed alternative | Evolutionary Algorithms, Constraint Programming       |
| **Rating and Ranking**   | Rank alternatives                                     | Ranked list                | ELECTRE, WSM, AHP, TOPSIS                             |
| **Sorting Problems**     | Assign alternatives to predefined categories          | Category assignments       | FlowSort, ELECTRE-Tri, Multiple Criteria Sorting      |
| **Clustering Problems**  | Group alternatives without predefined categories      | Similarity clusters        | ELECTRE-Based Clustering, Fuzzy C-Means               |
| **Classification**       | Assign alternatives to unordered classes              | Class allocations          | Rule-Based Approaches, Decision Trees                 |

## 3. Steps in the MCDA/MCDM Process

1. **Define Problem & Context:** Objectives and scope.
2. **Identify Criteria & Alternatives:** Evaluation standards and options.
3. **Elicit & Articulate Preferences:** Gather/refine decision-maker preferences.
4. **Assign Weights:** Prioritize criteria importance.
5. **Evaluate Alternatives:** Score options.
6. **Apply MCDA/MCDM Method:** Appropriate methodology (AHP, TOPSIS).
7. **Make Decision:** Select/rank alternatives.
8. **Validate & Communicate:** Ensure robustness and share results.

## 4. General Classifications of Methodologies

### Based on Aggregation Philosophy
- **Compensatory Approaches:** Allow trade-offs (WSM, WPM, AHP, MAVT).
- **Non-Compensatory Approaches:** No trade-offs; criteria independent (Lexicographic, EBA, Conjunctive).
- **Outranking Approaches:** Pairwise comparisons (ELECTRE, PROMETHEE).
- **Distance-Based Approaches:** Distance from ideal solutions (TOPSIS, VIKOR).

### Performance vs. Preference Aggregation

| Aspect               | Performance Aggregation-Based                    | Preference Aggregation-Based                 |
|----------------------|---------------------------------------------------|----------------------------------------------|
| **Core Idea**        | Combine alternative performance into a score      | Combine decision-makers’ preferences         |
| **Focus**            | Objective/quantitative performance data           | Subjective preferences/judgments             |
| **Data Requirements**| Measurable performance data                       | Preferences, rankings, pairwise comparisons  |
| **Common Methods**   | WSM, TOPSIS, VIKOR, MAUT                          | AHP, PROMETHEE, ELECTRE, Conjoint Analysis   |
| **Qualitative Data** | Difficult unless quantified                       | Handles qualitative judgments well           |
| **Trade-offs**       | Explicit mathematical formulas                    | Implicit via comparisons/outranking          |
| **Aggregation**      | Direct composite score                            | Pairwise comparisons/dominance relations     |
| **Flexibility**      | Precise, quantifiable contexts                    | Subjective/imprecise scenarios               |
| **Transparency**     | Transparent, may oversimplify                     | Captures complexity, less transparent        |
| **Applicability**    | Technical/engineering decisions                   | Social/policy/group decisions                |

## 5. Key Challenges in MCDA/MCDM

- **Subjectivity:** Weights/scores based on judgment.
- **Data Availability:** Reliability impacts accuracy.
- **Complexity:** Multiple conflicting criteria.
- **Sensitivity:** Results vary with weight/criteria changes.

## Conclusion

- **Summary:** MCDA/MCDM provides structured, transparent decision-making frameworks in complex scenarios.
- **Insight:** Method selection (compensatory/non-compensatory) and understanding problem type are crucial.

## Study Tips

- **Focus Areas:** Memorize key terms (dominance, Pareto optimality), understand problem types, methodology classifications.
- **Practice:** Apply steps to sample problems (e.g., car selection) using methods like WSM, AHP.
- **Review:** Challenges, sensitivity analysis for real-world application.