def get_todos():
    with open('todoslist.txt', "r") as file:
        todos_loc = file.readlines()
    return todos_loc

def write_todos(todos):
    with open('todoslist.txt', "w") as file:
        file.writelines(todos)