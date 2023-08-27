import streamlit as st
import pandas as pd

st.write("""
# Assignment App

TDS Week 8
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    first_number = st.number_input("FIRST_NUMBER", min_value=0.0,max_value=2000000000.0)
    second_number = st.number_input("SECOND_NUMBER", min_value=0.0,max_value=2000000000.0)
    third_number = st.number_input("THIRD_NUMBER", min_value=0.0,max_value=2000000000.0)

    data = {'FIRST_NUMBER': first_number,
            'SECOND_NUMBER': second_number,
            'THIRD_NUMBER': third_number
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
df_dict = df.to_dict()
st.write(df_dict)

for col in df.columns:
    if df[col].dtype != 'float64':
        df[col] = df[col].values.astype('float64')

st.subheader('The biggest number is')
st.subheader('Result: ', df_dict['FIRST_NUMBER'])
