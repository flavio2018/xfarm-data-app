# XFarm Data App

This project has been developed over a week during the Y³ labs organized by
[la Scuola Open Source](https://lascuolaopensource.xyz/) at [XFarm - Agricoltura
Prossima](https://www.xfarm.me/).

The goal of the project was to implement a technological stack that could
integrate in a single environment different technological and agronomical
features:
1. Sensor detection and automated data retrieval;
2. Crops and Farming Precision Digital Management;
3. Data visualization and report production.

## Technological Stack

The following technological stack has been adopted:

| Goal | Tool |
|-------|-----|
| Sensor data retrieval | Arduino boards and whatnot |
| Wireless data transmission | LoRa Technology |
| Management system | FarmOS installed on Raspberry Pi |
| Mapping and GIS | QGIS |
| Scripting and data viz | Python and Streamlit |

## TODO

- Implement HTTPS
- Integrate and improve data retrieval from FarmOS API (there is already a
    Python wrapper for data retrieval from FarmOS that requires the use of
    HTTPS, **use it!**)
- Extend FarmOS APIs in order for them to comply to XFarm's necessities
- Augument sensor data retrieval

We are open to contributions 🤙

**ATTENTION!!** DO NOT use these tools in production. They are early prototypes
and not ready for use in a production environment, nor feature sufficient
security measures.
