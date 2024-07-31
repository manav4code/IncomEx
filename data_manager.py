import pandas as pd
import streamlit as st
from io import BytesIO

CSV_FILE = 'expenditure_income_data.csv'

def load_data():
    try:
        return pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=['Date', 'Type', 'Category', 'Description', 'Amount'])

def save_data(data):
    data.to_csv(CSV_FILE, index=False)
    st.session_state.data = data

def update_daily_expenses(data):
    expenditures = data[data['Type'] == 'Expenditure']
    expenditures['Date'] = pd.to_datetime(expenditures['Date'])
    daily_expenses = expenditures.groupby(expenditures['Date'].dt.date)['Amount'].sum().reset_index()
    daily_expenses.columns = ['Date', 'Amount']
    return daily_expenses

def download_excel(dataframe):
    output = BytesIO()
    dataframe.to_excel(output, index=False, sheet_name='Expenditure and Income')
    output.seek(0)
    return output
