import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style as style
import os as os
# import matplotlib.dates as mdates
# from datetime import datetime
# import CLI.readFolder as readFolder
# from matplotlib.colors import LinearSegmentedColormap



"""

def messages(self):
    path = str(self.folder + "/messages/inbox/")
    messages = []
    try:
        folders = os.scandir(path)
        for f in folders:
          if os.path.isdir(os.path.join(path, f)):
            folder = os.scandir(os.path.join(path, f))
            for file in folder:
              if os.path.isfile(os.path.join(path, file)):
                messages.append(json.load(open(os.path.join(path, file))))
"""

# Folder size function from ->
# https://www.thepythoncode.com/article/get-directory-size-in-bytes-using-python
def get_directory_size(directory):
    """Returns the `directory` size in bytes."""
    total = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file():
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        return os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return total


def getLabels(data_folder):
    folders = os.scandir(data_folder)
    folderNames = []
    for f in folders:
        folderNames.append(f.name)

    return folderNames

def getCategoryObjects(data_folder):
    folders = os.scandir(data_folder)
    categoryObjects = []
    for f in folders:
        categoryObj = {
            "name": f.name,
            "size": get_directory_size(f)
        }
        categoryObjects.append(categoryObj)



    return categoryObjects

# Converts a bytes number into a more readable string
def bytesToString(size):
    if size > 1000000000: # Gigabytes
        return str(round(size/1000000000, 2)) + " gigabytes"
    elif size > 1000000: # Megabytes
        return str(round(size/1000000, 2)) + " megabytes"
    elif size > 1000: # Kilobytes
        return str(round(size/1000, 2)) + " kilobytes"
    else:
        return str(size) + " bytes"



# Arg: Folder path of facebook personal data file.
def plotDataQuantity(pie_chart_name, data_folder):

    # Gather directory info
    category_objects = getCategoryObjects(data_folder)

    # Get the total bytes of data
    totalBytes = 0
    for x in category_objects:
        totalBytes += x["size"]

    # Get the labels and sizes
    labels = []
    sizes = []
    for x in category_objects:
        if (x["size"] > totalBytes/200):
            labels.append(x["name"] + ":\n" + bytesToString(x["size"]))
            sizes.append(x["size"])

    # Data to plot
    #labels = 'Python', 'C++', 'Ruby', data_folder
    #labels = getLabels(data_folder)
    #print(len(labels))
    #labels = 'Python', 'C++', 'Ruby', data_folder
    #sizes = [215, 130, 245, 10]
    #sizes = [20 for i in range(34)]
    #colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    # Plot
    #plt.pie(sizes, labels=labels, colors=colors,
    #plt.pie(sizes, labels=labels, autopct='%0.1f%%', shadow=False, startangle=140)
    #patches, texts = plt.pie(sizes, startangle=90)
    #plt.legend(patches, labels, loc="best")

    #plt.axis('equal')
    #plt.tight_layout()

    plt.rcParams['font.size'] = 8.0

    # Pie chart code modified from ->
    # https://matplotlib.org/3.3.2/gallery/pie_and_polar_charts/pie_and_donut_labels.html#sphx-glr-gallery-pie-and-polar-charts-pie-and-donut-labels-py

    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))

    wedges, texts = ax.pie(sizes, wedgeprops=dict(width=1), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)

    ax.set_title(pie_chart_name)

    if pie_chart_name == '':
        return fig
    else:
        plt.savefig(pie_chart_name + '.png')


def main():
    plotDataQuantity("test", "/Users/AidenTheJaunty/Desktop/Software Engineering/facebook-aidenjnelson")
    print('Data Quantity Visualized')


if __name__ == '__main__':
    main()
