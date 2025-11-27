import pandas as pd
import numpy as np
from datetime import datetime as dt
import csv


data = pd.read_csv(r"C:\Users\DELL\Desktop\python notes\PANDAS\Data_cleaning_with_pandas\data\raw\Assignment_6_sales_data.csv")
df = pd.DataFrame(data)


# Inspection
# print(df.isnull().sum())
# print(df.info())
# print(df.duplicated().sum())

# print(df.dtypes)
# print(df.shape)
# print(df.describe())
# print(df.head(100))

def clean_column_name(col): 
    return col.strip().lower().replace(' ', '_').replace('-', '_') 
df.columns = [clean_column_name(col) for col in df.columns]
# print(df.columns)
df['customer_name'].fillna("Unknown", inplace=True)
df['customer_name'].str.lower().str.title()
# print(df['customer_name'].isna().sum())


# Gender Cleaning And Standardization
df['gender'].fillna('Unknown', inplace=True)

gender_standard = {
    "MALE": 'Male', 'male': 'Male',
    "FEMALE":'Female', 'female': 'Female',
    'UNKNOWN': 'Unknown', 'unknown': 'Unknown' 
}
df['gender'] = df['gender'].replace(gender_standard)


# Filling missing Age
median_df = df['age'].median()
df['age'].fillna(median_df, inplace=True)
df['age'] = pd.to_numeric(df['age'], errors='coerce').astype(int)

# Task 7: Customer Segmentation
def age_bracket(age):
    if age < 25:
        return 'Young'
    elif age >= 25 & age <= 40:
        return 'Middle'
    else:
        return 'Mature'
    
df['age_bracket'] = df['age'].apply(age_bracket)

category_df = {
    'electronics':'Electronics' , 'eLeCtronics': 'Electronics', 'eLeCtrOnIcs': 'Electronics',
    'clothing': 'Clothing', 'CloThIng': 'Clothing', 'CLOTHING':'Clothing', 'Cloth ing': "Clothing", 'ClOThIng': 'Clothing',
    'furniture': 'Furniture', 'furniTure': 'Furniture', 'furnITure': 'Furniture'
}
df['category'] = df['category'].replace(category_df)
category_map = {'Electronics': 'ET', 'Clothing': 'CL', 'Furniture': 'FR'}
df['category_code'] = df['category'].map(category_map)
# print(df['category_code'].unique())

# print( df.groupby('category')['price'].mean())
df['price'] = pd.to_numeric(df['price'], errors='coerce', downcast='float').round(2)
df['price'] = df.groupby('category')['price'].transform(lambda x: x.fillna(x.mean()))
print(df['price'])



df['quantity'].fillna(method= 'ffill', inplace=True)
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['quantity'] = df['quantity'].astype(int)


# Calculating Revenue
df['sub_total'] = (df['price'] * df['quantity']).round(2)
df['tax'] = (df['sub_total'] * 0.075).round(2)
df['final_total'] = df['sub_total'] + df['tax']
# print(df['final_total']) 



df['purchase_date'] = df['purchase_date'].str.replace('invalid_date','')
df['purchase_date'] = pd.to_datetime(df['purchase_date'], errors= 'coerce')
df['purchase_date'].fillna(method= 'ffill', inplace=True)
df['purchase_date'] = df['purchase_date'].bfill()
# print(df['purchase_date'].dtypes)

# Date Extraction
df['year'] = df['purchase_date'].dt.year
df['month'] = df['purchase_date'].dt.month
df['month_name'] = df['purchase_date'].dt.month_name()
df['day_of_week'] = df['purchase_date'].dt.day_name()
df['quarter'] = df['purchase_date'].dt.quarter


# Filling the Missing Emails
df['email'].fillna('no@email.com', inplace= True)



#Task 8: Export
df.to_csv(r'C:\Users\DELL\Desktop\python notes\PANDAS\Data_cleaning_with_pandas\data\clean\transformed_sales_data.csv', sep='', index=False)
print(df.info())



    
