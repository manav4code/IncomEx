import streamlit as st
import pandas as pd
from data_manager import load_data, save_data

def add_entry_form():
    # Initialize session state variables if they do not exist
    if 'description' not in st.session_state:
        st.session_state['description'] = ''
    if 'amount' not in st.session_state:
        st.session_state['amount'] = 0.0

    entry_type = st.selectbox("Entry Type", ["Income", "Expenditure"], key='entry_type')

    if entry_type == "Income":
        category = st.selectbox("Category", ["Salary", "Freelance", "Investments", "Others"])
    else:
        category = st.selectbox("Category", ["Food", "Transport", "Utilities", "Entertainment", "Charity", "Others"])

    date = st.date_input("Date")
    description = st.text_input("Description", key="description")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f", key="amount")
    submit_button = st.button(label='Add Entry')

    if submit_button:
        data = load_data()  # This function should be defined elsewhere to load your data
        new_data = pd.DataFrame({
            'Date': [date],
            'Type': [entry_type],
            'Category': [category],
            'Description': [description],
            'Amount': [amount]
        })
        data = pd.concat([data, new_data], ignore_index=True)
        save_data(data)  # This function should be defined elsewhere to save your data
        st.success(f"{entry_type} added successfully!")

