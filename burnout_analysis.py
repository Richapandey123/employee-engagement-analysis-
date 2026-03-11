import pandas as pd

df = pd.read_csv("processed_data.csv")

def burnout(row):

    if row['OverTime']==1 and row['WorkLifeBalance']<=2:
        return "High"

    elif row['OverTime']==1:
        return "Medium"

    else:
        return "Low"

df['BurnoutRisk'] = df.apply(burnout, axis=1)

df.to_csv("processed_data.csv", index=False)

print("Burnout analysis completed")