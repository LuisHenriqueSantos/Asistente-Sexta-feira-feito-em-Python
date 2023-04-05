import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import flask

audio = sr.Recognizer()
maquina = pyttsx3.init()


def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'sexta-feira' in comando:
                comando = comando.replace('sexta-feira', '')
                maquina.say(comando)
                maquina.runAndWait()
    except:
        print('Microfone não esta ok')
    return comando


def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procurar por' in comando:
        procurar = comando.replace('procurar por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 3)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando musica')
        maquina.runAndWait()


comando_voz_usuario()
