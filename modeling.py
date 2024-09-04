#!/usr/bin/env python
# coding: utf-8

# # Task 3 - Modeling
# 
# This notebook will get you started by helping you to load the data, but then it'll be up to you to complete the task! If you need help, refer to the `modeling_walkthrough.ipynb` notebook.
# 
# 
# ## Section 1 - Setup
# 
# First, we need to mount this notebook to our Google Drive folder, in order to access the CSV data file. If you haven't already, watch this video https://www.youtube.com/watch?v=woHxvbBLarQ to help you mount your Google Drive folder.

# In[ ]:


from google.colab import drive
drive.mount('/content/drive')


# We want to use dataframes once again to store and manipulate the data.

# In[ ]:


get_ipython().system('pip install pandas')


# In[ ]:


import pandas as pd


# ---
# 
# ## Section 2 - Data loading
# 
# Similar to before, let's load our data from Google Drive for the 3 datasets provided. Be sure to upload the datasets into Google Drive, so that you can access them here.

# In[ ]:


path = "/content/drive/MyDrive/Forage - Cognizant AI Program/Task 3/Resources/"

sales_df = pd.read_csv(f"{path}sales.csv")
sales_df.drop(columns=["Unnamed: 0"], inplace=True, errors='ignore')
sales_df.head()


# In[ ]:


stock_df = pd.read_csv(f"{path}sensor_stock_levels.csv")
stock_df.drop(columns=["Unnamed: 0"], inplace=True, errors='ignore')
stock_df.head()


# In[ ]:


temp_df = pd.read_csv(f"{path}sensor_storage_temperature.csv")
temp_df.drop(columns=["Unnamed: 0"], inplace=True, errors='ignore')
temp_df.head()


# Now it's up to you, refer back to the steps in your strategic plan to complete this task. Good luck!
