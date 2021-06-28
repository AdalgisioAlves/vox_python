from .interface import InterfaceEngine
import datetime, os
from gtts import gTTS

class EngineUnix(InterfaceEngine.EngineInterface):
   
    
    def __init__(self,idioma,engine =None):
        self.idioma = idioma
        self._engineUnix = engine
        self.configureEngine()  
        
    def configureEngine(self):
        self._engineUnix = gTTS
    
    def speak(self,texto):
        fileLocal =  os.getcwd() + '/'+'mp3/' 
        x = datetime.datetime.now()
        fileName  = 'Arq_' + x.strftime("%d%m%Y%m%S")+'.mp3'
        
        tts = self._engineUnix(texto,lang=self.idioma)
        tts.save(fileLocal+fileName)
        return fileLocal+fileName

        
        
    
        


