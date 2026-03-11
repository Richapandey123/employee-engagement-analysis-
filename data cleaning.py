import pandas as pd

df = pd.read_csv("file_dataset.csv")

print(df.head())

# check missing values
print(df.isnull().sum())

# convert categorical data
df['OverTime'] = df['OverTime'].map({'Yes':1,'No':0})

df['Attrition'] = df['Attrition'].map({'Yes':1,'No':0})

# save processed data
df.to_csv("processed_data.csv", index=False)

print("Data cleaning completed")