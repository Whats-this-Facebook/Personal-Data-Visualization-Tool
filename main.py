#!/usr/bin/env python
import GUI.gui as gui
import Plots.wordCounter as wordCounter
import CLI.comments_demo as comments
import matplotlib.pyplot as plt

def main():
    gui.set_colors()

    path = gui.get_folder()

    gui.set_window()

    comments_string = comments.getAllComments(path)

    figure = wordCounter.freqWords2Barchart(comments_string)
    plt.show()

if __name__ == "__main__":
    main()