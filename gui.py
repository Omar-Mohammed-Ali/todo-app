import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a TODO")
input_box = sg.InputText(tooltip="Enter a TODO")
add_button = sg.Button("Add")

window = sg.Window("My TODOS App", layout=[[label],[input_box, add_button]])

window.read()
window.close()