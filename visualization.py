import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot_pie_charts(incomes, expenditures):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    colors = sns.color_palette('Set3', 10)
    explode_factor = 0.05  # Factor to explode slices

    # Expenditure Pie Chart
    if not expenditures.empty:
        exp_by_category = expenditures.groupby('Category')['Amount'].sum()
        explode = [explode_factor] * len(exp_by_category)  # Explode all slices slightly
        wedges, texts, autotexts = ax1.pie(
            exp_by_category, labels=exp_by_category.index, autopct='%1.1f%%',
            startangle=90, colors=colors, explode=explode, shadow=True
        )
        ax1.set_title('Expenditure by Category')
        for text in texts:
            text.set_fontsize(12)
        for autotext in autotexts:
            autotext.set_fontsize(12)
            autotext.set_color('black')
        ax1.legend(wedges, exp_by_category.index, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    else:
        ax1.text(0.5, 0.5, 'No expenditure data', horizontalalignment='center', verticalalignment='center')

    # Income Pie Chart
    if not incomes.empty:
        inc_by_category = incomes.groupby('Category')['Amount'].sum()
        explode = [explode_factor] * len(inc_by_category)
        wedges, texts, autotexts = ax2.pie(
            inc_by_category, labels=inc_by_category.index, autopct='%1.1f%%',
            startangle=90, colors=colors, explode=explode, shadow=True
        )
        ax2.set_title('Income by Category')
        for text in texts:
            text.set_fontsize(12)
        for autotext in autotexts:
            autotext.set_fontsize(12)
            autotext.set_color('black')
        ax2.legend(wedges, inc_by_category.index, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    else:
        ax2.text(0.5, 0.5, 'No income data', horizontalalignment='center', verticalalignment='center')

    plt.tight_layout()
    st.pyplot(fig)

def plot_daily_expenses(start_date, end_date, data):
    if start_date and end_date:
        # Ensure the dates are in the correct format
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        # Generate a full date range and create a DataFrame with zero expenses
        full_date_range = pd.date_range(start=start_date, end=end_date)
        expense_df = pd.DataFrame({'Date': full_date_range, 'Amount': 0})

        # Convert 'Date' in main data to datetime
        data['Date'] = pd.to_datetime(data['Date'])

        # Filter expenditures within the selected date range
        mask = (data['Date'] >= start_date) & (data['Date'] <= end_date) & (data['Type'] == 'Expenditure')
        filtered_data = data[mask]

        # Sum the expenditures per day and update the expense DataFrame
        if not filtered_data.empty:
            daily_expenses = filtered_data.groupby(filtered_data['Date'].dt.date)['Amount'].sum()
            daily_expenses.index = pd.to_datetime(daily_expenses.index)
            expense_df.set_index('Date', inplace=True)
            expense_df.update(daily_expenses)
            expense_df.reset_index(inplace=True)

        # Plotting the bar graph with adjusted figure size
        fig, ax = plt.subplots(figsize=(8, 2))
        sns.barplot(x=expense_df['Date'], y=expense_df['Amount'], ax=ax, palette='viridis')

        # Format x-axis labels to display only the day and month (DD-MM)
        ax.set_xticklabels(expense_df['Date'].dt.strftime('%d-%m'), rotation=300)

        # Reduce font size for tick labels
        ax.tick_params(axis='x', labelsize=6)  # X-axis tick labels
        ax.tick_params(axis='y', labelsize=6)  # Y-axis tick labels

        # Set y-axis ticks with 4 minor ticks between each major tick
        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # 5 intervals = 4 minor ticks

        # Enable grid for both major and minor ticks
        ax.grid(True, which='major', axis='y', linestyle='--', linewidth=0.5, color='#303030')
        ax.grid(True, which='minor', axis='y', linestyle='--', linewidth=0.5, color='gray')
        ax.set_axisbelow(True)  # Ensure grid lines are below the bars

        ax.set_xlabel('Date')
        ax.set_ylabel('Amount')
        st.pyplot(fig)

         # Calculate average and maximum expenses per category
        if not filtered_data.empty:
            category_stats = filtered_data.groupby('Category')['Amount'].agg(['mean', 'max']).rename(columns={'mean': 'Avg', 'max': 'Max'})
            category_stats = category_stats.reset_index()

            # Display the category statistics table
            st.subheader("Expense per Category")
            st.table(category_stats.style.format({'Avg': '{:.2f}', 'Max': '{:.2f}'}))

def display_savings_tracker(incomes, expenditures):
    total_income = incomes['Amount'].sum()
    total_expenditure = expenditures['Amount'].sum()
    savings = total_income - total_expenditure

    st.metric("Total Income", f"₹{total_income:.2f}")
    st.metric("Total Expenditure", f"₹{total_expenditure:.2f}")
    st.metric("Savings", f"₹{savings:.2f}")

    budget = st.number_input("Enter your expected savings goal:", min_value=0.0, format="%.2f")
    if budget > 0:
        progress = int((savings / budget) * 100)
        progress = min(progress, 100)
    else:
        progress = 0
    st.progress(progress)
