from abc import ABC,abstractmethod

class EngineInterface(ABC):

    @abstractmethod
    def configureEngine():
        pass
    
    @abstractmethod
    def speak():
        pass
    