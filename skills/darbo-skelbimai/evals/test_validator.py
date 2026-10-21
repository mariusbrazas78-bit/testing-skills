import unittest
from datetime import datetime, timezone
from pathlib import Path
import importlib.util

p=Path(__file__).resolve().parents[1] / 'scripts' / 'validate_ads.py'
spec=importlib.util.spec_from_file_location('validator', p)
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
NOW=datetime(2026,10,21,12,tzinfo=timezone.utc)
BASE={'page_opened':True,'matching_company':True,'matching_title':True}

class TestAds(unittest.TestCase):
    def test_accepting(self):
        self.assertEqual(v.status({**BASE,'accepting_applications':True},NOW),'active')
    def test_closed(self):
        self.assertEqual(v.status({**BASE,'closed':True,'accepting_applications':True},NOW),'expired')
    def test_passed_deadline(self):
        self.assertEqual(v.status({**BASE,'deadline':'2026-10-20T12:00:00Z','apply_action_verified':True},NOW),'expired')
    def test_future_deadline_only(self):
        self.assertEqual(v.status({**BASE,'deadline':'2026-10-25T12:00:00Z'},NOW),'unverified')
    def test_future_deadline_verified_apply(self):
        self.assertEqual(v.status({**BASE,'deadline':'2026-10-25T12:00:00Z','apply_action_verified':True},NOW),'active')
    def test_search_excerpt(self):
        self.assertEqual(v.status({'accepting_applications':True},NOW),'unverified')
    def test_url(self):
        self.assertEqual(v.canonical_url('https://Example.com/job/?utm_source=x&id=2#apply'),'https://example.com/job?id=2')
    def test_duplicate(self):
        ads=[{'employer':'ABC','title':'Vadovas','city':'Vilnius','url':'https://example.com/job?utm_source=one'}, {'employer':'ABC','title':'Vadovas','city':'Vilnius','url':'https://example.com/job'}]
        self.assertEqual(len(v.deduplicate(ads)),1)
