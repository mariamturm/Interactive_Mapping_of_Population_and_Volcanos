import folium
import pandas

data = pandas.read_csv("Webmap_datasources/Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])


map = folium.Map(
    location = [38.58, -99.09], 
    zoom_start = 6, 
    tiles = "CartoDB positron",
    )
fg = folium.FeatureGroup(name = "My Map")

for lt, ln, el in zip(latitude, longitude, elev):
        fg.add_child(folium.Marker(location = [lt, ln], popup = "Elevation here is: " + str(el) + "m", icon = folium.Icon(color = 'purple')))


map.add_child(fg)
map.save("Map1.html")
