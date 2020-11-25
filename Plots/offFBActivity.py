import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import argparse
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def draw_figure(canvas, figure):
    """
    Combines the tkinter and pyplot using Canvas Widget
    """
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def delete_figure_agg(figure_agg):
    """
    Cleans the target figure so that another can be drawn
    """
    figure_agg.get_tk_widget().forget()
    plt.close('all')


# I shouldnt have two return here
def chooseActivity(activityList, activity_name):
    for activity in activityList:
        if activity['name'] == activity_name:
            return activity

    return None

    
def plotActivities(FB,choice):
    #FB = readFolder_demo.Facebook(path)
    names, dates = getActivities(FB,choice)
    return plotTimeline(names,dates)


def getActivities(FB,choice):
    activities = FB.offFB_activities()
    app_activities = chooseActivity(activities, choice)
    names = [i['type'] for i in app_activities['events']]
    dates = [datetime.fromtimestamp(i['timestamp']).isoformat() for i in app_activities['events']]
    dates = [datetime.strptime(i[:10], "%Y-%m-%d") for i in dates]
    return names, dates


def getActivityPlotInfo(app_activities):
    names = [i['type'] for i in app_activities['events']]
    dates = [datetime.fromtimestamp(i['timestamp']).isoformat() for i in app_activities['events']]
    dates = [datetime.strptime(i[:10], "%Y-%m-%d") for i in dates]
    return names, dates


def getAppPlotInfo(app_activities):
    names = []
    dates = []
    for act in app_activities['events']:
        names.append(act['type'])
        date = datetime.fromtimestamp(act['timestamp']).isoformat()
        dates.append(datetime.strptime(date[:10], "%Y-%m-%d"))
    return names, dates


def getEventCount(names, dates, event):
    size = len(names)
    eventName = []
    eventDate = []
    for name, date in zip(names, dates):
        if name == event:
            eventName.append(name)
            eventDate.append(date)

    return eventName, eventDate


def plotTimeline(names, dates, timeline_name=''):

    #https://matplotlib.org/3.2.1/gallery/lines_bars_and_markers/timeline.html
    # Choose some nice levels
    levels = np.tile([-11,11,-9,9,-7, 7, -5, 5, -3, 3, -1, 1], int(np.ceil(len(dates)/6)))[:len(dates)]
    
    # Create figure and plot a stem plot with the date
    fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
    ax.set(title="Apps that facebook knows you've used")
    
    markerline, stemline, baseline = ax.stem(dates, levels,
                                             linefmt="#3B5998", basefmt="k-",
                                             use_line_collection=True)
    
    plt.setp(markerline, mec="k", mfc="w", zorder=3,color='#3B5998')
    
    # Shift the markers to the baseline by replacing the y-data by zeros.
    markerline.set_ydata(np.zeros(len(dates)))
    
    # annotate lines
    vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
    for d, l, r, va in zip(dates, levels, names, vert):
        ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l)*3),
                    textcoords="offset points", va=va, ha="right")
    
    # format xaxis with 4 month intervals
    ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=4))
    ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    
    # remove y axis and spines
    ax.get_yaxis().set_visible(False)
    for spine in ["left", "top", "right"]:
        ax.spines[spine].set_visible(False)
    
    ax.margins(y=0.1)
    if timeline_name == '':
        return fig
    else:
        plt.savefig(timeline_name + '.png')
    plt.clf()


def plotSubplots(activity):
    names, dates = getAppPlotInfo(activity)
    unique_events = set(names)
    unique_events = list(unique_events)
    num_unique_events = len(unique_events)
    # Create subplots
    fig, axesList = plt.subplots(num_unique_events, 1, sharex=True)
    axes_list = []
    if num_unique_events == 1:
        axes_list.append(axesList)
    else:
        axes_list = list(axesList)
    fig.tight_layout(h_pad=2)
    plt.subplots_adjust(top=0.9,left=0.15,bottom=0.2,right=0.9)

    for ax, event in zip(axes_list, unique_events):
        count = []
        date = []
        eNames, eDates = getEventCount(names, dates, event)
        for el in eDates:
            if el not in date:
                date.append(el) 
                count.append(eDates.count(el))

        ax.bar(date,count)
        ax.yaxis.get_major_locator().set_params(integer=True)
        ax.set_ylim(ymin=0, ymax=None)
        ax.set_title(event)
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    
    return fig


def getOffFBActivityFigures(FB):
    fig_dict = {} 
    activities = FB.offFB_activities()
    for activity in activities:
        choice = activity['name']
        fig_dict[choice] = plotSubplots(activity)
    
    return fig_dict