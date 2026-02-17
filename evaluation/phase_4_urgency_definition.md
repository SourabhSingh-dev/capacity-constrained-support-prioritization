Phase 4 — Defining Urgency for Weekly Review

What urgency means in this project
    In this system, urgency does not mean how bad a case looks at a single moment.
    Urgency means how risky it is to delay human attention for one more week.
    A case is considered urgent if observable behavior suggests that waiting longer will likely make the situation worse.

This definition focuses on change over time, not on static severity.

Signals used to estimate urgency

The system does not observe true customer tolerance or future outcomes.
It only sees behavior.

Urgency is estimated using the following observable signals:
    Time gap between messages
    Shorter gaps suggest decreasing patience.
    Change in time gap (gap_change)
    When follow-ups become faster than before, it indicates worsening behavior.
    Worsening streak
    Repeated signs of deterioration across weeks increase concern.
    Each signal on its own is weak. Urgency emerges from their combination over time.

Why urgency is defined this way
    These signals were chosen because they reflect how real support teams notice problems:
        Customers who are getting frustrated tend to follow up more frequently.
        Sudden spikes are less reliable than sustained worsening.
        Trend matters more than a single snapshot.
        Urgency is therefore treated as a directional signal, not a precise measurement.

What urgency is not

Urgency is not:
    A prediction of churn
    A measure of customer value
    A severity label
    A guarantee that intervention will succeed
    Urgency is only a tool for ranking cases relative to each other under limited capacity.

Why urgency is used despite its limitations
    Urgency-based prioritization is locally reasonable and easy to explain.
    However, as shown in Phase 5, urgency alone is not sufficient to minimize long-term regret under capacity constraints.

This limitation motivates the need for controlled extensions in later phases.