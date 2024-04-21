import streamlit as st
st.write('# Find the largest of the 3 numbers (TDS ASSG 8)')
number1= st.number_input('number 1')
number2 = st.number_input('number 2')
number3 = st.number_input('number 3')
num3 = max(number1,number2,number3)
st.write('# The greatest number is ',num3)
