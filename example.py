if __name__ == '__main__':

    farmos = FarmOS('192.168.8.106')

    res = farmos.get_logs({'type': 'soil_test',
                           'log_category': 'soil'})

    temp_sensor = Sensor(
        name='temperature',
        public_key='e0c7f449a0640908ce89697038d93c58',
        private_key='50b44cade7133104cea6692042533410'
    )

    farmos.add_sensor(temp_sensor)
    res = farmos.sensors['temperature'].get_values()

    print(res)
