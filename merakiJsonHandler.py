#!/usr/bin/env python3
from types import SimpleNamespace
import requests

class MerakiJsonHandler(object):
    def __init__(self):
        self.json = requests.get('http://my.meraki.com/index.json').json()
        self.config = SimpleNamespace(**self.json['config'])
        self.client = SimpleNamespace(**self.json['client'])
        self.radio1 = SimpleNamespace(**self.json['radio_stats'][0])
        self.radio2 = SimpleNamespace(**self.json['radio_stats'][1])
        self.connection = SimpleNamespace(**self.json['connection_state'])

    def utilization2(self):
        prof_cc = self.radio2.prof_cc
        prof_rf = self.radio2.prof_rf
        prof_tf = self.radio2.prof_tf
        e = (100 / prof_cc) if (prof_cc > 0) else 0
        f = round((prof_rf + prof_tf)*e)
        return f

