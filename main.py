import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

# replace all header names with 

st.set_page_config(page_title = "Simple Finance App", page_icon = "💸", layout = "wide")

if "categories" not in st.session_state:
    st.session_state.categories = {
        "Uncategorized": []
    }

def load_transactions (file):
    try:
        df = pd.read_csv(file, header = None, delimiter = ",")
        df.columns = ["Date", "Details", "Credit", "Debit", "Total Due" ]
        df["Date"] = pd.to_datetime(df["Date"], format = "%m/%d/%Y")

        st.write(df)
        return df
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

def main():
    st.title("Simple Finance Dashboard")

    uploaded_file = st.file_uploader("Upload your transaction CSV file", type = ["csv"])

    if uploaded_file is not None:
        df = load_transactions(uploaded_file)

        if df is not None:
            debits_df = df["Debit"].copy()
            credits_df = df["Credit"].copy()

            tab1, tab2 = st.tabs(["Payments (Debits)", "Expenses (Credits)"])
            with tab1:
                st.write(debits_df)
            with tab2:
                st.write(credits_df)

        
main()