import pandas as pd

df = pd.read_csv("processed_data.csv")

df['EngagementIndex'] = (
    df['JobInvolvement'] +
    df['JobSatisfaction'] +
    df['EnvironmentSatisfaction'] +
    df['RelationshipSatisfaction']
) / 4

df.to_csv("processed_data.csv", index=False)

print("Engagement Index Created")