# Import from Standard Library
import os
from pathlib import Path

# Import from Third Party Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set directory paths
DIR_THIS_FILE =  Path(__file__).resolve().parent
print(f"Current working directory: {DIR_THIS_FILE}")

DIR_ROOT = DIR_THIS_FILE.parent
print(f"Root directory: {DIR_ROOT}")

DIR_DATA = DIR_ROOT / 'data' / 'raw' 
print(f"Data directory: {DIR_DATA}")

DIR_PLOTS = DIR_ROOT / 'plots' 
print(f"Plots directory: {DIR_PLOTS}")

# Verify the path exists
if os.path.exists(DIR_DATA):
    print(f"Path exists: {DIR_DATA}")
else:
    print("Path not found. Check your path string.")

#####################################
## Section 1. Import and Inspect the Data
#####################################


# Define the path to your data file
data_file = DIR_DATA / 'events-US-1980-2024-Q4.csv'  
# Load the data
df = pd.read_csv(data_file)

# Display the first few rows
df.head()

#####################################
## Section 2. Explore the Data
#####################################

# Display the shape of the DataFrame
print(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# Display column names
print("Column Names:")
print(df.columns.tolist())

# Display data types and non-null counts
df.info()

# Display summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

#####################################
## Section 3. Clean the Data
######################################

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)

# Drop rows with missing values (if appropriate)
df_cleaned = df.dropna()

# Alternatively, fill missing values with a default value
# df_filled = df.fillna(value=0)

# Check for duplicate rows
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Drop duplicate rows
df_no_duplicates = df.drop_duplicates()



#####################################
## Section 4. Explore Numeric Columns 
#####################################


# Histograms for all numerical columns
['Name', 'Disaster', 'Begin Date', 'End Date', 'CPI-Adjusted Cost', 'Unadjusted Cost', 'Deaths', 'Begin_Date', 'Begin_Year', 'Begin_Month']

df.hist(bins=30, figsize=(12, 8), edgecolor='black')
plt.suptitle('Histograms of Numerical Columns')
plt.tight_layout()
#plt.show()
plt.savefig( DIR_PLOTS / '04a_histograms.png')

# Boxplots to identify outliers
numeric_cols = df.select_dtypes(include='number').columns
num_cols = len(numeric_cols)

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=num_cols, figsize=(5 * num_cols, 6), sharey=False)

# Ensure axes is iterable
if num_cols == 1:
    axes = [axes]

# Plot each boxplot in its own subplot
for ax, col in zip(axes, numeric_cols):
    sns.boxplot(y=df[col], ax=ax)
    ax.set_title(f'Boxplot of {col}')
    ax.set_ylabel(col)
    ax.set_xlabel('')

plt.tight_layout()
#plt.show()
plt.savefig(DIR_PLOTS / '04b_boxplots.png')

# Correlation matrix - show relationships between numerical variables
correlation_matrix = df.corr(numeric_only=True)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
#plt.show()
plt.savefig(DIR_PLOTS / '04c_heatmap.png')

#####################################
## Section 5. Feature Engineering
#####################################

# Add features

# Add BEGIN_DATE column as datetime
df['Begin_Date'] = pd.to_datetime(df['Begin Date'].astype(str), format='%Y%m%d', errors='coerce')
print(df['Begin_Date'].isna().sum())

# Extract Year from 'Begin_Date'
df['Begin_Year'] = df['Begin_Date'].dt.year

# Extract Month from 'Begin_Date'
df['Begin_Month'] = df['Begin_Date'].dt.month

# Display column names
print("Column Names:")
print(df.columns.tolist())

#####################################
## Section 6. Visualize Trends
#####################################



# Columns after adding new features
# ['Name', 'Disaster', 'Begin Date', 'End Date', 'CPI-Adjusted Cost', 'Unadjusted Cost', 'Deaths', 'Begin_Date', 'Begin_Year', 'Begin_Month']

# Aggregate CPI-Adjusted Cost by year
yearly_cost_df = df.groupby('Begin_Year')['CPI-Adjusted Cost'].sum().reset_index()

# Plot CPI-Adjusted Cost by year
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")
sns.barplot(data=yearly_cost_df, x='Begin_Year', y='CPI-Adjusted Cost', color='green')
plt.title('CPI-Adjusted Cost by Year')
plt.xlabel('Year')
plt.ylabel('CPI-Adjusted Cost ($)')
plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()
plt.savefig(DIR_PLOTS / '06a_trendCPICost.png')

# Aggregate Deaths by year
yearly_deaths_df = df.groupby('Begin_Year')['Deaths'].sum().reset_index()

# Plot number of deaths over time
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")
sns.barplot(data=yearly_deaths_df, x='Begin_Year', y='Deaths', color='skyblue')
plt.title('Number of Deaths by Year')
plt.xlabel('Year')
plt.ylabel('Deaths')
plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()
plt.savefig(DIR_PLOTS / '06b_trendDeaths.png')
