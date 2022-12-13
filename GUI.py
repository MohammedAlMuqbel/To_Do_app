import functions
import PySimpleGUI

label=PySimpleGUI.Text("Please Add a Task")
input_box=PySimpleGUI.InputText(tooltip="Enter a Task",key="To_do")
add_button=PySimpleGUI.Button("Add")


window=PySimpleGUI.Window('To_do_list'
                          ,layout=[[label,input_box,add_button]],
                          font=('Helvetica',15))

while True:
    event,values=window.read()
    match event:
        case "Add":
            to_do=functions.get_to_do()
            new_to_do=values["To_do"]+"\n"
            to_do.append(new_to_do)
            functions.write_to_do(to_do)

        case PySimpleGUI.WIN_CLOSED:
            break

window.close()

