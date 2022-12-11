import functions
import PySimpleGUI

label=PySimpleGUI.Text("Please Add a Task")
input_box=PySimpleGUI.InputText(tooltip="Enter a Task")
add_button=PySimpleGUI.Button("Add")


window=PySimpleGUI.Window('To_do_list',layout=[[label,input_box,add_button]])
window.read()
window.close()

