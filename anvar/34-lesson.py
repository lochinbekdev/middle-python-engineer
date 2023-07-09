# Json

import json
import googlemap
from APIKEY import apikey



gmaps=googlemap.Client(key = apikey)

data = gmaps.geocode('Olmazor, Tashkent, Uzbekistan')

print(data)
