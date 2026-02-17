# EXPERIMENT CONFIG (FROZEN)
# Simulation
N_CUSTOMERS = 100
NUM_WEEKS = 10

# Capacity
K = 10

# Dynamics
DECAY_RATE = 0.1
RECOVERY_RATE = 0.2

# Cooldown policy
COOLDOWN_WINDOW = 1
COOLDOWN_PENALTY = 0.7

# Evaluation
REGRET_THRESHOLD = 0.3  

# Reproducibility
SEEDS = list(range(30))