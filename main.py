#!/usr/bin/env python
import GUI.gui as gui
import Plots.wordCounter as wordCounter
import Plots.appsUsed as appsUsed
import CLI.comments_demo as comments
import CLI.readFolder_demo as readFolder_demo
import matplotlib.pyplot as plt
import PySimpleGUI as sg


def main():
    gui.set_colors()

    path = gui.get_folder()

    window = gui.set_window()

    data = readFolder_demo.Facebook(path)
    comments = data.comments()
    comments_string = readFolder_demo.comments_str(comments)


    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'vis1':
            figure = wordCounter.freqWords2Barchart(comments_string)
            vis_window, window = gui.show_vis(figure,window)

            while True:
                vis_event, vis_values = vis_window.read()
                if vis_event == sg.WIN_CLOSED:
                    break
                elif vis_event == 'Back':
                    window = gui.set_window()
                    vis_window.close()
                    break
        elif event == 'vis2':
            figure = appsUsed.plotApps(path)
            vis_window, window = gui.show_vis(figure,window)

            while True:
                vis_event, vis_values = vis_window.read()
                if vis_event == sg.WIN_CLOSED:
                    break
                elif vis_event == 'Back':
                    window = gui.set_window()
                    vis_window.close()
                    break


if __name__ == "__main__":
    main()