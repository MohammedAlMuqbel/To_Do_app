import functions
import PySimpleGUI

label=PySimpleGUI.Text("Please Add a Task")
input_box=PySimpleGUI.InputText(tooltip="Enter a Task",key="To_do")
add_button=PySimpleGUI.Button("Add")
list_box=PySimpleGUI.Listbox(values=functions.get_to_do(),key='item',
                             enable_events=True,size=[45,10])
edit_button=PySimpleGUI.Button("Edit")

window=PySimpleGUI.Window('To_do_list'
                          ,layout=[[label],[input_box,add_button],[list_box,edit_button]],
                          font=('Helvetica',15))

while True:
    event,values=window.read()
    print(1,event)
    print(2,values)
    match event:
        case "Add":
            to_do=functions.get_to_do()
            new_to_do=values["To_do"]+"\n"
            to_do.append(new_to_do)
            functions.write_to_do(to_do)
            window['item'].update(values=to_do)


        case "Edit":
            todo_edit=values["item"][0]
            new_todo=values["To_do"]
            get_to_do=functions.get_to_do()
            index=get_to_do.index(todo_edit)
            get_to_do[index]=new_todo
            functions.write_to_do(get_to_do)
            window['item'].update(values=get_to_do)

        case "item":
            window["To_do"].update(value=values["item"][0])

        case PySimpleGUI.WIN_CLOSED:
            break

window.close()

