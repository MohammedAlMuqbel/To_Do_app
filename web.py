import streamlit as st
import functions

to_do=functions.get_to_do()

st.title("To_do List")
st.subheader("Add your Tasks daily")
st.write("To increase your productivity")

for todo in to_do:
    st.checkbox(todo)


st.text_input(label="",placeholder="Add a new task")
