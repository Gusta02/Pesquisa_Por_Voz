#Criar reconhecimento de voz
import speech_recognition as sr


class Bot_Ouvido():
    rec = sr.Recognizer()
        #quando sai da estrutura with os arquivos / mic é fechado automaticamente

        #print para decobrir qual o mic
        #print(sr.Microphone() .list_microphone_names())

    with sr.Microphone(0) as mic:
        rec.adjust_for_ambient_noise(mic)

        print("pode falar")

        audio = rec.listen(mic)
            
        text = rec.recognize_google(audio,language='pt-BR')

        print(text)
        print(type(text))
        



