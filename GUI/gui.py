#!/usr/bin/env python
import PySimpleGUI as sg
import os

'''
    GUI window to select data folder
'''
def set_colors():
    sg.set_options(background_color='#3b5998')

def get_folder():
    # Get the folder containing the images from the user
    folder = sg.popup_get_folder('Data folder to open')
    while folder is None or folder == '':
        folder = sg.popup_get_folder('Please select a folder to open')
    return folder

def set_window():
    # define menu layout
    menu = [['File', ['Open Folder', 'Exit']], ['Help', ['About', ]]]
    buttons = [[sg.Button('Vis1',key='vis1',size=(20, 3)),sg.Button('Vis2',key='vis2',size=(20, 3))]]

    # define layout, show and read the window
    layout = [[sg.Menu(menu)], [sg.Col(buttons)]]
    window = sg.Window('Visualization Browser', layout,
            return_keyboard_events=True,
            location=(0, 0),
            use_default_focus=False)

def main():

    set_colors()

    get_folder()

    set_window()

    # loop reading the user input
    i = 0
    while True:
        if folder is None or folder == '':
            folder = sg.popup_get_folder('Please select a folder to open')
        
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
        elif event == 'vis1':
            #show vis1 func call
            continue
        elif event == 'vis2':
            #show vis2 func call
            continue

    window.close()

if __name__ == '__main__':
    main()