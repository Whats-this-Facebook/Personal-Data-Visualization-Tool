#!/usr/bin/env python
import PySimpleGUI as sg
import os

'''
    Simple Image Viewer
'''


def main():

    png_file = "cat.png"


    # define menu layout
    menu = [['File', ['Open Folder', 'Exit']], ['Help', ['About', ]]]

    # define layout, show and read the window
    col = [[sg.Text(png_file, size=(80, 3), key='filename')],
           [sg.Image(filename=png_file, key='image')]]

    layout = [[sg.Menu(menu)], [sg.Col(col)]]
    window = sg.Window('Image Browser', layout,
            return_keyboard_events=True,
            location=(0, 0),
            use_default_focus=False)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        # ----------------- Menu choices -----------------

        # update window with new image
        window['image'].update(filename=png_file)
        # update window with filename
        window['filename'].update(png_file)
        # update page display

    window.close()

if __name__ == '__main__':
    main()