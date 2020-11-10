import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style as style
import matplotlib.dates as mdates
from datetime import datetime
import CLI.readFolder_demo as readFolder_demo
from matplotlib.colors import LinearSegmentedColormap


def findRepeatDates(dates,names):
    newDates, newNames = [], []
    for i,date in enumerate(dates):
        if(i != 0 and dates[i-1] == date):
            newNames[-1] = newNames[-1] + ' | ' + names[i]
        else:
            newNames.append(names[i])
            newDates.append(date)
    return newNames, newDates



def getApps(FB):
    apps = FB.apps()
    if apps == []:
        return None, None
    names = [i['name'] for i in apps]
    dates = [datetime.fromtimestamp(i['added_timestamp']).isoformat() for i in apps]
    dates = [datetime.strptime(i[:10], "%Y-%m-%d") for i in dates]
    return findRepeatDates(dates,names)

def plotTimeline(names, dates, timeline_name=''):
    """Generates timeline of of app names with their respective dates of installation.
    Names and dates must correspond to eachother via index. If no timeline_name is 
    specificied then this function returns the fig matplotlib object. Otherwise, it 
    saves .png file with the provided timeline name

    Args:
        names (list()): list of strings containing the names of all the apps
        dates ([type]): list of datetime objects that correspond to the installation
            of the apps in the names apps 
        timeline_name (str, optional): the name of the .png if you want
            to save it. Defaults to ''.

    Returns:
        if no timeline_name is passed then
            fig: the matplot lib fig object of the timeline
        else
            None
    """

    #https://matplotlib.org/3.2.1/gallery/lines_bars_and_markers/timeline.html
    # Choose some nice levels
    levels = np.tile([-11,11,-9,9,-7, 7, -5, 5, -3, 3, -1, 1],
                     int(np.ceil(len(dates)/6)))[:len(dates)]
    
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

def plotApps(path):
    """Plots apps you installed on a timeline. For apps installed on the
    the same day will show up as "app1 | app2 | app3 ...". Returns None if no
    apps were found.

    Args:
        path (string): path to the facebook folder

    Returns:
        fig: the matplotlib fig object to be used for the GUI
        
        or, None: if no apps exist
    """
    FB = readFolder_demo.Facebook(path)
    names, dates = getApps(FB)
    if names == None:
        return None
    return plotTimeline(names,dates)

def main():
    FB = readFolder_demo.Facebook('./facebook-christinebreckenridge')
    names, dates = getApps(FB)
    plotTimeline(names,dates,'testTL')
    print('hello')


if __name__ == '__main__':
    main()