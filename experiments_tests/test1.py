import PySimpleGUI as sg

feet = sg.Text("Enter feet")
input_feet = sg.InputText()
inches = sg.Text("Enter inches")
input_inches = sg.InputText()

convert_button = sg.Button("convert")

window = sg.Window('Converter', layout = [[feet,input_feet],
                                          [inches, input_inches],
                                          [convert_button]])
window.read()
window.close()