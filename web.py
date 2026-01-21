import streamlit as st
import functions


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


todos = functions.get_todos()
st.title("My Todo App")
st.subheader("This is my todo app")

for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ",placeholder="Add new todo...",
              on_change=add_todo,key="new_todo")

st.session_state