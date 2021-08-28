# Scripts

## Planting data massive loading script

Filename: `load_plantings`

This script loads planting data inserted in a `csv` file on a FarmOS instance as
assets and adds log events in order to set their locations. A model of the csv
file can be found in `plantings.csv`.

**ATTENTION!!** In order to access the FarmOS API the following procedure
should be followed beforehands (as described in the [FarmOS
Documentation](https://farmos.org/development/api/#2-session-cookie-and-csrf-token)):

1. Run the following `curl` commands:
    ```
    curl --cookie-jar farmOS-cookie.txt -d 'name=[USER]&pass=[PASS]&form_id=user_login' [URL]/user/login
    TOKEN="$(curl --cookie farmOS-cookie.txt [URL]/restws/session/token)"
    echo $TOKEN > token.txt
    ```
