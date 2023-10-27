from datetime import timedelta
from homeassistant.helpers.entity import Entity, PlatformEntity
from .const import BASE_URL, SENSOR_1, SENSOR_2, SENSOR_3, SCAN_INTERVAL

def setup_platform(hass, config, add_entities, discovery_info=None):
    sensors = [
        YROTestSensor(SENSOR_1),
        YROTestSensor(SENSOR_2),
        YROTestSensor(SENSOR_3)
    ]
    add_entities(sensors, True)

class YROTestSensor(PlatformEntity):  # Notez le changement de la classe de base
    def __init__(self, name):
        self._name = name
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        response = requests.get(BASE_URL)
        data = response.json()

        if self._name == SENSOR_1:
            self._state = data['name']
        elif self._name == SENSOR_2:
            self._state = data['version']
        elif self._name == SENSOR_3:
            self._state = data['rootUrl']

    # Définir l'intervalle de scan pour cette plateforme
    @property
    def scan_interval(self):
        return SCAN_INTERVAL
