import functions
import PySimpleGUI
import time
import os

if not os.path.exists("Data.txt"):
    with open ("Data.txt","w") as file:
        pass

PySimpleGUI.theme("LightBrown1")
clock=PySimpleGUI.Text('',key="Clock")
label=PySimpleGUI.Text("Please Add a Task")
input_box=PySimpleGUI.InputText(tooltip="Enter a Task",key="To_do")
add_button=PySimpleGUI.Button("Add",size=10)
list_box=PySimpleGUI.Listbox(values=functions.get_to_do(),key='item',
                             enable_events=True,size=[45,10])
edit_button=PySimpleGUI.Button("Edit")
complete_button=PySimpleGUI.Button("Complete")
exit_button=PySimpleGUI.Button("Exit")

window=PySimpleGUI.Window('To_do_list'
                          ,layout=[[clock],
                                   [label],[input_box,add_button],
                                   [list_box,edit_button,complete_button],
                                   [exit_button]],
                          font=('Helvetica',15))

while True:
    event,values=window.read(timeout=10)
    window["Clock"].update(value=time.strftime("%b-%d,%Y,%H:%M:%S"))

    match event:
        case "Add":
            to_do=functions.get_to_do()
            new_to_do=values["To_do"]+"\n"
            to_do.append(new_to_do)
            functions.write_to_do(to_do)
            window['item'].update(values=to_do)

        case "Edit":
            try:
                todo_edit=values["item"][0]
                new_todo=values["To_do"]
                get_to_do=functions.get_to_do()
                index=get_to_do.index(todo_edit)
                get_to_do[index]=new_todo
                functions.write_to_do(get_to_do)
                window['item'].update(values=get_to_do)
            except IndexError:
                PySimpleGUI.popup("please select a task first",font=("Helvetica",15))

        case "Complete":
            try:
                to_do_complete=values["item"][0]
                todos=functions.get_to_do()
                todos.remove(to_do_complete)
                functions.write_to_do(todos)
                window["item"].update(values=todos)
                window["To_do"].update(value='')
            except IndexError:
                PySimpleGUI.popup("please select a task first",font=("Helvetica",15))

        case"Exit":
            break
        case "item":
            window["To_do"].update(value=values["item"][0])

        case PySimpleGUI.WIN_CLOSED:
            break

window.close()

