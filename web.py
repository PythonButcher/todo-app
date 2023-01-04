import streamlit as st
import st_functions

todos = st_functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    st_functions.write_todos(todos)


st.title("My Todo App")
st.write("An app to track your honey-do list")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        st_functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a todo:", placeholder="Add a new todo...",
on_change=add_todo, key='new_todo')