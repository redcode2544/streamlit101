import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("ทดสอบ Demo")
st.header("Hello World!")
st.write("This is my first app")

st.image("./images/Porto.jpg", width=650, caption="Porto, Portugal")

path = "./data/bank.csv"
data = pd.read_csv(path, sep=";")
st.subheader("Data Visualization")
st.write(data)



st.image("./images/Porto.jpg", width=650, caption="Porto, Portugal")
st.subheader("Value Counts of a Categorical Column")
selected_column = st.selectbox("Select a categorical column",data.select_dtypes(include=object).columns)
st.write(f"Value counts of column: {selected_column}")
st.write(data[selected_column].value_counts())


st.subheader("Bar Plot")
columns = list(data.columns)
column = st.selectbox("Select column", columns)
st.bar_chart(data[column].value_counts())

VIDEO_URL = "https://www.youtube.com/watch?v=QQYgCxu988s"
st.subheader("Video Display")
st.video(VIDEO_URL)

option = st.radio("Select dataset option", ('bank','titanic'))
if option == 'bank':
    path = "./data/bank.csv"
    data = pd.read_csv(path, sep=";")
elif option == 'titanic':
    path = "./data/titanic.csv"
    data = pd.read_csv(path, sep=",")
    data.columns = data.columns.str.lower()
