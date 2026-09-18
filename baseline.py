import pandas as pd
from harness import evaluate

df = pd.read_csv("data/video_1_features.csv")

# The rule: a frame is "fall-like" if aspect ratio is above this threshold.
THRESHOLD = 1.0

df["is_fall_like"] = df["aspect_ratio"] > THRESHOLD

# Show the frames around the fall to eyeball it.
print(df[df["frame"].between(45, 75)])


fall_rows = df[df["is_fall_like"]]

fall_like_frames = fall_rows["frame"]

if len(fall_like_frames) > 0:
    predicted_start = fall_like_frames.min()
    predicted_end = fall_like_frames.max()
    print(f"Predicted fall: frames {predicted_start} to {predicted_end}")
else:
    print("No fall predicted.")


# --- Evaluate the prediction against the ground truth ---

# The true fall window (from the annotation file: frames 48-80).
true_start = 48
true_end = 80

# Turn both windows into sets of frame numbers.
predicted_frames = set(range(predicted_start, predicted_end + 1))
true_frames = set(range(true_start, true_end + 1))

# Call the shared harness function.
recall, precision = evaluate(predicted_frames, true_frames)

print(f"Recall: {recall}")
print(f"Precision: {precision}")