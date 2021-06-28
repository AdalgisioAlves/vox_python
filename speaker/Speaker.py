

class SpeakerVox:
    
    def __init__(self,engine) :    
        self.engine = engine

        
    def speaker( self,text ):
        file = self.engine.speak(text)
        print(file)