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
        "User-Agent": "artisendapi/1.0 (contact@yourdomain.com)"
    }
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
    except Exception:
        pass
    return None, None