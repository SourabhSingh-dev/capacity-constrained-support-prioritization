import pandas as pd
import numpy as np
def initialize_world():
    N = 100
    df = pd.DataFrame({
        "Customer_id" : range(N),
        "tolerance" : np.random.uniform(0,1.5,size=N)
    })
    df['time_gap'] = np.random.exponential(scale=df['tolerance']*5)
    df['worsening_streak'] = 0
    df['urgency_score'] = 0
    df['reviewed'] = False
    k = 10
    reviewed_ids = np.random.choice(df.index, size = k, replace = False)
    df.loc[reviewed_ids,'reviewed'] = True

    recovery_rate = 0.2
    df.loc[df['reviewed'],'tolerance'] = (df.loc[df['reviewed'],'tolerance']*(1+recovery_rate))

    decay_rate = 0.1
    df.loc[~df['reviewed'],'tolerance'] = (df.loc[~df['reviewed'],'tolerance']*(1-decay_rate))

    df['prev_time_gap'] = df['time_gap']
    df['time_gap'] = np.random.exponential(scale=df['tolerance'] * 5)
    df['gap_change'] = df['prev_time_gap'] - df['time_gap']
    df.loc[df['gap_change'] > 0,'worsening_streak'] += 1
    df.loc[df['gap_change'] <= 0,'worsening_streak'] = 0
    df['urgency_score'] = df['gap_change'] * df['worsening_streak']

    return df
def advance_one_week(df,decay_rate,recovery_rate):
    df.loc[df["reviewed"], "tolerance"] *= (1 + recovery_rate)
    df.loc[~df["reviewed"], "tolerance"] *= (1 - decay_rate)

    df["prev_time_gap"] = df["time_gap"]
    df["time_gap"] = np.random.exponential(scale=df["tolerance"] * 5)

    df["gap_change"] = df["prev_time_gap"] - df["time_gap"]

    df.loc[df["gap_change"] > 0, "worsening_streak"] += 1
    df.loc[df["gap_change"] <= 0, "worsening_streak"] = 0

    df["urgency_score"] = df["gap_change"] * df["worsening_streak"]

    return df