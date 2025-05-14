
# Base Libraries

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import warnings
warnings.filterwarnings("ignore")

# UI Library

import streamlit as st

################################# Dashboard ##########################################

# Ref for Streamlit commands: https://docs.streamlit.io/develop/api-reference

st.subheader(":green[Dashboard for Data Analytics]")
st.divider()
st.write(":blue[Data Taken For Analysis..]")
df = pd.read_excel("DSAIDA_Validated.xlsx")
st.dataframe(df.head())
st.divider()
st.subheader(":red[Uni-Variate Analytics (Single Column Data Study):]")
st.divider()

cola, colb , colc = st.columns(3)
with colb:
    colname = st.selectbox("Select Column:", df.columns)

if df[colname].dtype==object:
    col1, col2,col3 = st.columns(3)
    with col1:
        st.write(f"{colname} Stats:")
        st.divider()
        st.write(df[colname].value_counts())
    with col2:
        st.write(f"{colname} Bar Chart:")
        st.divider()
        st.bar_chart(df[colname].value_counts())
    with col3:
        st.write(f"{colname} pie Chart:")
        st.divider()
        fig, ax = plt.subplots()
        ax.pie(df[colname].value_counts(), labels=df[colname].value_counts(), autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
        
        st.divider()
# Sidebar configuration for choosing analysis type and columns
st.sidebar.header('Analysis Settings')
analysis_type = st.sidebar.radio("Choose the type of analysis:", ( 'Bivariate', 'Multivariate'))        

st.subheader(":red[Bi-Variate Analytics (Two Column Data Study):]")
st.divider()
# Need to write according to our data analytics project
col1 = st.sidebar.selectbox('Select the first column:', df.columns)
col2 = st.sidebar.selectbox('Select the second column:', df.columns)
if pd.api.types.is_numeric_dtype(df[col1]) and pd.api.types.is_numeric_dtype(df[col2]):
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[col1], y=df[col2], ax=ax)
    st.pyplot(fig)
elif pd.api.types.is_numeric_dtype(df[col1]) or pd.api.types.is_numeric_dtype(df[col2]):
        fig, ax = plt.subplots()
        sns.boxplot(x=df[col1], y=df[col2], ax=ax)
        st.pyplot(fig)
else:
        st.error("Please select at least one numerical column for bivariate analysis.")
st.subheader(":red[Multi-Variate Analytics ( more then Two Column Data Study):]")
st.divider()  
cols = st.sidebar.multiselect('Select columns:', df.columns, default=df.columns[:3])
if all(pd.api.types.is_numeric_dtype(df[col]) for col in cols):
        fig = sns.pairplot(df[cols])
        st.pyplot(fig)
else:
        st.error("Multivariate analysis requires all selected columns to be numerical.")  
st.divider()            


