#!/usr/bin/env python3

import requests
import json
from types import SimpleNamespace

class MerakiJsonHandler(object):
    def __init__(self):
        self.wap = requests.get('http://my.meraki.com/index.json').json()
        self.config = SimpleNamespace(**self.wap['config'])
        self.client = SimpleNamespace(**self.wap['client'])
        self.radio1 = SimpleNamespace(**self.wap['radio_stats'][0])
        self.radio2 = SimpleNamespace(**self.wap['radio_stats'][1])
        self.connection = SimpleNamespace(**self.wap['connection_state'])

    def utilization(self):
        prof_cc = self.radio['prof_cc']
        prof_rf = self.radio['prof_rf']
        prof_tf = self.radio['prof_tf']
        e = (100 / prof_cc) if (prof_cc > 0) else 0
        f = round((prof_rf + prof_tf)*e)
        return f

