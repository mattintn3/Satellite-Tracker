from get_json_data import get_json_data
from get_tle_data import get_tle_data
from combine_json_and_tle import combine_json_and_tle
from skyfield.api import EarthSatellite, load, wgs84

# Store JSON url and TLE url for active satellites
json_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json"
tle_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

json_data = get_json_data(json_url)
tle_data = get_tle_data(tle_url)

ts = load.timescale()


combined_data = combine_json_and_tle(json_data, tle_data)
iss_data = {}
line1 = ""
line2 = ""

for sat in combined_data:
    if sat["OBJECT_NAME"] == "ISS (ZARYA)":
        line1 = sat["tle_line1"]
        line2 = sat["tle_line2"]

        satellite = EarthSatellite(line1, line2, sat["OBJECT_NAME"], ts)

        t = ts.now()

        geocentric = satellite.at(t)
        lat, lon = wgs84.latlon_of(geocentric)
        print(sat)
        print("Latitude: ", lat)
        print("Longitude: ", lon)
#print(item)
#print("\n")