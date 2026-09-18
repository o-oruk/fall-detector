import pandas as pd

df = pd.read_csv("data/video_1_features.csv")

during_fall = df[(df["frame"] >= 48) & (df["frame"] <= 80)]
before_fall = df[df["frame"] < 48]

print("avg aspect ratio before fall: ", before_fall["aspect_ratio"].mean())
print("avg aspect ratio during fall: ", during_fall["aspect_ratio"].mean())