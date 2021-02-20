import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    
    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("Hi I am Jarvis Sir, How may I Help you")


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print("Say that again sir!")
        return "None"
    
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('maulikbhatt26@gmail.com', 'maulik123456bhatt12345')
    server.sendmail('maulikbhatt26@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()


        if 'wikipedia' in query:
            
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'my website' in query:
            webbrowser.open("http://white-hat.epizy.com/")

        elif 'play movie' in query:
            movie_dir = 'E:\\movie'
            movie = os.listdir(movie_dir)
            print(movie)
            os.startfile(os.path.join(movie_dir, movie[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Sir, the time is {strtime}")

        elif 'open gta' in query:
            gamepath = "E:\\games\\Grand Theft Auto V\\GTA5.exe"
            os.startfile(gamepath)

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "maulikbhatt26@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry I am not able to send email ")

       






































