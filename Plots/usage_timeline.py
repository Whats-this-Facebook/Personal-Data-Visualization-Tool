#!/usr/bin/env python
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np
import CLI.readFolder as readFolder
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import PySimpleGUI as sg
import numpy as np



def get_comment_dates(FB):
	comments = FB.comments()
	dates = [datetime.fromtimestamp(i['timestamp']).isoformat() for i in comments]
	dates = [datetime.strptime(i[:10], "%Y-%m-%d") for i in dates]
	return dates


def plot(FB):
	dates = get_comment_dates(FB)
	count = []
	date = []
	for el in dates:
		date.append(el)
		count.append(dates.count(el))

	fig, ax = plt.subplots()
	plt.bar(date,count)
	ax.yaxis.get_major_locator().set_params(integer=True)
	ax.set_ylim(ymin=0, ymax=None)

	# plt.show()
	return fig

"""
	Embedding the Matplotlib toolbar into your application

"""

# ------------------------------- This is to include a matplotlib figure in a Tkinter canvas


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


if __name__ == "__main__":


	# ------------------------------- PySimpleGUI CODE

	layout = [
		[sg.Canvas(key='controls_cv')],
		[sg.Column(
			layout=[
				[sg.Canvas(key='fig_cv',
						   # it's important that you set this size
						   size=(400 * 2, 400)
						   )]
			],
			background_color='#DAE0E6',
			pad=(0, 0)
		)],
		[sg.B('Back')]
	]

	window = sg.Window('Graph with controls', layout, finalize=True)
	data = readFolder.Facebook('/Users/christinebreckenridge/Downloads/facebook-christinebreckenridge')
	fig = plot(data)
	DPI = fig.get_dpi()
	fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
	draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)

	while True:
		event, values = window.read()
		print(event, values)
		if event in (sg.WIN_CLOSED, 'Exit'):  # always,  always give a way out!
			break

	window.close()
