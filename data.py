# Import necessary modules
import streamlit as st
# Define a function 'app()' which accepts 'car_df' as an input.
def app(df):
  st.header("View Data")
  with st.beta_expander("Dataset"):
    st.table(df)
  if st.checkbox("Show Summary"):
    st.table(df.describe())
  col1, col2,col3= st.beta_columns(3)
  with col1:
    if st.checkbox("Show all column names"):
      st.table(list(df.columns))
  with col2:
    if st.checkbox("View column data-types"):
      st.table(list(df.dtypes))
  with col3:
    if st.checkbox("View column data"):
      user_col= st.selectbox("Select the column", tuple(df.drop("price", axis=1).columns))
      st.table(df[user_col])