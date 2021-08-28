from datetime import datetime
import folium
from streamlit_folium import folium_static
import json
import matplotlib.pyplot as plt
import pandas as pd

from Sensor import Sensor
from FarmOS import FarmOS

import streamlit as st


def add_sensor_plot(sensor, xlabel, ylabel):
    sensor_name = sensor.name
    res = sensor.get_values()

    json_res = json.loads(res)
    timestamps = [int(entry['timestamp']) for entry in json_res]
    timestamps = [datetime.utcfromtimestamp(t).isoformat() for t in timestamps]
    values = [float(entry['value']) for entry in json_res]

    fig, ax = plt.subplots(1, 1, figsize=(6, 4))
    ax.scatter(timestamps, values)
    plt.xticks(rotation='vertical')
    ax.set_xlim(ax.get_xlim()[::-1])
    fig.suptitle(sensor_name)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    st.write(fig)


if __name__ == '__main__':
    farmos = FarmOS('192.168.8.106')

    add_selectbox = st.sidebar.selectbox(
        'Scegli la sezione del sito:',
        ('Aree XFarm', 'Sensori', 'Bilancio del carbonio'),
    )

    if add_selectbox == 'Sensori':
        col1, col2 = st.columns(2)

        temp_sensor0 = Sensor(
            name='temp_sensor_1',
            public_key='2af62b0d5189b65e7fb8bf7024fb574e',
            private_key='76102647a4127eada9aac3bae1229519',
        )
        temp_sensor1 = Sensor(
            name='temp_sensor_2',
            public_key='24c56526a74058f951bf69b577ed1068',
            private_key='945b741154c13fe61c53eadc7e333b88',
        )

        hum_sensor0 = Sensor(
            name='hum_sensor_1',
            public_key='24ca2501834d02fbb0e01c62ae17ccc8',
            private_key='da65ec96958277564197b7491dd8a994',
        )
        hum_sensor1 = Sensor(
            name='hum_sensor_2',
            public_key='1ad2540bcee390239ee23ba907ea4d4b',
            private_key='287d7476639204460cf8f3b1b8540ebf',
        )

        rain_sensor0 = Sensor(
            name='rain_sensor_1',
            public_key='bdfad07d1d020c124e348720df0f7948',
            private_key='ee0009b0684b854f12cc640c39339e74',
        )
        rain_sensor1 = Sensor(
            name='rain_sensor_2',
            public_key='8486b3b28734b5b178e169938f6dd25a',
            private_key='b003938e4ea7cca0ab746ae0534d13d5',
        )

        soil_hum_sensor0 = Sensor(
            name='soil_hum_sensor_1',
            public_key='e1b5b4f51caaf9fb126bcc3ac2e45fa5',
            private_key='f33c8bd9c030bf423312d5e99224ed75',
        )
        soil_hum_sensor1 = Sensor(
            name='soil_hum_sensor_2',
            public_key='12e22380ff156b2b22f33b362fb3f476',
            private_key='3171ecb6e64a3ede5e1b4ed2c14379fc',
        )

        farmos.add_sensor(temp_sensor0)
        farmos.add_sensor(temp_sensor1)
        farmos.add_sensor(hum_sensor0)
        farmos.add_sensor(hum_sensor1)
        farmos.add_sensor(rain_sensor0)
        farmos.add_sensor(rain_sensor1)
        farmos.add_sensor(soil_hum_sensor0)
        farmos.add_sensor(soil_hum_sensor1)

        with col1:
            st.markdown("## Temperature")
            add_sensor_plot(farmos.sensors['temp_sensor_1'], 'time', 'Air temperature (°C)')
            add_sensor_plot(farmos.sensors['temp_sensor_2'], 'time', 'Air temperature (°C)')

            st.markdown("## Rain")
            add_sensor_plot(farmos.sensors['rain_sensor_1'], 'time', 'Relative leaf wetness (%)')
            add_sensor_plot(farmos.sensors['rain_sensor_2'], 'time', 'Relative leaf wetness (%)')

        with col2:
            st.markdown("## Air humidity")
            add_sensor_plot(farmos.sensors['hum_sensor_1'], 'time', 'Relative air humidity (%)')
            add_sensor_plot(farmos.sensors['hum_sensor_2'], 'time', 'Relative air humidity (%)')

            st.markdown("## Soil humidity")
            add_sensor_plot(farmos.sensors['soil_hum_sensor_1'], 'time', 'Relative soil humidity (%)')
            add_sensor_plot(farmos.sensors['soil_hum_sensor_2'], 'time', 'Relative soil humidity (%)')

    elif add_selectbox == 'Aree XFarm':
        with open('xfarm_orchards1.geojson', 'r') as geojson_f:
            geojson = json.load(geojson_f)
        geojson_shapes = [f for f in geojson['features']]

        areas = farmos.get_taxonomy(terms=['areas'])

        json_areas = json.loads(areas)
        areas = json_areas['list']
        areas_names = [area['name'] for area in areas]
        areas_descriptions = [area['description'] for area in areas]
        areas_geofield = [area['geofield'] for area in areas]
        areas_latlon = []
        for ag in areas_geofield:
            if len(ag) > 0:
                areas_latlon.append([float(value) for value in ag[0]['latlon'].split(',')])
            else:
                pass

        st.markdown('# Aree di XFarm')

        for name, description, area_latlon, geojson_shape in zip(areas_names, areas_descriptions, areas_latlon, geojson_shapes):
            st.markdown(f"## {name}")
            st.write(description, unsafe_allow_html=True)

            m = folium.Map(location=area_latlon, zoom_start=14)
            folium.GeoJson(geojson_shape).add_to(m)
            folium_static(m)

    elif add_selectbox == 'Bilancio del carbonio':
        st.markdown("# Gestione aziendale")
        st.markdown("## Carbonio sottratto all'atmosfera: -0.3 ton/ha all' anno")
        st.markdown("- Consumo carburante: 30 l → 24 kg (0.8 kg/l)")
        st.markdown("- Biomassa immessa nel terreno: 0 ton/ha")
        st.markdown("- CO2 reimmessa nell'atmosfera: ~0.8 ton/ha")

        st.markdown("# Gestione sperimentale")
        st.markdown("## Carbonio sottratto all'atmosfera: +12 ton/ha all' anno")
        st.markdown("- Consumo carburante: 15 l → 12 kg (0.8 kg/l)")
        st.markdown("- Biomassa immessa nel terreno: 1.5 ton/ha")
        st.markdown("- CO2 reimmessa nell'atmosfera: ~1.4 ton/ha")