import streamlit as st
import pandas as pd
from datetime import datetime

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="Healthcare Analytics Dashboard",
    layout="wide"
)

# --------------------------------
# TITLE
# --------------------------------

st.title("🏥 MediCare Healthcare Analytics Dashboard")

st.markdown(
    "Scalable Healthcare Data Engineering Platform"
)

# --------------------------------
# CURRENT TIME
# --------------------------------

current_time = datetime.now().strftime(
    "%d-%m-%Y %H:%M:%S"
)

st.caption(
    f"Dashboard Refresh Time: {current_time}"
)

# --------------------------------
# DATA LOADING
# --------------------------------

df = pd.read_csv("data/healthcare_big_data.csv")

# --------------------------------
# DATE CONVERSION
# --------------------------------

df["admission_date"] = pd.to_datetime(
    df["admission_date"]
)

# --------------------------------
# SIDEBAR FILTERS
# --------------------------------

st.sidebar.header("🔍 Filter Analytics")

selected_city = st.sidebar.selectbox(
    "Select City",
    ["All"] + list(df["city"].unique())
)

selected_disease = st.sidebar.selectbox(
    "Select Disease",
    ["All"] + list(df["disease"].unique())
)

selected_gender = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + list(df["gender"].unique())
)

# --------------------------------
# FILTERING
# --------------------------------

filtered_df = df.copy()

if selected_city != "All":
    filtered_df = filtered_df[
        filtered_df["city"] == selected_city
    ]

if selected_disease != "All":
    filtered_df = filtered_df[
        filtered_df["disease"] == selected_disease
    ]

if selected_gender != "All":
    filtered_df = filtered_df[
        filtered_df["gender"] == selected_gender
    ]

# --------------------------------
# KPI SECTION
# --------------------------------

st.subheader("📊 Healthcare KPIs")

col1, col2, col3, col4 = st.columns(4)

total_patients = len(filtered_df)

average_age = round(
    filtered_df["age"].mean(),
    2
)

average_cost = round(
    filtered_df["treatment_cost"].mean(),
    2
)

total_revenue = (
    filtered_df["treatment_cost"].sum()
)

col1.metric(
    "Total Patients",
    total_patients
)

col2.metric(
    "Average Age",
    average_age
)

col3.metric(
    "Average Treatment Cost",
    f"₹ {average_cost}"
)

col4.metric(
    "Total Revenue",
    f"₹ {total_revenue}"
)

# --------------------------------
# DATASET
# --------------------------------

st.subheader("🧾 Healthcare Records")

st.dataframe(filtered_df.head(100))

# --------------------------------
# MONTHLY ADMISSION TREND
# --------------------------------

st.subheader("📈 Monthly Admission Trend")

monthly_admissions = (
    filtered_df
    .groupby(
        filtered_df["admission_date"]
        .dt.to_period("M")
    )
    .size()
)

monthly_admissions.index = (
    monthly_admissions.index.astype(str)
)

st.line_chart(monthly_admissions)

# --------------------------------
# DISEASE ANALYTICS
# --------------------------------

chart_col1, chart_col2 = st.columns(2)

with chart_col1:

    st.subheader("🦠 Disease Distribution")

    disease_count = (
        filtered_df["disease"]
        .value_counts()
    )

    st.bar_chart(disease_count)

with chart_col2:

    st.subheader("🏙️ City-wise Patients")

    city_count = (
        filtered_df["city"]
        .value_counts()
    )

    st.bar_chart(city_count)

# --------------------------------
# GENDER ANALYTICS
# --------------------------------

st.subheader("👨‍⚕️ Gender Distribution")

gender_count = (
    filtered_df["gender"]
    .value_counts()
)

st.bar_chart(gender_count)

# --------------------------------
# ADMISSION STATUS ANALYTICS
# --------------------------------

st.subheader("🏥 Admission Status")

admission_count = (
    filtered_df["admission_status"]
    .value_counts()
)

st.bar_chart(admission_count)

# --------------------------------
# TOP EXPENSIVE TREATMENTS
# --------------------------------

st.subheader("💰 Top Treatment Costs")

top_cost = filtered_df.sort_values(
    by="treatment_cost",
    ascending=False
).head(10)

st.dataframe(top_cost)

# --------------------------------
# FOOTER
# --------------------------------

st.markdown("---")

st.markdown(
    "Healthcare Analytics Pipeline Project | IIT Jodhpur Capstone"
)