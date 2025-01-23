def combine_json_and_tle(json, tle):
    combined_data = []
    for satellite in json:
        name = satellite["OBJECT_NAME"]
        if name in tle:
            satellite["tle_line1"] = tle[name]["tle_line1"]
            satellite["tle_line2"] = tle[name]["tle_line2"]
        else:
            satellite["tle_line1"] = None
            satellite["tle_line2"] = None
        combined_data.append(satellite)
    return combined_data