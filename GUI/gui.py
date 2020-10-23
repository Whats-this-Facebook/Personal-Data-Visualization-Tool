#!/usr/bin/env python
import PySimpleGUI as sg
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

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

def set_window(title=''):
    # define menu layout
    menu = [['File', ['Open Folder', 'Exit']], ['Help', ['About', ]]]
    buttons = [[sg.Button('Vis1',key='vis1',size=(20, 3)),sg.Button('Vis2',key='vis2',size=(20, 3))]]

    # define layout, show and read the window
    layout = [[sg.Menu(menu)], [sg.Col(buttons)]]
    window = sg.Window('Visualization Browser', layout,
            return_keyboard_events=True,
            location=(0, 0),
            use_default_focus=False)
    return window

def draw_figure(canvas, figure):
    if figure is None or canvas is None:
        return
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def show_vis(figure,window,title=''):
    if figure is None:
        return
    window.close()
    layout = [[sg.Text(title, size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Canvas(size=(640, 480), key='-CANVAS-')],
              [sg.Button('Back', size=(10, 2), pad=((280, 0), 3), font='Helvetica 14')]]
    
    new_window = sg.Window(title, layout, finalize=True)

    canvas_elem = new_window['-CANVAS-']
    canvas = canvas_elem.TKCanvas
    draw_figure(canvas,figure)
    return new_window, window

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