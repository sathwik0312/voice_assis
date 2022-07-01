import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os 
import pyautogui 
import psutil
import pyjokes

engine = pyttsx3.init()


def speak(audio): #created a function to speak 
    engine.say(audio) 
    engine.runAndWait()

#speak("this is friday and good day")

voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id) #0-for male voice and 1-for female voice 


def date(): #create da function to speak out current date
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak("current date is:")
    speak(date)
    speak(month)
    speak(year)

#date() - audio will be played by calling this function

def time(): #created a function to speak out the current time.
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(" and the time is:")
    speak(Time)

#time()

def wishme():
    speak("Welcome back , KARTHIK ")
    #date()
    #time()
    hour = datetime.datetime.now().hour #wishing at a particular hour.
    
    if hour>=6 and hour<12:
        speak("Good morning , Karthik")
    elif hour>=12 and hour<18:
        speak("Good afternoon, Karthik")
    elif hour>=18 and hour<24:
        speak("Good evening,karthik")
    else:
        speak("Good night, karthik")
    
    speak("how can i help you ??")

#wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing ... ")
        query = r.recognize_google(audio,'en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Say it again..please.")

        return "none"

    return query

#takeCommand()

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login()
    server.login("ambekar.karthik1808@gmail.com",to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\~krish~\\Desktop\\aa\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+ usage)

    battery = str(psutil.sensors_battery())
    speak("battery is at")
    print(battery.percent) #cant speak but can display for now.

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":

    wishme()

    query = "time"
    print(query)

    if "time" in query:
        time() 
    elif "date" in query:
        date()
    elif "offline" in query:
        quit()
    elif "wikipedia" in query:
        speak("Searching")
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences = 2)
        speak(result)
    elif "send email" in query:
        try:
            speak("what should I say?")
            content = "this is a test email"
            to = "b162197@rgukt.ac.in"
            sendmail(to, content)
            speak(content) #due to credential issues cant able to send.

        except Exception as e:
            speak(e)
            speak("unable to send mail")
    elif "open google" in query:
        speak("what should I say??")
        wb.open("google.com") #opens in internet explorer.
        #python -m webbrowser -t "http://www.google.com" simple comment to open google from terminal.
    elif "logout" in query:
        os.system("shutdown - 1")

    elif "shutdown" in query:
        os.system("shutdown /s /t 1")
    
    elif "restart" in query:
        os.system("shutdown /r /t 1")
    elif "play songs" in query:
        songs_dir = "C:\\Users\\~krish~\\Music\\MY SONGS" #could not find path specified.
        songs = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir,songs[1]))
    elif "remember that" in query:
        speak("what should I remember ??")
        data = "do this n times after me"
        speak("you said"+ data)
        remember = open("data.txt","w")
        remember.write(data)
        remember.close()
    elif "do you know anything" in query:
        remember = open("data.txt","r")
        speak("you said me to remember"+remember.read())
    elif "screenshot" in query:
        screenshot()
        speak("I took screenshot")
    elif "cpu" in query:
        cpu()
    elif "jokes" in query:
        jokes()

    