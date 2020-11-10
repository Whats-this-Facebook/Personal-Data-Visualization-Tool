import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style as style
# import matplotlib.dates as mdates
# from datetime import datetime
# import CLI.readFolder as readFolder
# from matplotlib.colors import LinearSegmentedColormap




# Arg: Folder path of facebook personal data file.
def plotDataQuantity(datFolder):
    fig, ax = plt.subplots()

    # Data to plot
    labels = 'Python', 'C++', 'Ruby', datFolder
    sizes = [215, 130, 245, 210]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0, 0, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    return fig

def main():
    plotDataQuantity()
    print('Data Quantity Visualized')


if __name__ == '__main__':
    main()
