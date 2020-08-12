# Raspberry Pi Power Supply Checker 
[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE.md) 
![Project Maintenance][maintenance-shield1]
[![Contributors][contributors-shield]][contributors]<a href="https://liberapay.com/Toast/donate"><img alt="Donate using Liberapay" align="right" align="top" src="https://liberapay.com/assets/widgets/donate.svg"></a>
[![Discord][discord-shield]][discord]

A sensor for Home Assistant that checks your power supply and reports back to your setup
this simple sensor reports values from the kernel and if it reports anything else then 0 then there are issues with the power supply.

For more information about Raspberry Pi Power supplies check the following [link](https://github.com/superjamie/lazyweb/wiki/Raspberry-Pi-Power).

## Getting started

⚠️ This requires kernel 4.14 or higher.

Place the component at this location on your setup:

* Home Assistant (former Hass.io): `/custom_components/rpi_power/sensor.py`
* Home Assistant Core / Hassbian / Other: `<config directory>/custom_components/rpi_power/sensor.py`

 	\__init__.py and manifest.json needs to be in the same folder

and then restart Home Assistant to make sure the component loads.

Here is a list of the current values the component checks for:

| Value  | Description |
| ------------- | ------------- |
| 0  | Everything is working as intended  |
| 1000*  | Under-voltage was detected, consider getting a uninterruptible power supply for your Raspberry Pi. |
| 2000* | Your Raspberry Pi is limited due to a bad power supply, replace the power supply. |
| 3000* | Your Raspberry Pi is limited due to a bad power supply, replace the power supply. |
| 4000* | Your Raspberry Pi is throttled due to a bad power supply this can lead to corruption and instability, please replace your charger and cables. |
| 5000* | Your Raspberry Pi is throttled due to a bad power supply this can lead to corruption and instability, please replace your charger and cables. |
| 8000* | Your Raspberry Pi is overheating, consider getting a fan or heat sinks. |

Due to how `custom_components` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home Assistant.

Breaking change: this project went from sensor to binary_sensor.

[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[contributors-shield]: https://img.shields.io/github/contributors/custom-components/sensor.rpi_power.svg?style=for-the-badge
[contributors]: https://github.com/custom-components/sensor.rpi_power/graphs/contributors/
[license-shield]: https://img.shields.io/github/license/custom-components/sensor.rpi_power.svg?style=for-the-badge
[maintenance-shield1]: https://img.shields.io/badge/maintainer-Toast%20%40swetoast-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/custom-components/sensor.rpi_power.svg?style=for-the-badge
[releases]: https://github.com/custom-components/sensor.rpi_power/releases
