from dataclasses import dataclass


@dataclass
class ControlParam:
    delta: float = 10.0
    gamma: float = 0.1
