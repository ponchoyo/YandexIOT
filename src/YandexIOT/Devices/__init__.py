from .SmartDevice import SmartDevice
from .SmartLight import SmartLight
from .SmartVacuum import SmartVacuum
from .SmartSocket import SmartSocket


TYPES = {
    "devices.types.light": SmartLight,
    "devices.types.vacuum_cleaner": SmartVacuum,
    "devices.types.socket": SmartSocket,
}
