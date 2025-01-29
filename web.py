import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state['new_todo'] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("My To-do App")
st.subheader("This my to-do app")
st.write("This app is to increase your productivity.")

#I used index to avoid unique key error and enumerate
# to avoid value error in the below for loop
for index, todo in enumerate(todos):
    checkbox_key = f"checkbox_{index}"
    checkbox = st.checkbox(todo, key=checkbox_key)
    #updated index to checkbox_key to avoid error with locating the
    #to-do on st.session_state
    if checkbox:
        todos.pop(index)
        del st.session_state[checkbox_key]
        functions.write_todos(todos)
        st.rerun()

st.text_input(label="Enter a to-do:", placeholder="Add a new to-do...",
              on_change=add_todo, key='new_todo')
