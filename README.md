# Raspberry Pi Power Supply Checker
[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE.md) 
![Project Maintenance][maintenance-shield1]
[![Contributors][contributors-shield]][contributors]
[![Discord][discord-shield]][discord]

A sensor for Home-Assistant that checks your power supply and reports back to your setup
this simple sensor reports values from the kernel and if it reports anything else then 0 then there are issues with the power supply.

For more information about Raspberry Pi Power supplies check the following link

https://github.com/superjamie/lazyweb/wiki/Raspberry-Pi-Power

## Getting started
Place the component at this location on your setup: 

* Hass.io: `/custom_components/rpi_power/sensor.py`
* Hassbian / Other: `<config directory>/custom_components/rpi_power/sensor.py`

Here is a list of the current values the component checks for 

| Value  | Description |
| ------------- | ------------- |
| 0  | Everything is working as intended  |
| 1000*  | Under-voltage was detected, consider getting a uninterruptible power supply for your Raspberry Pi. |
| 2000* | Your Raspberry Pi is limited due to a bad powersupply, replace the power supply. |
| 3000* | Your Raspberry Pi is limited due to a bad powersupply, replace the power supply. |
| 4000* | The Raspberry Pi is throttled due to a bad power supply this can lead to corruption and instability, please replace your changer and cables. |
| 5000* | The Raspberry Pi is throttled due to a bad power supply this can lead to corruption and instability, please replace your changer and cables. |
| 8000* | Your Raspberry Pi is overheating, consider getting a fan or heat sinks. |

***Example configuration.yaml***

```yaml
sensor:
  platform: rpi_power
  text_state: true
```

and then this as an automation that sets off a notification in homeassistant.

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
      title: "Power Supply Issue"
```

**Optional config options:**  

| key | required | default | description
| --- | --- | --- | ---
| **text_state** | no | `false` | Sets the description as the state if `true`.

⚠️ This requires Kernel 4.14 or higher.

Due to how `custom_components` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.

## Issues
Use the bugtracker for your issues if a value is missing please use the following command to get the value

```bash
cat /sys/devices/platform/soc/soc:firmware/get_throttled
```

Then post in the bug report makes it so much easier for me to implement the missing values.

## Donate

| Donate | Developer |
| --- | --- |
| <a href="https://www.paypal.me/swetoast"><img align="center" src="https://gitlab.com/swe_toast/asustor_firewall/raw/master/images/Untitled.png"></a>   | <a href="https://github.com/swetoast">Toast</a></div> |

or contribute code to the project :) just make sure to lint your stuff before submitting.

[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[contributors-shield]: https://img.shields.io/github/contributors/custom-components/sensor.rpi_power.svg?style=for-the-badge
[contributors]: https://github.com/custom-components/sensor.rpi_power/graphs/contributors/
[license-shield]: https://img.shields.io/github/license/custom-components/sensor.rpi_power.svg?style=for-the-badge
[maintenance-shield1]: https://img.shields.io/badge/maintainer-Toast%20%40swetoast-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/custom-components/sensor.rpi_power.svg?style=for-the-badge
[releases]: https://github.com/custom-components/sensor.rpi_power/releases
