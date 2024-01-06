from importlib.util import spec_from_file_location
from multiprocessing.spawn import import_main_path
from time import time
from turtle import speed
import webbrowser
import pyttsx3
import wikipedia
import pyaudio
import os
import smtplib
import datetime as dt
import speech_recognition as sr
import pyautogui
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def CheckAuthor():
    speak("Please Tell Me Password:")
    

def wishme():
    hour=(dt.datetime.now().hour)
    if hour > 12 and hour < 18:
        speak("GOOD AFTERNOON")
    if hour > 5 and hour < 12 :
        speak("GOOD MORNING")
    if hour >18 :
        speak("GOOD EVENING")
 
def navigate_to_location(directory_path):
    # Change the current working directory to the specified path
    os.chdir(directory_path)
    # Print the current working directory to verify the location change
    print("Current working directory:", os.getcwd())

def take_screenshot(file_path):
    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Add a timestamp to the file name
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"screenshot_{timestamp}.png"
    
    # Save the screenshot to the specified file path
    screenshot.save(os.path.join(file_path, file_name))
    print("Screenshot saved:", os.path.join(file_path, file_name))



def main():
    wishme()
    print("---------------------------------------------------------")
    print("-------------------------Jarvis--------------------------")
    print("---------------------------------------------------------")
    print("Hello This is Jarvis ....Ready in Your service sir..")
    speak("hello This is Jarvis ....Ready in Your service sir..")
    while True:
    # if 1:
        query = takeCommands().lower()
        # Logic for executing tasks based on query
        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            print("Playing Music")
            speak("Playing music")
            webbrowser.open("https://www.youtube.com/playlist?list=PLumVt4msMU8LxSXc3omd6YvCGNNh3-dgq")   
        
        elif 'Pause the song' in query:
            pyautogui.press('space')

        elif "screenshot" in query:
            take_screenshot("F:\\Final Year Project\\try\\new")  # Replace with your desired file pat
        
        elif 'sign off' in query:
            
            print("Signing off sir....")
            speak("Signing off sir....")
            exit()
if __name__=="__main__":
    main()