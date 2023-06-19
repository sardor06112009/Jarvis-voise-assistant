import time
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyautogui
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-uz')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    elif hour>18 and hour<20:
        speak("good evening")
    else:
        speak("good night")
    speak("I am Jarvis sir. How can I help you?")


#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sardor06112009@gmail.com', 'xpiwktyenknwkpvj')
    server.sendmail('sardor06112009@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wish()
    while True:
    #if 1:

        query = takecommand().lower()


def news():
    main_url = 'https://newsapi.org/v2/everything?q=Apple&from=2023-06-15&sortBy=popularity&apiKey=625b3f8219554910933334d8b01123bb'

    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print articles
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")
       
       
        # logic building for tasks

        if 'open notepad' in query:
            npath = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(npath)

        elif 'open CMD' in query:
            cpath = 'C:\\Windows\\System32\\cmd.exe'
            os.startfile(cpath)

        elif 'open sublime text' in query:
            spath = 'C:\\Program Files\\Sublime Text\\sublime_text.exe'
            os.startfile(spath)

        elif 'open telegram' in query:
            tpath = 'C:\\Users\\doniyorov.uz\\AppData\\Roaming\\Telegram Desktop\\telegram.exe'
            os.startfile(tpath)


        elif 'open power shell' in query:
            ppath = 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe'
            os.startfile(ppath)

        elif 'open microsoft word' in query:
            wpath = 'C:\\ProgramData\\Microsoft\\Windows\\Start \\Programs\\Word 2016.exe'
            os.startfile(wpath)

        elif 'open power point' in query:
            opath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint 2016.exe'
            os.startfile(opath)

        elif 'open control panel' in query:
            cpath = 'C:\\Windows\\System32\\control.exe'
            os.startfile(cpath)

        elif 'open anydesk' in query:
            anydesk = 'C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe'
            os.startfile(anydesk)

        elif 'open VS code' in query:
            wpath = 'E:\\Visual_Studio_code\\Code.exe'
            os.startfile(wpath)

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()




        elif 'play music' in query:
            music_dir = 'E:\\musics'
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs))



        elif 'my ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
            #print results

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'watch movie' in query:
            webbrowser.open("www.uzmovi.org")

        elif 'google translate' in query:
            webbrowser.open("translate.google.com")

        elif 'watch english movies' in query:
            webbrowser.open("www.imdb.com")

        elif 'my location' in query:
            webbrowser.open("google.com/maps")

        elif 'open my school' in query:
            webbrowser.open("https://maktab.piima.uz/sign-in?redirectURL=%2Fapps%2Fdiary")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")

        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'send message' in query:
            kit.sendwhatmsg("+998942257557", "Salom ona yaxshimisiz",2,24)
            time.sleep(120)
            speak("message has been sent")

        elif "hello" in query:
            try:
                speak("sir, what should i say?")
                content = takecommand().lower()
                to = "matlubaidiyeva057@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to your mum")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this email to your mum")

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day!")
            sys.exit()
            speak("sir, do you have any other work?")

        elif "you can sleep" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()
            
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = 'E\\musics'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play song on youtube' in query:
            kit.playonyt('see you again')

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "tell me a news" in query:
            speak("please wait sir, feteching the latest news")
            news()



#close applications
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close telegram" in query:
            speak("okay, sir, closing telegram")
            os.system("taskkill /f /im telegram.exe")

        elif "close CMD" in query:
            speak("okay sir, closing CMD")
            os.system("taskkill /f /im cmd.exe")

        elif "close google" in query:
            speak("okay sir, closing google")
            os.system("taskkill /f /im chrome.exe")


# switch window
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

#################################################################################################
#################################################################################################






