# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Swap - Back to Basic: Active USers',
                   page_icon=':bar_chart:', layout='wide')
st.title('🌌Swap')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.write(""" ### Swaping Concept   
 Swap facilitates the instant exchange of two non-native tokens between two unique blockchain protocols without the need of commencing the traditional crypto-to-fiat exchange or token migration. It allows users to swap tokens directly from the official private key wallet or the trading account.[[4]](https://www.leewayhertz.com/exchange-vs-dex-vs-swap/)    
""")

st.info(""" 
In this Swap Section you can find:
* A  
* b  
* C 
* d  
     """)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Transactions Weekly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2ece64b2-f7af-46e2-9da7-44c350eb0352/data/latest')
    elif query == 'Luna Daily Transaction':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b08821ca-c8fb-4db0-b95f-4dd0d25df9b9/data/latest')
    elif query == 'TX_Num_Overtime':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4e1c9246-a508-475f-9048-8abba7eb96d7/data/latest')
    elif query == 'Terra_Transactions_Intervals':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/22fab0e2-89d7-4f75-a2d1-d96c5dc017d1/data/latest')
    return None


transactions_weekly = get_data('Transactions Weekly')
Luna_daily_tx_vol = get_data('Luna Daily Transaction')
TX_Num_Overtime = get_data('TX_Num_Overtime')
Terra_Transactions_Intervals = get_data('Terra_Transactions_Intervals')


df = transactions_weekly
df2 = Luna_daily_tx_vol
df3 = TX_Num_Overtime
df4 = Terra_Transactions_Intervals


st.write(""" ### Finding From This Section ##

* A   
* B  
* C  
* D  


 """)
