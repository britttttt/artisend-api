import requests

def geocode_postal_code(postal_code):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "postalcode": postal_code,
        "countrycodes": "us",
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "artisendapi/1.0 (your_email@example.com)"
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200 and response.json():
        result = response.json()[0]
        return float(result["lat"]), float(result["lon"])
    return None, None