from googletrans import Translator
from gtts import gTTS
from pygame import mixer

source = "en"
destination="fr"
intext = "How amazing"
filename = "file.mp3"
translator = Translator()
sound = gTTS(translator.translate(intext, src= source, dest= destination).text, lang =destination)
sound.save(filename)
mixer.init()
mixer.music.load(filename)
mixer.music.play()
