from typing import Optional
from idevice import IDevice
from controlparam import ControlParam
from time import sleep
from threading import Thread


class Controller:
    def __init__(self, device: IDevice, param: Optional[ControlParam] = None) -> None:
        self.device = device
        self.update_param(param)
        self.is_cloop_running = False
        self.cloop_thread = None
        self.b = 2.0

    def update_param(self, param: Optional[ControlParam]):
        self.param = param or ControlParam()

    def start(self):
        self.stop()
        self.is_cloop_running = True
        self.cloop_thread = Thread(target=self.cloop)
        self.cloop_thread.start()

    def cloop(self):
        while self.is_cloop_running:
            sleep(0.05)
            d = self.device.get_distance_to_obstacle()
            delta_plus_b = self.param.delta+self.b
            if delta_plus_b < d:
                v = (d-delta_plus_b)*self.param.gamma
            elif self.param.delta < d:
                v = 0
            else:  # d <= Δ
                v = (d-self.param.delta)*self.param.gamma
            self.device.set_speed(v)

    def stop(self):
        self.is_cloop_running = False
        if self.cloop_thread:
            self.cloop_thread.join()
        self.device.set_speed(0.0)
