from gtts import gTTS

def OtVo(text) :
    
    ot_voice = gTTS(text, lang='ru')
    ot_voice.save('Jim.ogg')

    return

if __name__ == '__main__':
    OtVo('Ублюдок мать твою')