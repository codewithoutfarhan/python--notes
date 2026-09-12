1. Origin Story of Pandas
Definition:
Pandas is one of the most powerful and popular open-source data analysis and manipulation libraries built on top of Python. Its origin dates back to 2008 when developer Wes McKinney needed a high-performance, flexible tool to perform quantitative analysis on financial data at AQR Capital Management. He convinced management to open-source the code, naming it "Pandas" which is a play on the term "Panel Data" (econometric datasets for multi-dimensional data) and "Python Data Analysis". Today, it is the backbone of data science and machine learning workflows in Python.

2. Pandas Series
Definition:
A Pandas Series is a one-dimensional labeled array capable of holding data of any type (integers, strings, floating-point numbers, Python objects, etc.). You can think of it as a single column of an Excel spreadsheet or a specialized dictionary where every element has a unique label called an index. It forms the fundamental building block of Pandas, as a DataFrame is essentially just a collection of multiple Series bundled together.

Key Code Examples for Series:
Python
import pandas as pd

# 1. Creating a Series from a list
sports = ['Cricket', 'Football', 'Tennis']
s = pd.Series(sports)
print("Basic Series:\n", s)

# 2. Creating a Series with Custom Indices
marks = [85, 90, 78]
subjects = ['Math', 'Science', 'English']
custom_series = pd.Series(marks, index=subjects)
print("\nSeries with Custom Index:\n", custom_series)

# 3. Accessing elements by index
print("\nMarks in Math:", custom_series['Math'])
3. DataFrames in Pandas
Definition:
A Pandas DataFrame is a two-dimensional labeled data structure with rows and columns, similar to a spreadsheet, an SQL table, or a matrix. It is the most commonly used object in Pandas because real-world data is rarely ever 1D; it has multiple features and records. In a DataFrame, each column can hold a different data type (e.g., column 1 can be strings, column 2 can be integers), making it extremely versatile for data cleaning and manipulation.

Key Code Examples for DataFrames:
Python
import pandas as pd

# 1. Creating a DataFrame using a Dictionary
data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Neha'],
    'Age': [21, 23, 22, 24],
    'Score': [88, 92, 79, 95]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 2. Viewing basic info and statistics
print("\nDataFrame Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# 3. Selecting specific columns
print("\nOnly Names:\n", df['Name'])

# 4. Filtering rows based on condition (Students with score > 90)
toppers = df[df['Score'] > 90]
print("\nToppers List:\n", toppers)
4. Missing Data in Pandas
Definition:
Missing data refers to the absence of values for certain variables or records within a dataset, usually represented as NaN (Not a Number) or None in Python. Real-world data is messy and incomplete due to system errors, lost surveys, or empty fields. Handling missing data is a critical preprocessing step because most machine learning models and mathematical operations will crash or give inaccurate results if fed with empty values.

Common Operations for Missing Data:
Detection (isnull() / notnull()): Checks and flags which cells contain missing values.

Dropping (dropna()): Removes entire rows or columns that contain missing values.

Imputation (fillna()): Replaces missing slots intelligently with calculated values like the mean, median, or a custom constant.

Key Code Examples for Missing Data:
Python
import pandas as pd
import numpy as np

# Creating a messy dataset with missing values (NaN)
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Printer'],
    'Price': [70000, 1500, np.nan, 12000, np.nan],
    'Stock': [10, np.nan, 25, 15, 8]
}
df = pd.DataFrame(data)
print("Dataset with Missing Data:\n", df)

# 1. Check for missing values in each column
print("\nCheck null counts:\n", df.isnull().sum())

# 2. Drop rows containing ANY missing value
df_dropped = df.dropna()
print("\nAfter Dropping Rows with NaN:\n", df_dropped)

# 3. Fill missing values (Imputation)
# Filling missing 'Price' with mean price, and 'Stock' with a default value of 0
df['Price'] = df['Price'].fillna(df['Price'].mean())
df['Stock'] = df['Stock'].fillna(0)

print("\nCleaned Data after Imputation:\n", df)
