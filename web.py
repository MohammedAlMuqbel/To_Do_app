import functions
import streamlit as st


to_do=functions.get_to_do()


def add_todo():
    todos=st.session_state["add"]+"\n"
    to_do.append(todos)
    functions.write_to_do(to_do)


st.title("To_do List")
st.subheader("Add your Tasks daily")
st.write("To increase your productivity")

for index,todo in enumerate(to_do):
    check=st.checkbox(todo,key=todo)
    if check:
        to_do.pop(index)
        functions.write_to_do(to_do)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="",placeholder="Add a new task"
              ,on_change=add_todo,key="add")

