import streamlit as st
import pandas as pd

st.write("""
# Assignment App

TDS Week 8
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    first_number = st.number_input("FIRST_NUMBER", step=1)
    second_number = st.number_input("SECOND_NUMBER", step=1)
    third_number = st.number_input("THIRD_NUMBER", step=1)

    data = {'FIRST_NUMBER': first_number,
            'SECOND_NUMBER': second_number,
            'THIRD_NUMBER': third_number
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

#Preprocessing

for col in df.columns:
    if df[col].dtype != 'float64':
        df[col] = df[col].values.astype('float64')

st.subheader('Pre-processed Input to the Model')
st.table(df)

st.subheader('Result: ', max(df))
