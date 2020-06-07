import requests



url = 'http://localhost:3000/predict'

# make post request and print response
r = requests.get(url,json={"BlOCK":"500","GROSS SQUARE FEET":"40000","LOT":"50","ZIP CODE":"1092","LAND SQUARE FEET":"3000","YEAR BUILT":"1995"})
print(r.json())

