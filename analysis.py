import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("file_dataset.CSV")

print(data.head())
print(data.info())
print(data.describe())


# first 5 rows show
print(data.head())

# columns ka naam
print(data.columns)

# dataset information
print(data.info())

# summary statistics
print(data.describe())

# ghaph first 

plt.figure()

sns.countplot(x='Department', data=data)

plt.title("Employees in each Department")
plt.xticks(rotation=45)

plt.show()