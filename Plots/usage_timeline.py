#!/usr/bin/env python
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np
import readFolder_demo as readFolder
from datetime import datetime

# Fixing random state for reproducibility
np.random.seed(19680801)

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

	fig = plt.figure()
	plt.bar(date,count)

	plt.show()
	return fig

if __name__ == "__main__":
	data = readFolder.Facebook('/Users/christinebreckenridge/Downloads/facebook-christinebreckenridge')
	fig = plot(data)