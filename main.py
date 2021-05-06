import time

import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import webbrowser
from requests import get
import wikipedia
import pywhatkit
import sys
import pyjokes
import newspaper

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#engine.say('I\'m a little teapot...')

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold= 2
        audio = r.listen(source, timeout=5,phrase_time_limit=20)
    try:
        print('Recognizing......')
        query = r.recognize_google(audio,language='En-in')
        print(f"User Said: {query}")
    except Exception as e:
        speak("Say That Again Please....")
        return 'none'
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    dt = time.strftime("%A %B %d")
    tm = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f'Good Morning Paarth Sir. Its {dt}. time is {tm}')
    elif hour>=12 and hour<=18:
        speak(f'Good Afternoon Paarth Sir. Its {dt}. time is {tm}')
    else:
        speak(f'Good Evening Paarth sir. Its {dt}. time is {tm}')
    speak('I am wiki. How May I Help You Today') #Memory 16 GB, Base speed is 3.19 GigaHz, Logical processors is 12, Speed is 1.22 GigaHz,




if __name__ == "__main__":
    wish()
    while True:
    #if 1:
        query = takecommand().lower()

        #logic builing gor task

        if 'open notepad' in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'close notepad' in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'open chrome' in query:
            apath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(apath)

        elif 'close chrome' in query:
            speak("okay sir, closing chrome")
            os.system("taskkill /f /im chrome.exe")

        elif 'open edge' in query:
            spath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(spath)

        elif 'close edge' in query:
            speak("okay sir, closing edge")
            os.system("taskkill /f /im msedge.exe")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'close command prompt' in query:
            speak("okay sir, closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        elif 'Open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "G:\\music"
            song = os.listdir(music_dir)
            rd =random.choice(song)
            os.startfile(os.path.join(music_dir, rd))

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open google" in query:
            speak("What Should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "ip address" in query:
            ip = get('http://api.ipify.org').text
            speak(f"your ip address is{ip}")

        elif "wikipedia" in query:
            speak("searching in wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            #print(results)

        elif "send message" in query:
            speak("what should i write?")
            pywhatkit.sendwhatmsg("+916378242018", "Hii" ,12,42)


        elif "play song on youtube" in query:
            speak("What Should i search on youtube")
            yu = takecommand().lower()
            pywhatkit.playonyt(f"{yu}")

        elif "thanks baby" in query:
            speak("sir, if you call me baby then i have to call your girlfriend. should I ?")

        elif "no thank you wiki" in query:
            speak("Thank you for using me sir, if you need any other help just call me. have a nice day. ")

        elif "thanks wiki" in query:
            speak("Thank you for using me sir, if you need any other help just call me. have a nice day. ")

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==0 :
                music_dir = "G:\\music"
                song = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, song[0]))

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "tell me news" in query:
            nw = newspaper
            speak(nw)

            sys.exit()

        speak("any other thing sir ?")