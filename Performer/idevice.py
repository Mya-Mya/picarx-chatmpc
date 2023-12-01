from abc import ABC,abstractmethod

class IDevice(ABC):
    @abstractmethod
    def set_speed(self, v:float)->None:
        """
        Parameters
        ----------
        v : float
            vの値域は[-1,1]とする．v=0は停止，v<0は後退，v>0は前進を意味する． 
        """
    
    @abstractmethod
    def get_distance_to_obstacle(self)->float:
        """
        Parameters
        ----------
        
        Returns
        -------
        distance : float
            前方の障害物までの距離[cm]．
        """

    def get_battery_voltage(self) -> float:
        """
        Parameters
        ----------

        Returns
        -------
        voltage : float
            バッテリーの電圧[V]．
        """
    
    @abstractmethod
    def say(self,s:str)->None:
        """
        Parameters
        ----------
        s : str
        """