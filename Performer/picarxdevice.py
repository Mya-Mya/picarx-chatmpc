from idevice import IDevice
from picarx import Picarx
from robot_hat.utils import run_command


class PicarxDevice(IDevice):
    def __init__(self):
        self.px = Picarx()

    def set_speed(self, v: float) -> None:
        self.px.backward(int(v*100))

    def get_distance_to_obstacle(self) -> float:
        return self.px.ultrasonic.read()

    def say(self, s: str) -> None:
        command = f"sudo echo '{s}' " +\
            "| open_jtalk " +\
            "-x /usr/local/dic " +\
            "-m /home/inouelab/MMDAgent_Example-1.8/Voice/mei/mei_normal.htsvoice " +\
            "-ow /dev/stdout " +\
            "| sudo aplay"
        run_command(command)
