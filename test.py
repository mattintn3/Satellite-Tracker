from get_json_data import get_json_data
from skyfield.api import EarthSatellite, load, wgs84

# Store JSON url for active satellites
json_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json"

json_data = get_json_data(json_url)

#ts = load.timescale()

for sat in json_data:
    if sat["OBJECT_NAME"] == "ISS (ZARYA)":
        print(sat)
        break


iss_data = {}

#for sat in json_data:
#    if sat["OBJECT_NAME"] == "ISS (ZARYA)":
#
#        satellite = EarthSatellite(line1, line2, sat["OBJECT_NAME"], ts)
#
#        t = ts.now()
#
#        geocentric = satellite.at(t)
#        lat, lon = wgs84.latlon_of(geocentric)
#        print(sat)
#        print("Latitude: ", lat)
#        print("Longitude: ", lon)
##print(item)
##print("\n")