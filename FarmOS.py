import requests
import json

class FarmOS:
    def __init__(self, ip_address):
        self.hostname = ip_address
        self.sensors = {}

    def add_sensor(self, sensor):
        sensor.set_hostname(self.hostname)
        self.sensors[sensor.name] = sensor

    def get_logs(self, filters) -> str:
        """
        :param filters: A dict { str : str } with filter name as key and filter value as value.
            Example input: {'type': 'soil_test', 'log_category': 'soil'}
        :return: The API response as JSON formatted string.
        """
        url_log = f"http://{self.hostname}/log.json?"

        for f_name, f_value in filters.items():
            if f_name == 'type':
                url_log += f"{f_name}=farm_{f_value}&"
            else:
                url_log += f"{f_name}={f_value}&"

        res = requests.get(url_log)

        return res.text


    def get_assets(self):
        pass
