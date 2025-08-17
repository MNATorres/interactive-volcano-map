import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map( 
    location=[38.2,-99.1], 
    zoom_start=12, 
    tiles="cartodb positron"
) 

fg = folium.FeatureGroup(name="My Map")

for lt,ln, el in zip(lat,lon, elev):
    popup= folium.Popup(str(el) + " m", parse_html=True)
    fg.add_child(folium.Marker(location=[lt,ln], popup=popup, icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")