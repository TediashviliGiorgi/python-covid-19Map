
import folium
import requests
from bs4 import BeautifulSoup

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













'''
map = folium.Map(location = [41.69, 81.09], zoom_level = 4, tiles = "Stamen Terrain")

# init group
group = folium.FeatureGroup(name = "My Markers")

for item in [[41.89, 81.19], [41.59, 81.29], [41.80, 81.19]]:
# add group to map
    group.add_child(folium.Marker(location = item, popup = "Test Marker"))

#  put markers in map
map.add_child(group)

map.save("coronaMap.html")
'''