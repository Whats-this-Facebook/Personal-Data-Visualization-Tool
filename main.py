#!/usr/bin/env python
import GUI.gui as gui
import Plots.wordCounter as wordCounter
import CLI.comments_demo as comments
import matplotlib.pyplot as plt
import PySimpleGUI as sg


def main():
    gui.set_colors()

    path = gui.get_folder()

    window = gui.set_window()

    comments_string = comments.getAllComments(path)


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'vis1':
            figure = wordCounter.freqWords2Barchart(comments_string)
            gui.show_vis(figure,"10 most frequent words")


if __name__ == "__main__":
    main()