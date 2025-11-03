import folium
import pandas

data = pandas.read_csv("Webmap_datasources/Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def color_producer(elevation):
        if elevation <= 1500:
               return 'green'
        elif elevation > 1500 and elevation <= 3000:
                return 'orange'
        else:
                return 'red'


map = folium.Map(
    location = [38.58, -99.09], 
    zoom_start = 6, 
    tiles = "CartoDB positron",
    )

fg = folium.FeatureGroup(name = "My Map")

for lt, ln, el, nm in zip(latitude, longitude, elev, name):
        fg.add_child(
            folium.CircleMarker(
                location = [lt, ln], 
                popup = "This is " + nm + " volcano", 
                color = color_producer(el), 
                radius = 7, 
                fill = True,
                fill_opacity = 0.8
            )
        )


map.add_child(fg)
map.save("Map1.html")

print(len(elev))
print(min(elev), max(elev))
