Phase 3 — Simulation Notes

Why Simulation, Hidden Truth, and Observable Proxies
Why we use simulation in this project

In this project, the core challenge is that the system must decide which support cases need human attention now, even though the true risk of each case is unknown at decision time.

In real-world systems:
    We never observe “true urgency” or “true danger” directly.
    We only see delayed, noisy outcomes (e.g., churn, escalation).
    Human intervention itself changes outcomes, corrupting labels.

Simulation allows us to:
    Define a hidden ground truth that represents real risk.
    Hide that truth from the prioritization logic.
    Observe whether our prioritization decisions would have helped before bad outcomes occurred.
    This makes it possible to reason about prioritization quality without relying on misleading real-world labels.

Why we introduce a hidden variable called tolerance
    We introduce a hidden variable called tolerance to represent a customer’s true patience for delay.

Conceptually, tolerance captures:
    how long a customer is willing to wait
    how resilient they are to being ignored
    how quickly frustration escalates if no action is taken

Tolerance is intentionally modeled as hidden truth:
    Real systems do not store “customer patience”
    Support teams never know this value explicitly
    It exists in reality, but not in data
    This mirrors real life, where customer behavior is driven by internal states that are never directly observed.

Why the system cannot see tolerance
    A core principle of this project is:
        If the system can directly observe a variable, it cannot represent true underlying risk.

If tolerance were visible:
    Prioritization would be trivial
    There would be no uncertainty
    The problem would collapse into a simple rule

By hiding tolerance:
    We force the system to infer risk indirectly
    We recreate the real-world difficulty of decision-making under uncertainty
    We avoid accidentally building a “cheating” model
    This separation between truth and observation is intentional and foundational.
    Why time gap between messages is used as a proxy
    Although tolerance is unobservable, it influences behavior.

One observable behavioral signal is:
    the time gap between consecutive customer messages

In real systems:
    Customers with high tolerance tend to wait longer before following up
    Customers with low tolerance tend to message more frequently
    As tolerance decreases, time gaps shrink

Therefore:
    Time gap acts as a proxy for patience and urgency
    Shrinking time gaps indicate that delay is becoming more dangerous
    The system sees only behavior, not intent

This aligns with how real prioritization works:
    We do not act on emotions or future outcomes
    We act on changes in observable behavior over time

Why randomness is necessary
    Even customers with similar tolerance do not behave identically:
    People are inconsistent
    External factors influence response timing
    Behavior is noisy

Randomness ensures that:
    The proxy is imperfect (as in real life)
    The system cannot deterministically infer truth
    Patterns emerge only statistically, not individually
    This prevents overfitting and preserves realism.

Summary
    In Phase 3, we intentionally construct a world where:
    True risk exists but is hidden (tolerance)
    Only indirect, noisy behavioral signals are visible (time_gap)
    Urgency emerges from change over time, not static labels
    Prioritization must operate under uncertainty, just like in production systems
    This simulation framework ensures that any prioritization logic we build later is tested against the actual difficulty of the problem, not a simplified or unrealistic version.