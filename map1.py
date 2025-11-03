import folium
import pandas

data = pandas.read_csv("Webmap_datasources/Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
name = list(data["NAME"])


map = folium.Map(
    location = [38.58, -99.09], 
    zoom_start = 6, 
    tiles = "CartoDB positron",
    #tiles = "Stamen Terrain",
    #attr='Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap'
    )
fg = folium.FeatureGroup(name = "My Map")
#fg.add_child(folium.Marker(location = [38.2, -99.1], popup = "Hi I am a Marker", icon = folium.Icon(color = 'green')))
#fg.add_child(folium.Marker(location = [37.2, -89.1], popup = "Hi I am a Marker", icon = folium.Icon(color = 'green')))

for lt, ln, nm in zip(latitude, longitude, name):
        fg.add_child(folium.Marker(location = [lt, ln], popup = "This is " + nm + " volcano", icon = folium.Icon(color = 'green')))



# for coordinates in [[38.2, -99.1],[39.2, -97.1]]:
#     fg.add_child(folium.Marker(location = coordinates, popup = "Hi I am a Marker", icon = folium.Icon(color = 'green')))


map.add_child(fg)
map.save("Map1.html")
