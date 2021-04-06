#!/usr/bin/python3
"""Alta3 Research - tracking ISS updated output"""

import urllib.request
import json
import requests

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():

    groundctrl = urllib.request.urlopen(MAJORTOM)
    helmet = groundctrl.read()
    helmetson = json.loads(helmet.decode("utf-8"))
    print(type(helmetson))


    resp = requets.get(MAJORTOM)
    resp = resp.json()
    print(type(resp)
