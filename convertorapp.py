import PySimpleGUI as sg

layout = [
    [sg.Input(key="-INPUT-"),
     sg.Spin(["km to miles", "kg to pound", "sec to min"], key="-UNITS-"),
     sg.Button('Convert', key="-BUTTON-")],
    [sg.Text('Output', key="-OUTPUT-")],

]

window = sg.Window('Convertor', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "-BUTTON-":
        input_values = values["-INPUT-"]
        if input_values.isnumeric():
            if values["-UNITS-"] == "km to miles":
                output = round(float(input_values) * 0.6214, 2)
                output_string = f'{input_values} km = {output} miles'
                window["-OUTPUT-"].update(output_string)
            elif values["-UNITS-"] == "kg to pound":
                output = round(float(input_values) * 2.20462, 2)
                output_string = f'{input_values} kg = {output} pounds'
                window["-OUTPUT-"].update(output_string)
            elif values["-UNITS-"] == "sec to min":
                output = round(float(input_values) / 60, 2)
                output_string = f'{input_values} sec = {output} mins'
                window["-OUTPUT-"].update(output_string)
            else:
                invalid_output = "Your input is invalid, enter only numbers"
                window["-OUTPUT-"].update(invalid_output)

window.close()
