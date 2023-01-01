import PySimpleGUI as sg
import os


def edit_rules(xml_file):
    layout = [
        [sg.Text("Edit Rules")],
        [
            sg.Multiline(
                default_text=open(xml_file, "r").read(),
                size=(100, 50),
                key="-RULES-",
                font=("Arial", 10),
            )
        ],
        [sg.Push(), sg.Button("Save", key="-SAVE-")],
    ]

    window = sg.Window("Edit Rules", layout, finalize=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "-SAVE-":
            with open(xml_file, "w") as f:
                f.write(values["-RULES-"])
            window.close()
            sg.popup("Saved")
            break


def main():
    main_layout = [
        [sg.Button("Start", key="-START-", font=("Arial", 20))],
        [sg.Button("Edit Rules", key="-EDIT-", font=("Arial", 20))],
    ]

    window = sg.Window("Main Menu", main_layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "-START-":
            curr = os.getcwd()
            os.chdir(curr)
            os.system("python Main.py")

        elif event == "-EDIT-":
            xml_file = sg.popup_get_file(
                "Select XML file",
                file_types=(("XML Files", "*.xml")),
                font=("Arial", 20),
            )
            edit_rules(xml_file)


main()
