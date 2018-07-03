# rpi_power
  
![Version](https://img.shields.io/badge/version-0.0.2-green.svg?style=for-the-badge) ![mantained](https://img.shields.io/maintenance/yes/2018.svg?style=for-the-badge)   
A sensor that checks your Raspberry Pi charger so its not giving you undervoltage.
  
To get started put `/custom_components/sensor/rpi_power.py` here:  
`<config directory>/custom_components/sensor/rpi_power.py`  
  
**Example configuration.yaml:**
```yaml
sensor:
  platform: rpi_power
```
**Configuration variables:**  
  
key | description  
:--- | :---  
**platform (Required)** | Kernel 4.14+  
  
  
https://creativecommons.org/licenses/by-sa/4.0/  
***
Due to how `custom_componentes` are importerd, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.