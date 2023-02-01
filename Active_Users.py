# Libraries
import streamlit as st
from PIL import Image


# Layout
st.set_page_config(page_title='Back to Basic-Active Users',
                   page_icon=':bar_chart:', layout='wide')
st.title('Back to Basic Active Users')

# Content
c1, c2 = st.columns(2)
c2.image(Image.open('Images/Active_Users3.jpg'), width=450)
with c1:
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")

    st.write(""" # 🌔Terra Active Users  """)


st.write("""
 ### What Is Terra?
Terra is an open-source blockchain payment platform for an algorithmic stablecoin, which are cryptocurrencies that automatically track the price of currencies or other assets. The Terra blockchain enables users to instantly spend, save, trade, or exchange Terra stablecoins.  
The Terra protocol creates stablecoins designed to consistently track the price of a fiat currency (a government-backed currency such as the U.S. dollar or euro). It consists of two cryptocurrency tokens—Terra and Luna.
### What is an active user? ###
An active user is a user who engages with an app within a given period of time. This metric gives app developers and marketers valuable insight into their app’s growth, engagement, and stickiness.
### What are the most commonly used measurement periods for an active user? ###
There are three commonly used active user definitions:

* Daily active user (DAU): A daily active user is someone who interacts with an app on a specific day   
* Weekly active user (WAU): A weekly active user is someone who interacts with an app over a period of seven days   
* Monthly active user (MAU): A monthly active user is someone who interacts with an app over a period of 30 days   
The usefulness of each measurement period depends on an app’s vertical. While it’s beneficial to maintain a healthy number of daily active users, an app that is based on seasonal or occasional usage, such as a last-minute hotel booking app or a banking app, might place more emphasis on monthly active users. Monthly active users is an important metric for many businesses because it is another indication of whether their retention rate is healthy.
Daily active users and monthly active users are typically the most commonly used of the three metrics, and can be used to calculate an app’s “stickiness”. Stickiness measures how often users are returning to an app.
For example, if you have 500 monthly active users, and 50 of these users interact with the product every day, then your app has a stickiness of 10%. This means 10% of your daily active users are becoming monthly active users.  """)

st.image(Image.open('Images/Stickness.jpg'))

st.write("""
### What is the difference between users and active users? ###
During the selected period, active users are calculated by counting each user uniquely. So if a single user is active multiple times in a day, they'll count as one active user. However, an app will also have inactive, or churned, users who have installed the app but have not used it during the selected period. These users are therefore not counted as active users, but may use the app during a future period with the help of re-engagement campaigns.
### Why are active users important? ###
From a business perspective, active users are important because they have the potential to generate revenue. An app needs active users to survive, so a healthy count of active users is positive.
Calculating an app’s number of active users over a period of time can also help assess the effectiveness of marketing campaigns. Spikes in active user counts that correlate with a push notification on a particular day, or a weekly offer, can be analyzed against like-for-like campaigns to assess performance.
Knowing active user numbers is also essential in calculating key metrics. Figures like retention rate rely on finding out whether users remain active over a period of time, and metrics like lifetime value (LTV) can’t be calculated without retention.
In sum, active user counts act both as a way of checking on the general health of an app and as a first step to calculating deeper and more informative metrics further down the line. 

## Methodology ##
The question of “active wallets” faces every ecosystem. Let’s investigate this question for Terra — and go beyond the “one transaction in 30 days” approach!
Define what an active, high quality user looks like and how it can be measured. Assess how many active users exist on Terra, according to your definition. Additionally, provide a few brief, specific ideas to attract additional users, as well as an assessment of what it would cost to implement these ideas. What is the acquisition cost for a high-value user, according to your recommendations?
to asnwer these



 """)


st.write("""   
##### Sources #####   """)
st.write("""    1.https://www.investopedia.com/terra-5209502  
        2.https://www.adjust.com/glossary/active-user#what-are-the-most-commonly-used-measurement-periods-for-an-active-user   
        3.https://social.techcrunch.com/2022/05/12/    
        4.https://www.leewayhertz.com/exchange-vs-dex-vs-swap/  
        5.https://www.fool.com/investing/stock-market/market-sectors/financials/cryptocurrency-stocks/what-is-staking/  
        6.https://www.kaspersky.com/resource-center/definitions/what-is-an-nft  
        7.https://www.netservice.eu/en/research-and-development/crypto-voting  
        8.https://www.techtarget.com/searchsecurity/definition/crypto-wallet-cryptocurrency-wallet  
              """)
c1, c2 = st.columns(2)
with c2:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
with c1:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
