import requests

def get_tle_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        tle_data = response.text.strip().split("\n")
        tle_dict = {}

        # Group each entry into sets of 3 lines for TLE format
        for i in range(0, len(tle_data), 3):
            name = tle_data[i].strip()
            tle_line1 = tle_data[i+1].strip()
            tle_line2 = tle_data[i+2].strip()
            tle_dict[name] = {"tle_line1": tle_line1, 
                              "tle_line2": tle_line2}
        return tle_dict
    else:
        raise Exception(f"Failed to fetch TLE data: {response.status_code}")