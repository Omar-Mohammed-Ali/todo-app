import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a TODO")
input_box = sg.InputText(tooltip="Enter a TODO",key="TODO")
add_button = sg.Button("Add")

window = sg.Window("My TODOS App",
                   layout=[[label],[input_box, add_button]],
                   font=("Helvetica", 15))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values["TODO"] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()