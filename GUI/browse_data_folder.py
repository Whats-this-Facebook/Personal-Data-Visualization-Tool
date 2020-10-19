#!/usr/bin/env python
import PySimpleGUI as sg
import os

'''
    GUI window to select data folder
'''


def main():

    sg.set_options(background_color='#3b5998')

    # Get the folder containing the images from the user
    folder = sg.popup_get_folder('Data folder to open')
    if folder is None:
        sg.popup_cancel('Cancelling')
        return

    # get JSON data
    # insert func call here

    # define menu layout
    menu = [['File', ['Open Folder', 'Exit']], ['Help', ['About', ]]]
    buttons = [[sg.Button('Vis1'),sg.Button('Vis2')]]

    # define layout, show and read the window
    col = [[sg.Text("Visualization buttons here", size=(80, 3), key='filename')]]

    layout = [[sg.Menu(menu)], [sg.Col(buttons)]]
    window = sg.Window('Visualization Browser', layout,
            return_keyboard_events=True,
            location=(0, 0),
            use_default_focus=False)

    # loop reading the user input and displaying image, filename
    i = 0
    while True:

        event, values = window.read()
        # --------------------- Button & Keyboard ---------------------
        if event == sg.WIN_CLOSED:
            break

        # ----------------- Menu choices -----------------
        if event == 'Open Folder':
            newfolder = sg.popup_get_folder('New folder', no_window=True)
            if newfolder is None:
                continue

            folder = newfolder
            window.refresh()

            i = 0
        elif event == 'About':
            sg.popup('Personal Data Visualization Tool',
                     'Insert info here')

    window.close()

if __name__ == '__main__':
    main()