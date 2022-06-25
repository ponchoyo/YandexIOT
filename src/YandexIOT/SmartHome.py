import YandexIOT.Devices
import typing as t
import requests


class SmartHome:
    def __init__(self, token: str, token_type="Bearer"):
        self.token = token
        self.token_type = token_type

        self.headers = {
            "Authorization": f"{self.token_type} {self.token}"
        }

    def get_home_info(self) -> t.Tuple[bool, dict]:
        req = requests.get("https://api.iot.yandex.net/v1.0/user/info", headers=self.headers)

        data = None
        result = req.status_code == 200

        if result:
            data = req.json()

        return result, data

    def get_devices(self) -> t.List[YandexIOT.Devices.SmartDevice]:
        info = self.get_home_info()
        devices = []

        if info[0]:
            for device in info[1]['devices']:
                if device['type'] not in YandexIOT.Devices.TYPES:
                    continue

                device_class = YandexIOT.Devices.TYPES[device['type']](device, self)
                devices.append(device_class)

        return devices

    def get_device_by_name(self, device_name):
        device = None
        for i in self.get_devices():
            if i.get_name() == device_name:
                device = i
                break

        return device

    def get_device_by_id(self, device_id):
        device = None
        for i in self.get_devices():
            if i.get_id() == device_id:
                device = i
                break

        return device
