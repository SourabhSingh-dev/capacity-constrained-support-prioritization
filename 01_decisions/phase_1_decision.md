Phase 1 — Decision Definition
    Weekly Prioritization of Customer Support Cases

Problem Context
    The company receives a large volume of customer support cases on an ongoing basis.
    While many cases are routine or self-resolving, a subset require manual human intervention to prevent escalation, customer harm, or business risk.
    Human review capacity is limited.
    It is not possible to deeply review every open case within a given time window.
    As a result, the organization must decide where to allocate scarce human attention.

The core decision supported by this system is:
    Which support cases should receive human review this week, given limited capacity?

This decision is:
    made on a recurring (weekly) basis
    constrained by available human resources
    consequential, as delayed or missed intervention can lead to serious outcomes
    The system does not make the final decision.
    It provides a prioritized list to assist a human decision-maker (e.g., support operations lead), who remains accountable.

Decision-Maker and Role of the System

Decision-maker:
    A human support operations manager or senior support lead.

Role of the system:
    Assist decision-making by ranking open cases
    Surface cases where delay is likely to be dangerous
    Reduce cognitive load when reviewing large volumes of cases
    The system does not automate action or replace human judgment.

Capacity Constraint
    Human review capacity is limited and significantly smaller than total incoming case volume.
    For example:
        Only a fixed number of cases (K) can be reviewed deeply in a given week
        Increasing K has real costs (time, quality, burnout)
        Because capacity is constrained:
        Some cases will not receive immediate human attention
        The decision inherently involves trade-offs
        This scarcity is the reason prioritization is necessary.

What “Urgent” Means in This Context

Urgency is not defined as:
    high severity labels
    customer loudness
    predicted churn probability

Instead, urgency is defined as:
    The risk associated with delaying human intervention on a case.

A case is considered urgent when:
    signals suggest it is getting worse over time
    delay increases the likelihood of escalation or harm
    ignoring it would likely be regretted in hindsight
    This definition focuses on danger of delay, not static characteristics.
    Regret as the Evaluation Lens

Success is not measured by predictive accuracy.

Instead, the key evaluation question is:

Which cases would we regret not reviewing earlier?

Regret occurs when:
    warning signs were present
    a case deteriorated over time
    earlier human intervention could have prevented a serious issue
    This framing aligns the system with real operational accountability.

Why Churn Prediction Is Insufficient

Customer churn is a lagging outcome:
    it occurs after issues accumulate
    it arrives too late to guide weekly prioritization
    it is corrupted by intervention (reviewed cases improve outcomes)

Additionally:
    customers at high churn risk may not have urgent issues
    customers with urgent issues may not appear at churn risk
    Therefore, churn prediction cannot replace a dedicated prioritization system focused on immediate decision making.