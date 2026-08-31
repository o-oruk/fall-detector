

# test_harness.py
# A tiny test of our scoring logic, using fake data where we KNOW the right answer.

# The model's output: one risk score per frame (frames 0 through 10).
risk_scores = [0.1, 0.0, 0.2, 0.1, 0.3, 0.8, 0.9, 0.7, 0.85, 0.6, 0.2]

# The ground truth: the real fall happened during frames 5 through 9.
true_fall_start = 5
true_fall_end = 9

# The threshold: a frame counts as "model says FALL" if its score is above this.
theshold = 0.5
print("Setup loaded. Number of frames:", len(risk_scores))

