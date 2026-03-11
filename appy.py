import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("processed_data.csv")

st.title("Employee Engagement & Burnout Analytics Dashboard")

# -----------------------------
# Sidebar Filters
# -----------------------------

st.sidebar.header("Filters")

department = st.sidebar.selectbox(
"Select Department",
df['Department'].unique()
)

overtime_filter = st.sidebar.selectbox(
"Overtime",
["All","Yes","No"]
)

job_level = st.sidebar.slider(
"Job Level",
int(df['JobLevel'].min()),
int(df['JobLevel'].max())
)

# apply filters

filtered_df = df[df['Department']==department]

if overtime_filter != "All":
    filtered_df = filtered_df[filtered_df['OverTime']==overtime_filter]

filtered_df = filtered_df[filtered_df['JobLevel']>=job_level]

# -----------------------------
# KPI Metrics
# -----------------------------

st.subheader("Key Performance Indicators")

col1,col2,col3 = st.columns(3)

col1.metric(
"Avg Engagement",
round(filtered_df['EngagementIndex'].mean(),2)
)

col2.metric(
"Work Life Balance",
round(filtered_df['WorkLifeBalance'].mean(),2)
)

col3.metric(
"Burnout Risk %",
round((filtered_df['BurnoutRisk']=="High").mean()*100,2)
)

# -----------------------------
# Engagement Distribution
# -----------------------------

st.subheader("Engagement Distribution")

fig,ax=plt.subplots()

sns.histplot(filtered_df['EngagementIndex'],ax=ax)

st.pyplot(fig)

# -----------------------------
# Burnout Risk Chart
# -----------------------------

st.subheader("Burnout Risk Levels")

fig2,ax2=plt.subplots()

sns.countplot(
x='BurnoutRisk',
data=filtered_df,
ax=ax2
)

st.pyplot(fig2)

# -----------------------------
# Job Role Engagement
# -----------------------------

st.subheader("Engagement by Job Role")

fig3,ax3=plt.subplots()

sns.barplot(
x='JobRole',
y='EngagementIndex',
data=filtered_df,
ax=ax3
)

plt.xticks(rotation=90)

st.pyplot(fig3)

# -----------------------------
# Tenure Analysis
# -----------------------------

st.subheader("Tenure vs Engagement")

fig4,ax4=plt.subplots()

sns.scatterplot(
x='YearsAtCompany',
y='EngagementIndex',
data=filtered_df,
ax=ax4
)

st.pyplot(fig4)

# -----------------------------
# Manager Alert Panel
# -----------------------------

st.subheader("Low Engagement Employees")

low_engagement = filtered_df[filtered_df['EngagementIndex']<2]

st.dataframe(low_engagement)