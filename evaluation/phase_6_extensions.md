## Phase 6: Review Cooldown Extension

### Motivation
Phase 5 showed that naive urgency-based prioritization performs worse than random selection under capacity constraints.

This failure is structural. Urgency is reactive and repeatedly selects already-distressed customers, causing capacity to be monopolized while quieter customers decay without attention.

### Core Idea
The extension introduces a simple attention-rotation rule.

Customers reviewed recently should be temporarily less likely to be reviewed again. This prevents repeated selection while still allowing urgent cases through.

### Cooldown Rule
Each customer tracks the week they were last reviewed.

When selecting cases:
- Urgency scores are still used for ranking
- Customers reviewed in the previous week receive a soft penalty
- Highly urgent cases can still be selected
- Moderately urgent repeat cases are deprioritized

This modifies urgency without replacing it.

### Why This Fixes the Failure
The cooldown directly targets the failure observed in Phase 5:
- It reduces repeated reviews of the same customers
- It increases coverage across the population
- It allows quiet-but-decaying customers to be reviewed earlier

The goal is not to maximize short-term saves, but to reduce long-term starvation and cumulative regret.
