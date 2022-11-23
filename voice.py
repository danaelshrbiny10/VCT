'''from googletrans import Translator

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"AK47 Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query

def Translate():
	speak("what I should Translate??")
	sentence = takeCommand()
	trans = Translator()
	trans_sen = trans.translate(sentence,src='en',dest='ca')
	print(trans_sen.text)
	speak(trans_sen.text)

Translate()
'''


import speech_recognition as sr

def main():
 
    r = sr.Recognizer()
    
    # for microphone users
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Please say something")
 
        audio = r.listen(source)
 
        print("Recognizing Now .... ")
 
 
        # recognize speech using google
        try:
            print("You have said \n" + r.recognize_google(audio))
            print("Audio Recorded Successfully \n ")
 
 
        except Exception as e:
            print("Error :  " + str(e))
 
 
 
        # record audio
        sound = "recordAudio/recordAudio.wav"
        with open(sound, "wb") as f:
            f.write(audio.get_wav_data())



        # Convert Recorded Audio To Text
        sound = "recordAudio/recordAudio.wav"
        with sr.AudioFile(sound) as source:
            r.adjust_for_ambient_noise(source)

            print("Converting Audio To Text ..... ")

            audio = r.listen(source)

        
        try:
            print("Converted Audio Is : \n" + r.recognize_google(audio))

    
        except Exception as e:
            print("Error {} : ".format(e) )



if __name__ == "__main__":
    main()
