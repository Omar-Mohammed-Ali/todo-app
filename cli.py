#from functions import get_todos, write_todos
import functions
import time
now = time.strftime("%m-%d-%Y %H:%M:%S")
print("It is",now)

while True:
    user_action = input("Type add,show,edit,complete or Exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo.capitalize() + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("New todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos,"todos.txt")
        except ValueError:
            print("your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")

            todos.pop(index)

            functions.write_todos(todos,"todos.txt")

            message = f"Todo {todo_to_remove} has been completed."
            print(message)
        except IndexError:
            print("there is not item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid command")

print("BYE!")





