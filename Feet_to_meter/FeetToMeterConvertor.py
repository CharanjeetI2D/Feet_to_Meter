import FreeSimpleGUI as sg
from ConvertorFunction import inches_to_meters

label1 = sg.Text("Enter Feel:")
input_box = sg.InputText(key='feet')

label2 = sg.Text("Enter inches")
input_box_2 = sg.InputText(key='inches')

convert_button = sg.Button("Convert")
result_label = sg.Text(key="output")

window = sg.Window(title='Convertor'
                   , layout=[[label1, input_box],
                             [label2, input_box_2],
                             [convert_button, result_label]])
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Convert":
        try:
            feet = float(values['feet'])
            inches = float(values['inches'])
            meters = inches_to_meters(feet, inches)
            window["output"].update(value=f"{meters:.2f} m")
        except ValueError:
            sg.popup_error("Please enter valid numbers for feet and inches")


window.close()
