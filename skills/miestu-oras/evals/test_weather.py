import datetime as dt
import importlib.util
import pathlib
import unittest

path = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "weather.py"
spec = importlib.util.spec_from_file_location("weather", path)
weather = importlib.util.module_from_spec(spec)
spec.loader.exec_module(weather)


class WeatherTests(unittest.TestCase):
    def test_nearest_future_and_translation(self):
        now = dt.datetime(2026, 10, 21, 12, 30, tzinfo=dt.timezone.utc)
        data = {"forecastTimestamps": [
            {"forecastTimeUtc": "2026-10-21 12:00:00", "airTemperature": 1, "conditionCode": "clear"},
            {"forecastTimeUtc": "2026-10-21 14:00:00", "airTemperature": 8.5, "conditionCode": "rain"},
            {"forecastTimeUtc": "2026-10-21 13:00:00", "airTemperature": 7, "conditionCode": "cloudy"},
        ]}
        result = weather.pick_nearest(data, now)
        self.assertEqual(result["temperature"], 7)
        self.assertEqual(result["condition"], "Debesuota")
        self.assertEqual(result["local_time"], "2026-10-21 16:00")

    def test_missing_future(self):
        with self.assertRaisesRegex(ValueError, "būsimos"):
            weather.pick_nearest({"forecastTimestamps": []})

    def test_zero_temperature(self):
        now = dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)
        result = weather.pick_nearest({"forecastTimestamps": [
            {"forecastTimeUtc": "2026-01-01 10:00:00", "airTemperature": 0, "conditionCode": None}
        ]}, now)
        self.assertEqual(result["temperature"], 0)
        self.assertEqual(result["condition"], "Nenustatyta")


if __name__ == "__main__":
    unittest.main()
