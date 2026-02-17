Why urgency performs worse than random

At first, urgency-based prioritization looks like the right strategy. It focuses on customers who appear to be in the most trouble, based on recent behavior like faster follow-ups and worsening trends.

However, when the system is run over many weeks with limited review capacity, a problem appears.

Urgency repeatedly selects the same customers. Once a customer becomes urgent, they tend to stay near the top of the list or return there again after a short recovery. As a result, a small group of customers consumes a large share of the available review capacity across weeks.

At the same time, many customers with weaker or quieter signals are never reviewed. Their tolerance slowly decays while they remain invisible to the urgency score. When they finally appear urgent, they are often already below the regret threshold.

This creates a starvation effect: urgent cases keep getting attention, while slow-burning cases are ignored until it is too late. Over time, this leads to higher total regret.

Random selection does not target urgent customers, but it spreads attention more evenly across the population. By occasionally reviewing quiet customers, random selection prevents silent decay from accumulating and therefore achieves lower cumulative regret.

This shows that the failure of urgency is not due to bad signals or implementation errors, but due to reactive prioritization under strict capacity constraints.