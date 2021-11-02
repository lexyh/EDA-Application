# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import plotly as py
import plotly.graph_objs as go

#Testing github desktop changes

@dataclass
class TextColumn:
  col_name: str = None
  serie: pd.Series = None
  
  def __init__(self):
    print('init')
  
  def get_name(self):
    """
    Return name of selected column
    """
    return self.col_name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    return self.serie.nunique()

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    return self.serie.isna().sum()

  def get_empty(self):
    """
    Return number of rows with empty string for selected column
    """
    return self.serie.eq('').sum()

  def get_whitespace(self):
    """
    Return number of rows with only whitespaces for selected column
    """
    return self.serie.str.isspace().sum()

  def get_lowercase(self):
    """
    Return number of rows with only lower case characters for selected column
    """
    return self.serie.str.islower().sum()

  def get_uppercase(self):
    """
    Return number of rows with only upper case characters for selected column
    """
    return self.serie.str.isupper().sum()
  
  def get_alphabet(self):
    """
    Return number of rows with only alphabet characters for selected column
    """
    return self.serie.str.isalpha().sum()

  def get_digit(self):
    """
    Return number of rows with only numbers as characters for selected column
    Assumption here is numeric values only included. Ignores subscript and special characters
    """
    return self.serie.str.isnumeric().sum()

  def get_mode(self):
    """
    Return the mode value for selected column
    """
    # identify the mode, nulls are dropped
    modes = self.serie.mode(dropna = True)

    # determine the caption to show
    caption_text = None #empty string 
    if modes is None:
        caption_text = "The selected column contains unique values (no mode found)"
    if len(modes) > 1:
        caption_text = "Multiple values in this column are equally most frequent."
    
    # put results into a table to improve presentation where multiple modes are found
    
    fig = go.Figure(data=[go.Table(
    header=dict(
            fill_color='blue',
            align='center'),
    cells=dict(values=modes['Mode Values'],
            fill_color='white',
            align='center'))
    ])

    return fig


  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    x = self.serie.unique()
    y = self.serie.value_counts()

    fig = go.Figure(data=[go.Bar(x=x, y=y, hovertext = ['some text' ])])
    
    # figure formatting
    fig.update_layout(title = "Frequency of Column Values") #bargap = 0.3, couldn't adjust

    return fig

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    d = self.serie

    ## adjust content to remove nulls and empty strings (drop whitespace, '' and nulls)
    d = d[(d !='') & d.str.isspace() == False].dropna()
    
    #create data frame to publish to streamlit
    df = pd.DataFrame(d.value_counts()).reset_index()
    df.columns = ["Value", "Occurance"]
 
    #total number of data points in column, after removing nulls
    total = self.serie.size # overall size
    total_adj = d.size #adjusted for whitespace, empty and nulls 
    df['Percentage'] = (df['Occurance']/total_adj)*100
    return df 