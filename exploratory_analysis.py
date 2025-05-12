import pandas as pd
from speedy_charts.charts import Line
from speedy_charts.palettes import af_categorical

df = pd.read_csv(r"C:\Users\joefr\Documents\Strava Data\download_20250512\activities.csv")

df_run = df[df['Activity Type'] == 'Run']

