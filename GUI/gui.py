#!/usr/bin/env python
import PySimpleGUI as sg
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

'''
    GUI window to select data folder
'''
def set_colors():
    sg.set_options(background_color='#3b5998',
        element_background_color='#3b5998',
        text_element_background_color='#3b5998')

def get_folder():
    # Get the folder containing the images from the user
    folder = sg.popup_get_folder('Data folder to open')
    while folder is None or folder == '':
        folder = sg.popup_get_folder('Please select a folder to open')
    return folder

info_icon = b'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'

def set_window_with_info():
    menu = [['File', ['Exit']], ['About', ['Privacy', 'Terms and Conditions']]]
    layout = [
        [sg.Menu(menu)],
        [sg.Text(' ', size=(75, 1)), sg.Button('', image_data=info_icon, button_color=(sg.theme_background_color(),sg.theme_background_color()), image_subsample=20, border_width=0, key='info')],
        [sg.Text('Personal-Data-Visualization-Tool', size=(30, 1), justification='center', font=("Helvetica", 30), relief=sg.RELIEF_RIDGE)],
        [sg.Text(' ', size=(15, 1)), sg.Input(), sg.FolderBrowse('Browse')],
        [sg.Text(' ', size=(15, 1)), sg.Submit('Go'), sg.Cancel('Exit')],
    ]

    window = sg.Window('Personal Data Visualization Tool', layout)
    return window

def set_window(title=''):
    # define menu layout
    menu = [['File', ['Open Folder', 'Exit']], ['About', ['Privacy', 'Terms and Conditions']]]
    buttons = [[
        sg.Button('Top 10 words',key='vis1',size=(25, 3)),
        sg.Button('Apps you use',key='vis2',size=(25, 3)),
        sg.Button('Quantity of data',key='vis3',size=(25, 3))],
        [sg.Button('Off FB Activites',key='vis4',size=(25, 3)),
        sg.Button('Account Activity Locations',key='vis5',size=(25, 3)),
        sg.Button('FaceBook Usage Over Time',key='vis6',size=(25,3))]]

    # define layout, show and read the window
    layout = [[sg.Menu(menu)], [sg.Col(buttons)]]
    window = sg.Window('Visualization Browser', layout, 
            return_keyboard_events=True,
            use_default_focus=False).Finalize()
    return window

def draw_figure(canvas, figure):
    if figure is None or canvas is None:
        return
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)

def show_vis(figure,window,desc=None,title='',toolbar=False):
    if figure is None:
        return
    window.close()
    if toolbar:
        if desc is not None:
            print("showing desc")
            layout = [
                [sg.Canvas(key='-TOOLBAR-')],
                [sg.Column(
                    layout=[
                        [sg.Canvas(key='-CANVAS-',
                                   # it's important that you set this size
                                   size=(640, 600)
                                   )]
                    ],
                    pad=(0, 0)
                )],
                [sg.Text(desc, size=(100, 10))],
                [sg.Button('Back', size=(10, 2), pad=((280, 0), 3), font='Helvetica 14')]
            ]
            new_window = sg.Window(title, layout, finalize=True)
            canvas_elem = new_window['-CANVAS-']
            canvas = canvas_elem.TKCanvas
            toolbar_canvas_elem = new_window['-TOOLBAR-']
            toolbar_canvas = toolbar_canvas_elem.TKCanvas

            draw_figure_w_toolbar(canvas,figure,toolbar_canvas)
        else:
            layout = [
                [sg.Canvas(key='-TOOLBAR-')],
                [sg.Column(
                    layout=[
                        [sg.Canvas(key='-CANVAS-',
                                   # it's important that you set this size
                                   size=(640, 600)
                                   )]
                    ],
                    pad=(0, 0)
                )],
                [sg.Button('Back', size=(10, 2), pad=((280, 0), 3), font='Helvetica 14')]
            ]
            new_window = sg.Window(title, layout, finalize=True)
            canvas_elem = new_window['-CANVAS-']
            canvas = canvas_elem.TKCanvas
            toolbar_canvas_elem = new_window['-TOOLBAR-']
            toolbar_canvas = toolbar_canvas_elem.TKCanvas

            draw_figure_w_toolbar(canvas,figure,toolbar_canvas)

    else:
        if desc is not None:
            layout = [[sg.Canvas(size=(640, 480), key='-CANVAS-')],
                      [sg.Text(desc, size=(100, 10))],
                      [sg.Button('Back', size=(10, 2), pad=((280, 0), 3), font='Helvetica 14')]]

            new_window = sg.Window(title, layout, finalize=True)

            canvas_elem = new_window['-CANVAS-']
            canvas = canvas_elem.TKCanvas
            draw_figure(canvas,figure)
        else:
            layout = [[sg.Canvas(size=(640, 480), key='-CANVAS-')],
                      [sg.Button('Back', size=(10, 2), pad=((280, 0), 3), font='Helvetica 14')]]

            new_window = sg.Window(title, layout, finalize=True)

            canvas_elem = new_window['-CANVAS-']
            canvas = canvas_elem.TKCanvas
            draw_figure(canvas,figure)
    return new_window, window

def show_vis_list(listbox_values,window,desc=None,title=''):
    window.close()
    figure_w, figure_h = 640, 480

    if desc is not None:
        col_listbox = [[sg.Listbox(values=listbox_values, change_submits=True, size=(28, 30), key='-LISTBOX-')],
               [sg.Button('Back', size=(10, 2), font='Helvetica 14')]]
    else:
        col_listbox = [[sg.Listbox(values=listbox_values, change_submits=True, size=(28, 30), key='-LISTBOX-')],
               [sg.Button('Back', size=(10, 2), font='Helvetica 14')]]

    col_multiline = sg.Col([[sg.MLine(size=(70, 35), key='-MULTILINE-')]])
    col_canvas = sg.Col([[sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-')]])
    col_instructions = sg.Col([[sg.Pane([col_canvas, col_multiline], size=(650, 425))],[sg.Text(desc, size=(100, 10))]])

    layout = [[sg.Text('Interactions List', font=('ANY 18'))],
          [sg.Col(col_listbox), col_instructions]]

    new_window = sg.Window('Your Off Facebook Activity Timeline',
                   layout, resizable=True, finalize=True)
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
        elif event == 'vis3':
            #show vis3 func call
            continue
        elif event == 'vis4':
            #show vis4 func call
            continue
        elif event == 'vis5':
            #show vis5 func call
            continue
        elif event == 'vis6':
            #show vis6 func call
            continue

    window.close()

if __name__ == '__main__':
    main()
