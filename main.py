import phonenumbers
import folium
from myphone import number
import opencage

from phonenumbers import geocoder #for the loaction of the mobile number

# Country Name
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

# Service Provider Name
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

# Getting Latitude and Longitude Coordinates
from opencage.geocoder import OpenCageGeocode
key = '6da942e534b446cd807ad83926f2f83f'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
long = results[0]['geometry']['lng']
print(lat, long)

myMap = folium.Map(location=[lat,long], zoom_start=9)
folium.Marker([lat,long], popup=location).add_to(myMap)

# Save the Map
myMap.save("mylocation.html")



