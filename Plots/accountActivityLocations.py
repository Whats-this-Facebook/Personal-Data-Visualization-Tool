import matplotlib.pyplot as plt
import CLI.readFolder as readFolder

import pandas as pd
import geopandas
from cities_coordinates import CityCoordinator

def constructGeoPandaDF(FB):
    """Constructs a data frame that is the location information
    to be plotted

    Args:
        readFolder object

    Returns:
        geopanda dataframe
    """
    aa = FB.account_activity()

    cities = []
    countries = []
    latitudes = []
    longitudes = []

    c=CityCoordinator()
    city = c.get_city(city_name="Albany",country_code_iso="US")

    print("Processing account activity data...")

    for i in aa:
        if ("city" in i) and ("country" in i):
            cityCoords = c.get_city(city_name=i["city"],country_code_iso=i["country"])
            if isinstance(cityCoords, dict):
                cities.append(i["city"])
                countries.append(i["city"])
                latitudes.append(float(cityCoords["location"]["lat"]))
                longitudes.append(float(cityCoords["location"]["lon"]))

    df = pd.DataFrame(
        {'City': cities,
         'Country': countries,
         'Latitude': latitudes,
         'Longitude': longitudes})

    print("Done!")

    return df


def plotLocations(path):
    """Plots account activity locations

    Args:
        path (string): path to the facebook folder

    Returns:
        fig: geopanda fig object to be used for the GUI
    """

    FB = readFolder.Facebook(path)

    df = constructGeoPandaDF(FB)
    gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))

    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

    # Set the map image
    ax = world.plot(color='white', edgecolor='black')

    # Plot ``GeoDataFrame``.
    plot = gdf.plot(ax=ax, color='red')

    # Return figure image
    return plt.gcf()

def main():
    print('howdy')


if __name__ == '__main__':
    main()
