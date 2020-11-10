#!/usr/bin/env python

import pytest
import Plots.usage_timeline as timeline
import matplotlib.pyplot as plt
import CLI.readFolder as readFolder

@pytest.fixture

def test_plot():
	data = readFolder.Facebook('~/Downloads/facebook-christinebreckenridge')
	fig = timeline.plot(data)
	assert fig != None

