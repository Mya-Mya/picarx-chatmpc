import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from idevice import IDevice
from picarxdevice import PicarxDevice
from controller import Controller
from server import launch
from time import sleep


device:IDevice = PicarxDevice()
controller:Controller = Controller(device)

launch(controller)
