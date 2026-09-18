def evaluate(predicted_frames, true_frames):
    """Compare a predicted fall window to the true one. Returns (recall, precision)."""
    overlap = predicted_frames & true_frames
    false_alarms = predicted_frames - true_frames
    misses = true_frames - predicted_frames

    recall = len(overlap) / len(true_frames)
    precision = len(overlap) / len(predicted_frames)

    return recall, precision