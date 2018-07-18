"""
A sensor platform which detects underruns and capped status from the official Raspberry Pi Kernel.
Minimal Kernel needed is 4.14+
"""
import logging
import voluptuous as vol
from homeassistant.helpers.entity import Entity

__version__ = '0.0.5'

ATTR_DESCRIPTION = 'description'

SYSFILE='/sys/devices/platform/soc/soc:firmware/get_throttled'

ICON = 'mdi:raspberrypi'
PLATFORM_NAME = 'rpi_power'

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    import os
    exist=os.path.isfile(SYSFILE)
    if exist == True:
        add_devices([RaspberryChargerSensor()], True)
    else:
        _LOGGER.critical('Can not read system information, your hardware is not supported.')

class RaspberryChargerSensor(Entity):
    def __init__(self):
        self._state = None
        self._description = None
        self.update()

    def update(self):
        _throttled = open(SYSFILE, 'r').read()[:-1]
        if _throttled == '0':
            self._description = 'No throttling detected'
        elif _throttled == '1000':
            self._description = 'A under-voltage has occurred.'
        elif _throttled == '2000':
            self._description = 'ARM frequency capped has with under-voltage.'
        elif _throttled == '3000':
            self._description = 'ARM frequency capped has with under-voltage.'
        elif _throttled == '4000':
            self._description = 'CPU is throttled due to under-voltage.'
        elif _throttled == '5000':
            self._description = 'CPU is throttled due to under-voltage.'
        else:
            self._description = 'There is a problem with your power supply or system.'
        self._state = _throttled

    @property
    def name(self):
        return 'RPi Power status'

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return ICON

    @property
    def device_state_attributes(self):
        return {
            ATTR_DESCRIPTION: self._description
        }
