What small rule did we add, and why does it fix the failure we observed ?
Motivation

In Phase 5, urgency-based prioritization was shown to perform worse than random selection in terms of cumulative regret. This was not due to incorrect signals or implementation errors, but due to a structural failure.

Urgency is reactive. It repeatedly selects customers who are already in distress. Under strict capacity constraints, this leads to a small subset of customers being reviewed again and again, while quieter customers decay silently without ever receiving attention.

Phase 6 introduces a minimal system-level rule to address this imbalance.

Core Idea

The key idea is attention rotation.

If a customer was reviewed recently, they should be temporarily less likely to be reviewed again. This prevents urgency from repeatedly selecting the same customers and allows attention to reach customers who have not yet become loud.

This extension does not replace urgency. It modifies how urgency is applied.

The Review Cooldown Rule

Each customer maintains a short memory of recent reviews.

A customer is considered “recently reviewed” if they were reviewed within the last N weeks.

When selecting cases for review:
    Urgency scores are still used for ranking.
    Customers who were reviewed recently receive a soft penalty.
    Highly urgent cases can still be selected despite the penalty.
    Moderately urgent repeat cases are deprioritized in favor of others.
    This creates friction against repeated selection without banning any customer outright.

Why This Is Not Cheating

The cooldown rule:
    Does not observe hidden tolerance.
    Does not use future outcomes.
    Does not predict churn or regret.
    Uses only review history, which the system naturally has access to.
    This makes it a policy constraint, not a modeling shortcut.

What This Fixes
    The cooldown directly targets the failure observed in Phase 5:
    It reduces repeated reviews of the same customers.
    It increases coverage across the customer population.
    It allows quiet-but-decaying customers to be reviewed earlier.
    It reduces long-term cumulative regret.
    The goal is not to save more customers in any single week, but to avoid systematic starvation over time.

What This Does Not Fix

The cooldown does not:
    Eliminate regret entirely.
    Guarantee optimal prioritization.
    Replace human judgment.
    Make urgency a perfect signal.
    It only corrects a known structural imbalance in a greedy, reactive policy.

Evaluation Plan
The cooldown extension will be evaluated using the same setup and metrics as Phase 5:
    Same simulation environment
    Same regret definition
    Same capacity constraints

Comparison across:
    Random selection
    Naive urgency
    Urgency with cooldown
    Any improvement will be interpreted as evidence that attention rotation improves system stability under capacity constraints.