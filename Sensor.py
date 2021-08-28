import requests
import json


class Sensor:
    def __init__(self, name, public_key, private_key):
        self.name = name
        self.public_key = public_key
        self.private_key = private_key

    def set_hostname(self, hostname):
        self.hostname = hostname

    def get_values(self, params={'limit': 0}):
        url = f"http://{self.hostname}/farm/sensor/listener/{self.public_key}?{self.private_key}&"

        for p_key, p_value in params.items():
            url += f"{p_key}={p_value}&"

        res = requests.get(url)

        return res.text
