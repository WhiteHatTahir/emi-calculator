import streamlit as st
def calculate_emi(p,n,r):
    emi = p*(r/100)*(1+r/100)**n/((1+r/100)**n-1)
    st.write('emi calculated:',round(emi,3))

def calculate_outstanding_balance(p,n,r,m):
    balance =(p*((1+r/100)** n -(1+r/100)**m))/((1+r/100)**n-1)
    st.write('outstanding loan balace calculated:',round(balance,3))
    
st.title('emi calculator')
principal = st.slider('loan amount',1000.0,100000.0)
tenure = st.slider('tenure in years',1,30)
roi =  st.slider('interest rate',1,15)
period = st.slider('period in months',1,tenure*12)

n = tenure * 12
r = roi/12
emi_button = st.button('calculate emi')
balance_button = st.button('calculate outstanding loan balance')
if emi_button:
   calculate_emi(principal,n,r)
elif balance_button:
     calculate_outstanding_balance(principal,n,r,period)