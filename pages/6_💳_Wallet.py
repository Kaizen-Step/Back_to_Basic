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
st.set_page_config(page_title='Wallets - Terra Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('💳Wallets')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'New_and_Active_Wallets':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e9e0c78c-0d63-44a8-aab1-4dcc5216891b/data/latest')
    elif query == 'Richest_users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/60f07d44-b578-44ee-9cdb-7372b3029adf/data/latest')
    return None


New_and_Active_Wallets = get_data('New_and_Active_Wallets')
Richest_users = get_data('Richest_users')

df = New_and_Active_Wallets
df2 = Richest_users

st.write(""" ### Wallet in Cryptocurrency """)

st.write(""" A crypto wallet is software or hardware that enables users to store and use cryptocurrency. A crypto wallet enables users to both send and receive cryptocurrency transactions, in an approach that is similar in concept to how a traditional bank account enables users to conduct transactions.[[8]](https://www.fool.com/investing/stock-market/market-sectors/financials/cryptocurrency-stocks/what-is-staking/)      
  
In this Stake Section you can find:
* A  
* b  
* C 
* d  
     """)

st.write(""" ### Finding From This Section ##

* A   
* B  
* C  
* D  


 """)


#################################

# Top 20 Richest users and Number of Their Transactions
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["USER"], y=df2["BALANCE"],
                     name="BALANCE".title()), secondary_y=False)
fig.add_trace(go.Line(x=df2["USER"], y=df2["Number of transactions"],
                      name="Number of transactions"), secondary_y=True)
fig.update_layout(
    title_text='Top 20 Richest users and Number of Their Transactions')
fig.update_yaxes(
    title_text="BALANCE".title(), secondary_y=False)
fig.update_yaxes(title_text="Number of transactions", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Total Number of Active Wallets Per Week With Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df['ACTIVE_WALLETS'],
                     name='Number of ACTIVE WALLETS'), secondary_y=False)
fig.add_trace(go.Line(x=df['WEEK'], y=df['CUMULATIVE_ACTIVE_WALLET'],
                      name='CUMULATIVE ACTIVE WALLET'), secondary_y=True)
fig.update_layout(
    title_text='Total Number of Active Wallets Per Week With Cumulative Value')
fig.update_yaxes(
    title_text='Number of ACTIVE WALLETS', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Number', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Total Number of New Wallets Per Week With Cumulative Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df['NEW_WALLETS'],
                     name='NEW WALLETS'), secondary_y=False)
fig.add_trace(go.Line(x=df['WEEK'], y=df['CUMULATIVE_NEW_WALLET'],
                      name='CUMULATIVE NEW WALLET'), secondary_y=True)
fig.update_layout(
    title_text='Total Number of New Wallets Per Week With Cumulative Number')
fig.update_yaxes(
    title_text='Number of NEW WALLETS', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Number', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
