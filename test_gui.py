#!/usr/bin/env python
import pytest
import GUI.gui as gui
import matplotlib.pyplot as plt

@pytest.fixture

def test_get_folder():
	folder = gui.get_folder()
	assert folder != None

def test_set_window():
	window = gui.set_window()
	assert window != None

def test_draw_figure_none():
	fig = gui.draw_figure(None,None)
	assert fig == None

def test_draw_figure():
	figure, ax = plt.subplots()
	window = gui.set_window()
	canvas = window['-CANVAS-'].TKCanvas
	fig = gui.draw_figure(canvas,figure)
	assert fig != None

