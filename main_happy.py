import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")

st.title("In Search for Happiness")
X_axis = st.selectbox("Select the data for X-axis",
                      (df.columns))
Y_axis = st.selectbox("Select the data for Y-axis",
                      (df.columns))
st.subheader(f"{X_axis} and {Y_axis}")



X_axis = X_axis.lower()
Y_axis = Y_axis.lower()

x_data = df[X_axis]
y_data = df[Y_axis]
figure = px.scatter(x=x_data, y=y_data, labels={"x": X_axis.upper(), "y": Y_axis.upper( )})
st.plotly_chart(figure)