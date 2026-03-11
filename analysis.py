import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
df = pd.read_csv("file_dataset.csv")
# 3 Convert text columns to numeric
df_numeric = df.copy()

for col in df_numeric.select_dtypes(include="object").columns:
    df_numeric[col] = df_numeric[col].astype("category").cat.codes
# heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df_numeric.corr(), cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print("Dataset Shape:", df.shape)
print(df.head())
print(df.info())

# Attrition Count
plt.figure(figsize=(6,4))
sns.countplot(x="Attrition", data=df)
plt.title("Employee Attrition Count")
plt.show()

# Work Life Balance vs Attrition
plt.figure(figsize=(6,4))
sns.countplot(x="WorkLifeBalance", hue="Attrition", data=df)
plt.title("Work Life Balance vs Attrition")
plt.show()

# Job Satisfaction vs Attrition
plt.figure(figsize=(6,4))
sns.countplot(x="JobSatisfaction", hue="Attrition", data=df)
plt.title("Job Satisfaction vs Attrition")
plt.show()

# Monthly Income vs Attrition
plt.figure(figsize=(6,4))
sns.boxplot(x="Attrition", y="MonthlyIncome", data=df)
plt.title("Monthly Income vs Attrition")
plt.show()

# Age Distribution
plt.figure(figsize=(6,4))
sns.histplot(df["Age"], bins=20)
plt.title("Age Distribution")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.title("Feature Correlation")
plt.show()