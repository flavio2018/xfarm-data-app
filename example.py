from FarmOS import FarmOS
from Sensor import Sensor

if __name__ == '__main__':

    farmos = FarmOS('192.168.8.106')

    res = farmos.get(
        resource='log',
        filters={'type': 'purchase',
                 'log_category': "Costi%20Produzione%20Olio",
                 }
    )
    print(res)

    temp_sensor = Sensor(
        name='temperature0',
        public_key='2af62b0d5189b65e7fb8bf7024fb574e',
        private_key='76102647a4127eada9aac3bae1229519'
    )

    farmos.add_sensor(temp_sensor)
    res = farmos.sensors['temperature0'].get_values()

    print(res)
