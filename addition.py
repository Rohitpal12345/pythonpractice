#using strealit library calculate sum of two number

import streamlit as st
st.set_page_config(page_title="number addition",page_icon="➕add",layout="centered")
st.title("Addition of Two Number 'today discuss stramlit library'")
st.caption("enter two number and it will return addition of them")
form=st.form("add_form")
num1=form.number_input("first number")
num2=form.number_input("second number")

submitted=form.form_submit_button("calculate")
if submitted:
    result=num1+num2
    st.divider()
  
    st.metric(label="Result",value=result)

    # number print 1 to 10
    for i in range(1,11):
        st.write(i)


