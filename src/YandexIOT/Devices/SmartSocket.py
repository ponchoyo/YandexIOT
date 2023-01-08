from YandexIOT.Devices import SmartDevice
from YandexIOT.Devices.SmartDevice import UnsupportedFeature


class SmartLight(SmartDevice):
    def __init__(self, device_json, home):
        super(SmartSocket, self).__init__(device_json, home)

    def turn_on(self):
        """Turn on the light.
        :return: SmartDeviceResponse
        """

        return self._change_state(True)

    def turn_off(self):
        """Turn off the light.
        :return: SmartDeviceResponse
        """

        return self._change_state(False)
