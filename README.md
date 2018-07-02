# rpi_charger
  
![Version](https://img.shields.io/badge/version-0.0.1-green.svg?style=for-the-badge) ![mantained](https://img.shields.io/maintenance/yes/2018.svg?style=for-the-badge)   
A sensor that checks your Raspberry Pi charger so its not giving you undervoltage.
  
To get started put `/custom_components/sensor/rpi_charger.py` here:  
`<config directory>/custom_components/sensor/rpi_charger.py`  
  
**Example configuration.yaml:**
```yaml
sensor:
  platform: rpi_charger
```
**Configuration variables:**  
  
key | description  
:--- | :---  
**platform (Required)** | The platform name.  
  
  
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).  
***
Due to how `custom_componentes` are importerd, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.