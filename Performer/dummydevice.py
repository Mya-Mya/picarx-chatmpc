from idevice import IDevice


class DummyDevice(IDevice):
    def set_speed(self, v: float) -> None:
        print(f"Setting speed: {v}")

    def get_distance_to_obstacle(self) -> float:
        import random
        return random.uniform(-5, 30)

    def get_battery_voltage(self) -> float:
        import random
        return random.uniform(0, 10)

    def say(self, s: str) -> None:
        print(f"Speech: {s}")
