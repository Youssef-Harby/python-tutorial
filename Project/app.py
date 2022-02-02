import streamlit as st
import datetime
import abc

st.write(""" # Python OOP Project """)
    
    
## Streamlet Options
i = st.text_input('Player Name','Salah',placeholder='Salah')

ii = st.number_input('Player Number',min_value=1, max_value=30, value=11, step=1)

iii = st.number_input('Player Salary Per Week',min_value=1, max_value=100000, value=20000, step=10)

iv = st.date_input(
     "Signing Date",
     datetime.date(2019, 7, 6))
st.write('Signing Date:', iv)

v = st.number_input('Contract Duration In Years',min_value=1, max_value=5, value=3, step=1)

vi = st.number_input('Number Of Matches Played',min_value=0, value=0, step=1)

set = st.button('Set')