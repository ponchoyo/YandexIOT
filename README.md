# YandexIOT
Library for controlling Yandex Smart Devices in Python.

## Install

```shell
pip install YandexIOT
```

## Documentation
It's not completed still, but some useful information you can find in our [wiki](https://github.com/Artingl/YandexIOT/wiki)

## Example

```python
from YandexIOT import SmartHome

home = SmartHome("YOUR_TOKEN_HERE")

light = home.get_device_by_name("Лампочка")
light.turn_on()

```
