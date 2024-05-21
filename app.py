import pickle
import streamlit as st
import pandas as pd

pipe = pickle.load(open('pipe1.pkl','rb'))

st.write('## Diagnosis System for Parkinson’s Disease ##')

st.image('img.jpg')
#st.write('# ______________________________ #')
#pipe.predict()
st.sidebar.write('Diagnosis System Form')
Jitter = st.sidebar.number_input('Enetr Jitter in DDP')
NHR = st.sidebar.number_input('Enter NHR')
HNR = st.sidebar.number_input('Enter HNR')
RPDE = st.sidebar.number_input('Enter RPDE')
DFA = st.sidebar.number_input('Enter DFA')
D2 = st.sidebar.number_input('Enter D2')
PPE = st.sidebar.number_input('Enter PPE')

input_data = pd.DataFrame([[Jitter, NHR, HNR, RPDE, DFA, D2, PPE]],columns=['Jitter:DDP','NHR','HNR','RPDE','DFA','D2','PPE'])
res = -1
res = pipe.predict(input_data)
if Jitter !=0 or NHR !=0 or HNR !=0 or RPDE !=0 or DFA !=0 or D2 !=0 or PPE !=0 :
    if res == 1 or res == 0:
        if res == 1:
            st.write("# You are effected by PARKINSON #")
        else:
            st.write('# You are not effected by PARKINSON #')


#st.sidebar.slider('')