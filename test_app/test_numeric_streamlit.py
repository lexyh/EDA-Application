import streamlit as st
import pandas as pd
import src.numeric as n
import src.numeric from NumericColumn()

# read csv
csv_path = "01-01-2021.csv"
df = pd.read_csv('/Users/annahome/Documents/GitHub/DSP_Team8/test_app/01-01-2021.csv')

# init NumericColumn
dc = n.NumericColumn()
dc.col_name = "Last_Update"
dc.serie = pd.to_numeric(df[dc.col_name], dayfirst=True)

nc1 = n.NumericColumn()
nc1.col_name = "test"
nc1.serie = pd.Series([None,28.0339, -11.2027, -30, -45, 0, 34.90171875, 34.90171875, 30.86747479,0])

# read csv
df = pd.read_csv(csv_path)

col = nc1
nc1.get_missing()
#print(nc1.get_missing())
nc = NumericColumn()

def numeric_summary(NumericColumn):

    summary = {}

    summary["Missing Values"] = NumericColumn.get_missing()
    summary["Unique Values"] = NumericColumn.get_unique()
    summary["Number Rows with 0"] = NumericColumn.get_zeros()
    summary["Number of Rows with Negative Values"] = NumericColumn.get_negatives()
    summary["Average Value"] = NumericColumn.get_mean()
    summary["Standard Deviation Value"] = NumericColumn.get_std()
    summary["Minimum Value"] = NumericColumn.get_min()
    summary["Maximum Value"] = NumericColumn.get_max()
    summary["Median Value"] = NumericColumn.get_median()

    df = pd.DataFrame(pd.Series(summary).reset_index()) 

    return df



#st.dataframe(numeric_summary(col))



st.title("Numeric Test")

dc.get_histogram()
dc.get_frequent()
