import pandas as pd

df = pd.read_csv("processed_data.csv")

print("Average Engagement Index:")
print(df['EngagementIndex'].mean())

print("\nWork Life Balance Average:")
print(df['WorkLifeBalance'].mean())

print("\nBurnout Risk Distribution:")
print(df['BurnoutRisk'].value_counts())