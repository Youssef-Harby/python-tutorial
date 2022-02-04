import streamlit as st
import datetime 
import pandas as pd
from player import *

st.set_page_config(layout="wide")
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

# SetState
data = []

if 'set' not in st.session_state:
     st.session_state.set = data
if 'count' not in st.session_state:
     st.session_state.count = 0


def callbackf():
     # if change:
          st.session_state.count +=1
          p1 = player(i,ii,iii,iv,v,vi)
          st.write(p1.printPlayerData())
          pdata1 = [p1.playerName,p1.playerNumber,p1.playerSalaryPerWeek,p1.playerSigningDate,p1.playerContractDurationInYears,p1.playerNumberOfMatchesPlayed,p1.calcSalaryPerYear(),p1.calcRemainingDuration()]
          st.session_state.set.append(pdata1)

set = st.button('Setting',on_click=callbackf) #(returns true/false)

df = pd.DataFrame(st.session_state.set, columns = ['Name', 'Number','Salary/Week','Signing Date', 'Contract Duration / Years','Number Of Matches Played','Salary / Year','Remaining Duration/Weeks'])
st.table(df.head(st.session_state.count))
# st.dataframe(df)
# st.write('set = ', st.session_state.set)
# st.write('count = ', st.session_state.count)