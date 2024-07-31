import streamlit as st
from data_manager import *

def add_entry_form():
    entry_type = st.selectbox("Entry Type", ["Income", "Expenditure"], key='entry_type')

    if entry_type == "Income":
        category = st.selectbox("Category", ["Salary", "Freelance", "Investments", "Others"])
    else:
        category = st.selectbox("Category", ["Food", "Transport", "Utilities", "Entertainment", "Others"])

    date = st.date_input("Date")
    description = st.text_input("Description", key="description")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f", key="amount")
    submit_button = st.button(label='Add Entry')

    if submit_button:
        data = load_data()
        new_data = pd.DataFrame({
            'Date': [date],
            'Type': [entry_type],
            'Category': [category],
            'Description': [description],
            'Amount': [amount]
        })
        data = pd.concat([data, new_data], ignore_index=True)
        save_data(data)
        st.success(f"{entry_type} added successfully!")
        st.session_state['description'] = ''
        st.session_state['amount'] = 0.0
