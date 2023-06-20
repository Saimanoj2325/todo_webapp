import streamlit as st
import functions1 as f

todos = f.get_todos()
def add_todo():
     todo = st.session_state["new_todo"] + "\n"
     todos.append(todo)
     f.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This is to Increase your productivity")
for i,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=f"todo{i}")
    if checkbox:
        todos.pop(i)
        f.write_todos(todos)
        del st.session_state[f"todo{i}"]
        st.experimental_rerun()


st.text_input(label="Enter a todo:",placeholder="Add new todo..",
              on_change=add_todo,key="new_todo")
