from peripherals.sensors.tds_sensors.tds_config import TDSConfig

class TDSConfigExtension(TDSConfig):
    schedule_enabled: bool = True
    schedule_interval_seconds: int = 15