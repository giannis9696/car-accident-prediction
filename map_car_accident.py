import folium
from folium.plugins import HeatMap
import pandas as pd
def map_of_car_accidents(car_accident):

    map_center = [car_accident['Latitude'].mean(), car_accident['Longitude'].mean()]
    mymap = folium.Map(location=map_center, zoom_start=12)

    heatmap = HeatMap(car_accident[['Latitude', 'Longitude']].dropna(), radius=15)
    mymap.add_child(heatmap)

    return mymap

