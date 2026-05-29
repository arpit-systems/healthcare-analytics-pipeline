import streamlit as st
import pandas as pd

st.set_page_config(
page_title="Healthcare Analytics Dashboard",
layout="wide"
)

st.title("🏥 MediCare Healthcare Analytics Dashboard")

df = pd.read_csv("data/healthcare_big_data.csv")

st.success(f"Dataset Loaded Successfully: {len(df)} Records")

st.dataframe(df.head(20))
