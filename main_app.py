import streamlit as st
from data_manager import load_data, save_data, update_daily_expenses, download_excel
from entry_handler import add_entry_form
from visualization import plot_pie_charts, plot_daily_expenses
from savings_manager import load_savings_goal, save_savings_goal

# Set the layout to wide
st.set_page_config(layout="wide")

# Main app
st.title("Expenditure and Income Tracker")

# Load existing savings goal into session state
if 'savings_goal' not in st.session_state:
    st.session_state.savings_goal = load_savings_goal()

# Create tabs
tab1, tab2, tab3 = st.tabs(["Entry", "Ledger", "Analysis"])

# Entry Tab
with tab1:
    st.header("Add New Entry")
    add_entry_form()

# Ledger Tab
with tab2:
    st.header("Ledger")
    data = load_data()
    incomes = data[data['Type'] == 'Income']
    expenditures = data[data['Type'] == 'Expenditure']

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Income")
        st.dataframe(incomes)

    with col2:
        st.subheader("Expenditure")
        st.dataframe(expenditures)

    st.download_button(
        label="Download full ledger as Excel",
        data=download_excel(data),
        file_name='expenditure_income_data.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

# Analysis Tab
with tab3:
    st.header("Income and Expenditure Analysis")
    plot_pie_charts(incomes, expenditures)
    
    st.subheader("Day-to-Day Expenditure")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    plot_daily_expenses(start_date, end_date, data)
    
    # Savings Tracker
    st.subheader("Savings Tracker")

    # Calculate total income, total expenditure, and savings
    total_income = incomes['Amount'].sum()
    total_expenditure = expenditures['Amount'].sum()
    savings = total_income - total_expenditure

    # Display the metrics horizontally using columns
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"₹{total_income:,.2f}")
    col2.metric("Total Expenditure", f"₹{total_expenditure:,.2f}")
    col3.metric("Savings", f"₹{savings:,.2f}")

    # Load existing savings goal
    initial_goal = load_savings_goal()
    budget = st.number_input("Enter your expected savings goal:", min_value=0.0, value=initial_goal, format="%.2f")

    # Save new savings goal if it has changed
    if budget != initial_goal:
        save_savings_goal(budget)

    # Display progress towards savings goal
    if budget > 0:
        progress = int((savings / budget) * 100)
        progress = min(progress, 100)
    else:
        progress = 0
    st.progress(progress)