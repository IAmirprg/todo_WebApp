import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)


st.title("Todo App")

for index, item in enumerate(todos):
    check = st.checkbox(item, key=item)
    if check:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()


st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

