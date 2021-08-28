"""
This file contains the implementation of the main FarmOS object that can be used to access
log and assets data.
"""
import requests
import json


class FarmOS:
    def __init__(self, ip_address: str):
        self.hostname = ip_address
        self.sensors = {}

    def add_sensor(self, sensor):
        """
        :param sensor: An Sensor object.
        """
        sensor.set_hostname(self.hostname)
        self.sensors[sensor.name] = sensor

    def get_logs(self, filters: dict) -> str:
        """
        :param filters: A dict { str : str } with filter name as key and filter value as value.
            Example input: {'type': 'soil_test', 'log_category': 'soil'}
        :return: The API response as JSON formatted string.
        """
        url = f"http://{self.hostname}/log.json?"

        for f_name, f_value in filters.items():
            if f_name == 'type':
                url += f"{f_name}=farm_{f_value}&"
            else:
                url += f"{f_name}={f_value}&"

        res = requests.get(url)

        return res.text


    def get_assets(self, filters):
        pass
