import streamlit as st
import datetime 
import pandas as pd
from player import *
import abc

st.write(""" # Python OOP Project """)
    
    
## Streamlet Options
i = st.text_input('Player Name','Salah',placeholder='Salah')

ii = st.number_input('Player Number',min_value=1, max_value=30, value=11, step=1)

iii = st.number_input('Player Salary Per Week',min_value=1, max_value=100000, value=20000, step=10)

timee = st.date_input(
     "Signing Date",
     datetime.date(2011, 7, 6))
st.write('Signing Date:', timee)
iv = str(timee.strftime('%Y-%m-%d'))
v = st.number_input('Contract Duration In Years',min_value=1, max_value=5, value=3, step=1)

vi = st.number_input('Number Of Matches Played',min_value=0, value=0, step=1)

st.write(iv)

result = st.button('Set') #(returns true/false)

if result:
     p1 = player(i,ii,iii,iv,v,vi)
     st.write(p1.playerName)
     st.write(p1.playerNumber)
     st.write(p1.playerSalaryPerWeek)
     st.write(p1.playerSigningDate)
     st.write(p1.playerContractDurationInYears)
     st.write(p1.playerNumberOfMatchesPlayed)
     st.write(p1.calcSalaryPerYear())