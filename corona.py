
import folium
import requests
from bs4 import BeautifulSoup
import pandas

def radius_gen(tcases):
    return float(tcases) ** 0.25



r = requests.get("https://www.worldometers.info/coronavirus/")
c = r.content
soup = BeautifulSoup(c, "html.parser")
data = soup.find("tbody")
rows = data.find_all("tr", {"style":""})

d = {}

# rows.find_all("td")[2].txt

for item in rows:
    tcases = item.find_all("td")[2].text
    d[item.find_all("td")[1].text] = tcases.replace(",","")
print(d)

country_data = pandas.read_csv("countries.csv")

lat = list(country_data["latitude"])
lon = list(country_data["longitude"])
name = list(country_data["name"])



map = folium.Map(location = [41.69, 81.09], zoom_level = 4, tiles = "Stamen Terrain")

# init group
group = folium.FeatureGroup(name = "countries")

for lt, ln, ne in zip(lat, lon, name):
    if ne in d.keys():

# add group to map
        group.add_child(folium.CircleMarker(location = [lt,ln], popup = str(ne) + "\n" + str(d[ne]),
        radius = radius_gen(d[ne]), fill_color = "red", color = "black", fill_opacity = 0.7))

#  put markers in map
map.add_child(group)

map.save("coronaMap.html")
