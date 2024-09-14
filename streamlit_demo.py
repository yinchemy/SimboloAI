import streamlit as st

st.text("This is my first streamlit deployment")

number = st.number_input(
    "Insert a number", value=None, placeholder="Type a number..."
)
st.write("The number is ", number)

