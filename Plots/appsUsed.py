import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style as style
import matplotlib.dates as mdates
from datetime import datetime
import CLI.readFolder as readFolder
from matplotlib.colors import LinearSegmentedColormap


def findRepeatDates(dates,names):
    cnt = 0
    newDates, newNames = [], []
    for i,date in enumerate(dates[:-1]):
        if abs(int((dates[i-1] - date).days)) <= 31:
            newNames[-1] += ' | ' + names[i]
            cnt += len(names[i])
            if cnt > 100:
                newNames[-1] += '\n'
                cnt = 0
        else:
            cnt = 0
            newNames.append(names[i])
            newDates.append(date)
    return newNames, newDates

def getApps(FB):
    apps = FB.apps()
    if apps == []:
        return None, None
    names = [i['name'] for i in apps]
    #timestamps = 
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
    if len(names) > 29:
        fontSize = 7
    elif len(names) > 24:
        fontSize = 7 
    elif len(names) > 19:
        fontSize = 7
    else:
        fontSize = 7
    vertResolution = [2,2,2,2,2,2]
    levels = np.tile(vertResolution,
                     int(np.ceil(len(dates)/6)))[:len(dates)]

    # Create figure and plot a stem plot with the date
    '''
    total_years = int(dates[0].year) - int(dates[-1].year)
    if total_years < 7:
        height = 10
    elif total_years < 8:
        height = 25
    elif total_years < 9:
        height = 40
    else:
        height = 55
    '''
    fig, ax = plt.subplots(figsize=(10,20))
    ax.set(title="Apps that facebook knows you've used")

    #markerline, stemline, baseline = ax.stem(dates, levels,
                                             #linefmt="#3B5998", basefmt="k-",
                                             #use_line_collection=True)
    
    ax.hlines(dates, 0, levels, color="tab:blue",linestyles='solid')  # The vertical stems.
    ax.plot(np.zeros_like(dates), dates, "-o",
        color="k", markerfacecolor="w")  # Baseline and markers on it.    


    #plt.setp(markerline, mec="k", mfc="w", zorder=3,color='#3B5998')

    # Shift the markers to the baseline by replacing the y-data by zeros.
    #markerline.set_ydata(np.zeros(len(dates)))

    # annotate lines
    vert = np.array(['top', 'center'])[(levels > 0).astype(int)]
    for d, l, r, va in zip(dates, levels, names, vert):
        ax.annotate(r, fontsize=fontSize, xy=(l, d), xytext=(-3, np.sign(l)*3),
                    textcoords="offset points", va=va, ha="right")

    # format xaxis with 4 month intervals
    ax.get_yaxis().set_major_locator(mdates.MonthLocator(interval=4))
    ax.get_yaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(ax.get_yticklabels(), rotation=30, ha="right")

    # remove y axis and spines
    ax.get_xaxis().set_visible(False)
    for spine in ["left", "top", "right"]:
        ax.spines[spine].set_visible(False)

    ax.margins(y=0.1)
    #ax.set_adjustable('datalim')
    plt.tight_layout()
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
    FB = readFolder.Facebook(path)
    names, dates = getApps(FB)
    if names == None:
        return None
    return plotTimeline(names,dates)

def main():
    #FB = readFolder.Facebook('../../facebook-emilygarcia906')
    FB = readFolder.Facebook('facebook-christinebreckenridge')

    names, dates = getApps(FB)
    plotTimeline(names,dates,'testTL')
    print('hello')


if __name__ == '__main__':
    main()
