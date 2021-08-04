from gtts import gTTS

import subprocess
import ffmpeg

def OtVo(text) :
      
    gTTS(text, lang='ru').save('Jim.ogg')
    subprocess.run('C:\\ffmpeg\\bin\\ffmpeg', '-i', 'Jim.ogg', '-acodec', 'libopus', 'Jim.ogg', '-y')

    with open('Jim.ogg', 'rb') as f:
        data = f.read()

    file = {'audio': ('Message.ogg', data)}
    
    return file

if __name__ == '__main__':
    OtVo('Ублюдок мать твою')