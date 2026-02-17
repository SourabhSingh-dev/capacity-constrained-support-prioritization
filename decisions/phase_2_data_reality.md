Phase 2 — Data Reality
What Information Exists, What Is Missing, and What Cannot Be Trusted
Purpose of This Phase

This phase documents the actual data environment in which the prioritization decision must be made.

Rather than assuming clean labels or perfect signals, this phase explicitly acknowledges:
    what data realistically exists in a support system
    what information arrives too late to guide action
    what signals are unreliable or misleading
    what critical information is missing entirely
    This prevents the system from being designed around false assumptions.

Data We Actually Have

A typical customer support system records operational facts related to ticket activity, including:
    Customer identifier
    Ticket identifier
    Ticket creation timestamp
    Last update or last reply timestamp
    Number of customer messages or contacts
    Issue category (customer- or agent-selected)
    Severity tag (if present)
    Ticket status (open, pending, closed, reopened)
    These fields describe what happened and when, but do not directly encode urgency or risk.

Data That Arrives Too Late

Some information exists, but only after the window for intervention has passed.
These signals are useful for retrospective analysis, not for weekly prioritization.

Examples include:
    Customer churn
    Post-resolution satisfaction feedback
    Formal escalations
    Public complaints or reputational fallout
    By the time these signals appear, the opportunity to intervene earlier has already been missed.

Data That Is Unreliable or Noisy

Several available fields appear useful but cannot be trusted at face value:
    Severity labels
    Often exaggerated by customers or inconsistently applied by agents under time pressure.
    Issue categories
    Frequently misclassified, duplicated, or applied inconsistently across agents and time.
    Ticket status
    “Closed” does not necessarily mean “resolved”; tickets may be auto-closed, prematurely closed, or later reopened.
    Customer-reported urgency
    Loudness and emotional tone do not reliably correspond to true risk or urgency.
    Timestamps (interpretation)
    A long gap may indicate resolution, abandonment, or frustration; the meaning is ambiguous without context.

These signals are treated as weak hints, not ground truth.

Data We Do Not Have

Critically, the system does not have access to:
    True customer frustration or emotional state
    True tolerance for delay
    The likelihood that a case will escalate if ignored
    The downstream cost of inaction
    Which cases will later be regretted
These missing variables are exactly what make prioritization difficult and necessary.

Key Implications for System Design

Because of these data realities:
    The system cannot rely on clean labels or outcomes

Urgency must be inferred, not measured directly

Change over time is more informative than static values

Decisions must be made under uncertainty and noise

All modeling and simulation choices in later phases are constrained by these realities.