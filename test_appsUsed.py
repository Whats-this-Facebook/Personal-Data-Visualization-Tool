from Plots.appsUsed import plotApps
import matplotlib.pyplot as plt
import pytest


def test_plotApps():
    assert plotApps('./Plots/facebook-christinebreckenridge') != None 

#def test_plotApps_small():
#    assert plotApps('facebook-100056193726775') != None


def main():
    fig = plotApps('./Plots/facebook-christinebreckenridge')
    plt.show()
    print('hello') 


if __name__ == '__main__':
    main()