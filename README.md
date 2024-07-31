# Expenditure Tracker


Expenditure Tracker is a Streamlit-based web application designed to help you manage and analyze your finances. It allows users to log incomes and expenditures, view detailed analyses, and track savings over time. The app provides visualizations, including pie charts and bar graphs, to give insights into spending habits.


## Features


- **Entry Logging**: Easily add income and expenditure entries.
- **Ledger**: View all logged incomes and expenditures, with the ability to highlight maximum expenditure entries by category.
- **Analysis**: Visualize income and expenditure distributions through pie charts, analyze daily expenses with a bar graph, and track savings.
- **Savings Tracker**: Set and track your savings goals with progress indicators.


## Setup


### Prerequisites


Ensure you have the following installed:


- Python 3.7+
- pip (Python package installer)


### Installation


1. **Clone the repository:**


   ```bash
   git clone https://github.com/yourusername/expenditure-tracker.git
   cd expenditure-tracker
   ```


2. **Install required packages:**


   ```bash
   pip install -r requirements.txt
   ```


### Running the App


To start the application, run the following command in the terminal:


```bash
streamlit run main_app.py
```


This will launch the app in your default web browser.


## Usage


### Entry Tab


- **Purpose**: To log new income or expenditure entries.
- **Components**:
  - **Entry Type**: Select "Income" or "Expenditure".
  - **Category**: Choose a category (dynamically updates based on Entry Type).
  - **Date**: Select the date of the entry.
  - **Description**: Add a description for the entry.
  - **Amount**: Enter the amount in the local currency.


After filling in the details, click "Add Entry" to save the record. All fields except the date will reset for new entries.


### Ledger Tab


- **Purpose**: To view and manage all income and expenditure entries.
- **Components**:
  - **Income Table**: Displays all logged incomes.
  - **Expenditure Table**: Displays all logged expenditures.
  - **Highlighted Rows**: Clicking on a "Max" value in the Analysis tab highlights corresponding rows in the expenditure table.


### Analysis Tab


- **Purpose**: To analyze financial data and track savings.
- **Components**:
  - **Income and Expenditure Distribution**: Pie charts showing the distribution of income and expenditures by category.
  - **Daily Expenditure**: A bar graph showing daily expenses over a selected date range.
  - **Category Statistics**: A table showing the average and maximum expenditure per category with buttons to highlight maximum expenses in the ledger.
  - **Savings Tracker**: Displays total income, total expenditure, and savings. Set and track savings goals with visual progress indicators.


### Customization


- **Date Range for Analysis**: The date range for analysis defaults to 15 days before and 14 days after the current date. Users can adjust these dates as needed.
- **Setting Savings Goals**: Users can input and update their savings goals, with the app tracking progress towards these goals.


## Contributions


Contributions are welcome! Please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.


---


### Additional Notes


- **Data Persistence**: The app uses a CSV file to store all financial entries. The savings goal is stored in a separate JSON file.
- **Security**: Ensure that sensitive data is handled securely, especially if deploying the app to a public server.


---
