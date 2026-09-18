import pandas as pd

# Open the annotation file and read all its lines into a list.
with open("data/annotations/video (1).txt") as f:
    lines = f.readlines()


# The first two lines are the fall start and end frames.
fall_start = int(lines[0])
fall_end = int(lines[1])


print("Fall starts at frame:", fall_start)
print("Fall ends at frame:", fall_end)
print("Total lines in file:", len(lines))

# create a list (array) which contains all the rows that correspond to frames
frame_rows = lines[2:] 

parsed_frames = []
for row in frame_rows:
    parts = row.strip().split(",")
    if len(parts) < 6:
        continue  # Skip rows that don't have enough data
    numbers = [int(p) for p in parts]  # convert each piece to an int
    parsed_frames.append(numbers)

print("Number of parsed frames:", len(parsed_frames))
print("First parsed frame:", parsed_frames[0])
print("A frame during the fall:", parsed_frames[50])




feature_rows = []
for frame_data in parsed_frames:
    frame_num = frame_data[0]
    x1 = frame_data[2]
    y1 = frame_data[3]
    x2 = frame_data[4]
    y2 = frame_data[5]


    width = x2 - x1
    height = y2 - y1


    if height == 0:
        aspect_ratio = None
    else:
        aspect_ratio = width / height

    feature_rows.append({
        "frame": frame_num,
        "width": width,
        "height": height,
        "aspect_ratio": aspect_ratio
    })

df = pd.DataFrame(feature_rows)

print(df.head(10))
print(df.shape)

# Save the features to a CSV file for later use.
df.to_csv("data/video_1_features.csv", index=False)
print("Saved features to data/video_1_features.csv")