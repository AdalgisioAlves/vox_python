from  speaker.ConfigureEngine import EngineUnix
from  speaker.Speaker  import SpeakerVox
 
texto = """é o senhor
Com todo o meu ser
Com tudo o que sou
Sempre te adorarei


Aclame ao senhor toda a terra e cantemos
Poder, majestade e louvores ao rei
Montanhas se prostrem e rujam os mares
Ao som de teu nome
Alegre te louvo por teus grandes feitos
Firmado estarei, sempre te amarei
Incomparáveis são tuas promessas pra mim
Aclame ao senhor toda a terra e cantemos.


Poder, majestade e louvores ao rei
Montanhas se prostrem e rujam os mares
Ao som de teu nome
Alegre te louvo por teus grandes feitos
Firmado estarei, sempre te amarei
Incomparáveis são tuas promessas pra mim"""

engine = EngineUnix('Pt-Br')
Falar = SpeakerVox(engine)
Falar.speaker(texto)


