"""
This file contains the implementation of the main FarmOS object that can be used to access
log and assets data.
"""
import requests


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

    def get(self, resource, filters={}):
        """
        :param filters: A dict { str : str } with filter name as key and filter value as value.
            Example input: {'type': 'soil_test', 'log_category': 'soil'}
        :param resource: A string among: "log", "asset"
        :return: The API response as JSON formatted string.
        """
        base_url = f"http://{self.hostname}"
        if resource == 'log':
            url = f"{base_url}/log.json?"
        elif resource == 'asset':
            url = f"{base_url}/farm_asset.json?"
        else:
            print(f"Unrecognized resource: {resource}")
            return

        for f_name, f_value in filters.items():
            if resource == 'log' and f_name == 'type':
                url += f"{f_name}=farm_{f_value}&"
            elif (resource == 'asset' and f_name == 'type') or f_name == 'log_category':
                url += f"{f_name}={f_value}&"
            else:
                print(f"Unrecognized filters: {filters}")
                return

        res = requests.get(url)

        return res.text

    def get_taxonomy(self, terms):
        """
        :param terms: One of the terms of the taxonomy (es. "areas", "crops", "log_categories").
        """
        base_url = f"http://{self.hostname}"
        url = f"{base_url}/taxonomy_term.json?"

        for term in terms:
            url += f"bundle=farm_{term}"

        res = requests.get(url)

        return res.text
