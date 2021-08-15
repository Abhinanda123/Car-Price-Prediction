# Import necessary modules 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import random
# Define a function 'app()' which accepts 'car_df' as an input.
def app(df):
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.header("Data Visualisation")
  col_list= st.multiselect("Select the Columns", tuple(df.drop("price",axis=1).columns))
  color_list=["red","green","orange","violet","lawngreen","tomato","purple","crimson","blue"]
  for i in col_list:
    plt.figure(figsize=(10,10))
    plt.scatter(df[i], df["price"], color= color_list[random.randInt(0,len(color_list))])
    st.pyplot()
  plot_choice= st.multiselect("Select the plot name", ("Histogram","Correlation heatmap","Boxplot"))
  for i in plot_choice:
    if i=="Histogram":
      col_choice= st.selectbox("Select the columns for the histogram",tuple(df.drop("price",axis=1).columns))
      plt.figure(figsize=(10,10))
      plt.hist(df[col_choice], bins= "sturges", color= color_list[random.randInt(0,len(color_list))], edgecolor= "black")
      st.pyplot()
    if i=="Correlation heatmap":
      plt.figure(figsize=(10,10))
      sns.heatmap(df.corr(), annot=True)
      st.pyplot()
    if i=="Boxplot":
      col_choice= st.selectbox("Select the columns for the box-plot",tuple(df.drop("price",axis=1).columns))
      plt.figure(figsize=(10,10))
      sns.boxplot(df[col_choice])
      st.pyplot()