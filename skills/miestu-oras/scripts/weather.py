#!/usr/bin/env python3
"""Artimiausia penkių didžiausių Lietuvos miestų meteo.lt prognozė."""
import concurrent.futures
import datetime as dt
import json
import sys
import urllib.error
import urllib.request
from zoneinfo import ZoneInfo

CITIES = {
    "Vilnius": "vilnius",
    "Kaunas": "kaunas",
    "Klaipėda": "klaipeda",
    "Šiauliai": "siauliai",
    "Panevėžys": "panevezys",
}
CONDITIONS = {
    "clear": "Giedra",
    "partly-cloudy": "Mažai debesuota",
    "cloudy-with-sunny-intervals": "Debesuota su pragiedruliais",
    "cloudy": "Debesuota",
    "light-rain": "Nedidelis lietus",
    "rain": "Lietus",
    "heavy-rain": "Smarkus lietus",
    "thunder": "Perkūnija",
    "isolated-thunderstorms": "Trumpas lietus su perkūnija",
    "thunderstorms": "Lietus su perkūnija",
    "heavy-rain-with-thunderstorms": "Smarkus lietus su perkūnija",
    "light-sleet": "Nedidelė šlapdriba",
    "sleet": "Šlapdriba",
    "freezing-rain": "Lijundra",
    "hail": "Kruša",
    "light-snow": "Nedidelis sniegas",
    "snow": "Sniegas",
    "heavy-snow": "Smarkus sniegas",
    "fog": "Rūkas",
}
VILNIUS_TZ = ZoneInfo("Europe/Vilnius")


def parse_utc(value):
    return dt.datetime.fromisoformat(value.replace(" ", "T").replace("Z", "+00:00")).replace(
        tzinfo=dt.timezone.utc
    ) if "+" not in value and not value.endswith("Z") else dt.datetime.fromisoformat(
        value.replace(" ", "T").replace("Z", "+00:00")
    ).astimezone(dt.timezone.utc)


def pick_nearest(data, now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    candidates = []
    for item in data.get("forecastTimestamps", []):
        when = parse_utc(item["forecastTimeUtc"])
        if when >= now:
            candidates.append((when, item))
    if not candidates:
        raise ValueError("Nėra būsimos prognozės")
    when, item = min(candidates, key=lambda x: x[0])
    if item.get("airTemperature") is None:
        raise ValueError("Nėra temperatūros duomenų")
    condition = item.get("conditionCode")
    return {
        "temperature": item["airTemperature"],
        "condition": CONDITIONS.get(condition, condition or "Nenustatyta"),
        "local_time": when.astimezone(VILNIUS_TZ).strftime("%Y-%m-%d %H:%M"),
    }


def fetch_city(name, code):
    url = f"https://api.meteo.lt/v1/places/{code}/forecasts/long-term"
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "miestu-oras/1.0 (weather-information)"})
        with urllib.request.urlopen(request, timeout=15) as response:
            data = json.load(response)
        return name, pick_nearest(data), None
    except (urllib.error.URLError, TimeoutError, ValueError, KeyError, json.JSONDecodeError) as exc:
        return name, None, str(exc)


def main():
    print("Artimiausia orų prognozė penkiems didžiausiems Lietuvos miestams\n")
    print("| Miestas | Temperatūra (°C) | Oro sąlygos | Prognozės laikas (Lietuvos) |")
    print("|---|---:|---|---|")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        results = list(pool.map(lambda pair: fetch_city(*pair), CITIES.items()))
    failures = 0
    for name, result, error in results:
        if error:
            failures += 1
            print(f"| {name} | — | Nepavyko gauti duomenų | — |")
            print(f"Klaida ({name}): {error}", file=sys.stderr)
        else:
            temp = f"{result['temperature']:g}" if isinstance(result["temperature"], (int, float)) else str(result["temperature"])
            print(f"| {name} | {temp} | {result['condition']} | {result['local_time']} |")
    print("\nŠaltinis: Lietuvos hidrometeorologijos tarnyba — https://api.meteo.lt/")
    print("Pastaba: tai artimiausio laiko prognozė, ne faktiniai meteorologiniai matavimai.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
