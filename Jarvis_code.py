from gettext import install
from pip import main
import os
import webbrowser
import pyttsx3
import datetime
import  speech_recognition as sr
import wikipedia
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour<=0 and hour<12:
        speak("Good Morning!")
        speak("I am Jarvis sir, please tell me how may i help you...")

    elif hour<=12 and hour<18:
        speak("Good Afternoon!")
        speak("I am Jarvis sir, please tell me how may i help you...")

    else:
        speak("Good Evening!")
        speak("I am Jarvis sir, please tell me how may i help you...")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)       
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'hi jarvis' in query:
            speak("Hello Boss, hope you are doing good...")
        elif 'i am fine what about you' in query:
            speak("I am doing good sir, thank you for asking")
        elif 'who am i' in query:
            speak("You are Yash...")
        elif 'who is the president of India' in query:
            speak("The president of India is Narendra Modi, sir...")

        



            
    
        