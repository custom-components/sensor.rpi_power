# rpi_power

[![Version](https://img.shields.io/badge/version-0.0.7-green.svg?style=for-the-badge)](#) [![mantained](https://img.shields.io/maintenance/yes/2018.svg?style=for-the-badge)](#) [![maintainer](https://img.shields.io/badge/maintainer-Peter%20Skopa%20%40swetoast-blue.svg?style=for-the-badge)](#) [![forum](https://img.shields.io/badge/forum-visit-orange.svg?style=for-the-badge)](https://community.home-assistant.io/t/raspberry-pi-power-sensor-updated-2018-07-03/58155)   
A sensor that checks your Raspberry Pi charger so its not giving you undervoltage.

To get started put `/custom_components/sensor/rpi_power.py` here:  
`<config directory>/custom_components/sensor/rpi_power.py`  

**Example configuration.yaml:**

```yaml
sensor:
  platform: rpi_power
```

**Optional config options:**  

| key | required | default | description
| --- | --- | --- | ---
| **text_state** | no | `false` | Sets the desctiption as the state if `true`.

⚠️ This require Kernel 4.14 or higher.

[Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/)  
***
Due to how `custom_componentes` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.

Here is a simple automation example that will notify you if the psu is failing 

```yaml
- id: 'rpi_power_issue'
  alias: Power Problem Notification
  trigger:
  - platform: numeric_state
    entity_id: sensor.rpi_power_status
    above: 0
    for:
      minutes: 1
  condition:
  action:
    service: persistent_notification.create
    data:
      message: "Charger reported {{ states.sensor.rpi_power_status.state }}"
      title: "RPI Power Issue"
```
