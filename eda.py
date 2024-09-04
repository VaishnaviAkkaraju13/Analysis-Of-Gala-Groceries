#!/usr/bin/env python
# coding: utf-8

# # Task 1 - Exploratory Data Analysis
# 
# This notebook will walk you through this task interactively, meaning that once you've imported this notebook into `Google Colab`, you'll be able to run individual cells of code independantly, and see the results as you go.
# 
# This notebooks is designed for users that have an understanding of Python and data analysis. There will be some helper functions and initial setup code provided, but it will be up to you to perform the analysis and to draw insights!
# 
# ---
# 
# ## Section 1 - Setup
# 
# First, we need to mount this notebook to our Google Drive folder, in order to access the CSV data file. If you haven't already, watch this video https://www.youtube.com/watch?v=woHxvbBLarQ to help you mount your Google Drive folder.

# In[4]:


from google.colab import drive
drive.mount('/content/drive')


# In order to view, analyse and manipulate the dataset, we must load it into something called a `dataframe`, which is a way of storing tabulated data in a virtual table. This dataframe will allow us to analyse the data freely. To load it into a dataframe, we will need a package called `Pandas`. We can install pandas with this command:

# In[5]:


get_ipython().system('pip install pandas')


# And now we can import this package like so:

# In[6]:


import pandas as pd


# ---
# 
# ## Section 2 - Data loading
# 
# Now that Google Drive is mounted, you can store the CSV file anywhere in your Drive and update the `path` variable below to access it within this notebook. Once we've updated the `path`, let's read this CSV file into a pandas dataframe and see what it looks like

# In[7]:


path = "/content/drive/MyDrive/Forage - Cognizant AI Program/Task 1/Resources/sample_sales_data.csv"
df = pd.read_csv(path)
df.drop(columns=["Unnamed: 0"], inplace=True, errors='ignore')
df.head()


# Using the `.head()` method allows us to see the top 5 (5 by default) rows within the dataframe. We can use `.tail()` to see the bottom 5. If you want to see more than 5 rows, simply enter a number into the parentheses, e.g. `head(10)` or `tail(10)`.

# ---
# 
# ## Section 3 - Descriptive statistics
# 
# In this section, you should try to gain a description of the data, that is: what columns are present, how many null values exist and what data types exists within each column.
# 
# To get you started an explanation of what the column names mean are provided below:
# 
# - transaction_id = this is a unique ID that is assigned to each transaction
# - timestamp = this is the datetime at which the transaction was made
# - product_id = this is an ID that is assigned to the product that was sold. Each product has a unique ID
# - category = this is the category that the product is contained within
# - customer_type = this is the type of customer that made the transaction
# - unit_price = the price that 1 unit of this item sells for
# - quantity = the number of units sold for this product within this transaction
# - total = the total amount payable by the customer
# - payment_type = the payment method used by the customer
# 
# After this, you should try to compute some descriptive statistics of the numerical columns within the dataset, such as:
# 
# - mean
# - median
# - count
# - etc...

# In[7]:





# ---
# 
# ## Section 4 - Visualisation
# 
# Now that you've computed some descriptive statistics of the dataset, let's create some visualisations. You may use any package that you wish for visualisation, however, some helper functions have been provided that make use of the `seaborn` package. If you wish to use these helper functions, ensure to run the below cells that install and import `seaborn`.

# In[8]:


get_ipython().system('pip install seaborn')


# In[9]:


import seaborn as sns


# To analyse the dataset, below are snippets of code that you can use as helper functions to visualise different columns within the dataset. They include:
# 
# - plot_continuous_distribution = this is to visualise the distribution of numeric columns
# - get_unique_values = this is to show how many unique values are present within a column
# - plot_categorical_distribution = this is to visualise the distribution of categorical columns
# - correlation_plot = this is to plot the correlations between the numeric columns within the data

# In[11]:


def plot_continuous_distribution(data: pd.DataFrame = None, column: str = None, height: int = 8):
  _ = sns.displot(data, x=column, kde=True, height=height, aspect=height/5).set(title=f'Distribution of {column}');

def get_unique_values(data, column):
  num_unique_values = len(data[column].unique())
  value_counts = data[column].value_counts()
  print(f"Column: {column} has {num_unique_values} unique values\n")
  print(value_counts)

def plot_categorical_distribution(data: pd.DataFrame = None, column: str = None, height: int = 8, aspect: int = 2):
  _ = sns.catplot(data=data, x=column, kind='count', height=height, aspect=aspect).set(title=f'Distribution of {column}');

def correlation_plot(data: pd.DataFrame = None):
  corr = df.corr()
  corr.style.background_gradient(cmap='coolwarm')


# Now it is your chance to visualise the columns, give it your best shot! As well as simply visualising the columns, try to interpret what the results mean in the context of the client.

# ---
# 
# ## Section 5 - Summary
# 
# We have completed an initial exploratory data analysis on the sample of data provided. We should now have a solid understanding of the data. 
# 
# The client wants to know
# 
# ```
# "How to better stock the items that they sell"
# ```
# 
# From this dataset, it is impossible to answer that question. In order to make the next step on this project with the client, it is clear that:
# 
# - We need more rows of data. The current sample is only from 1 store and 1 week worth of data
# - We need to frame the specific problem statement that we want to solve. The current business problem is too broad, we should narrow down the focus in order to deliver a valuable end product
# - We need more features. Based on the problem statement that we move forward with, we need more columns (features) that may help us to understand the outcome that we're solving for
# 
# 
