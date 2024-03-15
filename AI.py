import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import json
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
 engine.say(text)
 engine.runAndWait()
 
    
def wishMe():
    hour=(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
         speak("Hello,Good Morning")
         print("Hello,Good Morning")
    elif hour>=12 and hour<18:
         speak("Hello,Good Afternoon")
         print("Hello,Good Afternoon")
    else:
         speak("Hello,Good Evening")
         print("Hello,Good Evening")

         
def takeCommand():
     r=sr.Recognizer()
     with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing...")
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement
wishMe()
print("Loading your personal AI assistant Alice!")
speak("Loading your personal AI assistant Alice!")

if __name__=='__main__':
        
        while True:
         speak("Tell me how can I help you now?")
         
         statement = takeCommand().lower()       
         if statement==0:
            continue
        
         if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Alice is shutting down,Good bye')
            print('your personal assistant Alice is shutting down,Good bye')
            break
        
         if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
         elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

         elif 'open google' in statement:
          webbrowser.open_new_tab("https://www.google.com")
          speak("Google chrome is open now")
          time.sleep(5)

         elif 'open gmail' in statement:
          webbrowser.open_new_tab("gmail.com")
          speak("Google Mail open now")
          time.sleep(5)
            
         elif 'time' in statement:
          strTime=datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"the time is {strTime}")
            
         elif 'news' in statement:
          news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com//home//headlines")
          speak('Here are some headlines from the Times of India,Happy reading')
          time.sleep(6)

         elif "camera" in statement or "take a photo" in statement:
          ec.capture(0,"robo camera","img.jpg")
            
         elif 'search'  in statement:
          statement = statement.replace("search", "")
          webbrowser.open_new_tab(statement)
          time.sleep(5)
          
         elif 'stack overflow' in statement:
             webbrowser.open_new_tab("https://stackoverflow.com")
             speak("Stackoverflow is open now")
             time.sleep(5)
            
         elif "play music" in statement:
          music_dir="C:\\Users\\harsh\\Music\\Music"
          songs=os.listdir(music_dir)
          print(songs)
          
          for i in songs:
           os.startfile(os.path.join(music_dir,i))
           
         elif "play video" in statement:
           video_dir="C:\\Users\\harsh\\Videos\\Captures\\Video"
           video=os.listdir(video_dir)
           print(video)
            
           for i in video:
            os.startfile(os.path.join(video_dir,i))
            
            
         elif 'open code' in statement:
          codepath = "C:\\Users\\harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codepath)
            
         elif 'open microsoft sql' in statement:
          codepath ="C:\\Program Files (x86)\\Microsoft SQL Server Management Studio 18\\Common7\\IDE\\Ssms.exe"
          os.startfile(codepath)
          
         elif 'who are you' in statement or 'what can you do' in statement:
           speak('I am Alice version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia' 
                  'get top headline news from times of india ')
           
           print('I am Alice version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia' 
                  'get top headline news from times of india ')
           


         elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Harshal")
            print("I was built by Harshal")
          
            
         elif "log off" in statement or "sign out" in statement:
          speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
          subprocess.call(["shutdown", "/l"])
time.sleep(3)