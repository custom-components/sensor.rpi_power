# Raspberry Pi Power Supply Checker
[![GitHub Release][releases-shield]][releases]
![Project Maintenance][maintenance-shield1]

[![Discord][discord-shield]][discord]

A sensor that checks your Raspberry Pi charger so its not giving you undervoltage.

To get started put `/custom_components/sensor/rpi_power.py` here:  
`<config directory>/custom_components/rpi_power/`  and rename it to sensor.py

**Example configuration.yaml:**

```yaml
sensor:
  platform: rpi_power
```

**Optional config options:**  

| key | required | default | description
| --- | --- | --- | ---
| **text_state** | no | `false` | Sets the description as the state if `true`.

⚠️ This requires Kernel 4.14 or higher.

Here is some more information about how to improve your Raspberry Pi power situation.

https://github.com/superjamie/lazyweb/wiki/Raspberry-Pi-Power

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
***
Due to how `custom_components` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.

[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/custom-components/sensor.rpi_power.svg?style=for-the-badge
[maintenance-shield1]: https://img.shields.io/badge/maintainer-Peter%20Skopa%20%40swetoast-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/custom-components/sensor.rpi_power.svg?style=for-the-badge
[releases]: https://github.com/custom-components/sensor.rpi_power/releases
