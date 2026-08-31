

# test_harness.py
# A tiny test of our scoring logic, using fake data where we KNOW the right answer.



# The model's output: one risk score per frame (frames 0 through 10).
risk_scores = [0.1, 0.0, 0.2, 0.1, 0.3, 0.8, 0.9, 0.7, 0.85, 0.6, 0.2]

# The ground truth: the real fall happened during frames 5 through 9.
true_fall_start = 5
true_fall_end = 9



# The threshold: a frame counts as "model says FALL" if its score is above this.
threshold = 0.5
print("Setup loaded. Number of frames:", len(risk_scores))



flagged_frames = []
for frame_number in range(len(risk_scores)):
    score = risk_scores[frame_number]
    if score > threshold:
        flagged_frames.append(frame_number)

print("frames flagged by model:", flagged_frames)



# The true fall window, as the set of frames that are truly "fall".
true_fall_frames = list(range(true_fall_start, true_fall_end + 1))
print("True fall frames:", true_fall_frames)



#checking overlap
overlap = set(flagged_frames) & set(true_fall_frames)
if len(overlap) > 0:
    print("Event caught!")
else:
    print("Event missed!")



 # False alarms: frames the model flagged that were NOT truly a fall.
false_alarm_frames = set(flagged_frames) - set(true_fall_frames)
print("False alarm frames:", false_alarm_frames)

# Misses: frames that were truly a fall but the model did NOT flag.
missed_frames = set(true_fall_frames) - set(flagged_frames)
print("Missed frames:", missed_frames)



# calculating recall
recall = len(overlap) / len(true_fall_frames)
print("Recall:", recall)



# calculating precision
precision = len(overlap) / len(flagged_frames)
print("Precision:", precision)