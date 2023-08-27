import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# Assignment App

TDS Week 8
""")
#Get Input

st.header('User Input Parameters')

def user_input():
    first_number = st.number_input("FIRST_NUMBER", min_value=0.0,max_value=2000000000.0)
    second_number = st.number_input("SECOND_NUMBER", min_value=0.0,max_value=2000000000.0)
    third_number = st.number_input("THIRD_NUMBER", min_value=0.0,max_value=2000000000.0)

    data = [ first_number, second_number, third_number ]
    return data

data = user_input()

st.subheader('User Input parameters')
st.write(data)

st.subheader('The biggest number is:')
st.write(np.max(data))
