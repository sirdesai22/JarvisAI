import speech_recognition as sr
import sys
import cv2
import pyttsx3
import os
import pywhatkit
import random
from gtts import gTTS

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

# Define a function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to get speech input from the user
def get_audio():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
            return None

# Define a function to handle user commands
def handle_command(command):
    if 'hello' in command:
        speak('Hello, how can I assist you?')
    elif 'how are you' in command:
        speak('I am fine, thank you for asking.')
    elif 'what is your name' in command:
        speak('My name is Jarvis, your personal assistant.')
    elif 'open notepad' in command:
        speak('Opening Notepad')
        os.system('notepad.exe')
    elif 'open calculator' in command:
        speak('Opening Calculator')
        os.system('calc.exe')
    elif 'play' in command:
        pywhatkit.playonyt(command)
        speak('Playing', command)
        # speak('Playing Music')
        # music_dir = 'C:\\Music\\'
        # songs = os.listdir(music_dir)
        # os.startfile(os.path.join(music_dir, random.choice(songs)))
    elif 'stop' or 'exit' or 'bye' in command:
        speak('Goodbye!')
        exit()
    else:
        speak('Sorry, I didn\'t understand that command.')

# Main loop
img = cv2.imread("E:\Codes\Python\JarvisAi\listening.png", cv2.IMREAD_ANYCOLOR)
cv2.namedWindow("Jarvis", cv2.WND_PROP_FULLSCREEN)          
cv2.setWindowProperty("Jarvis", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("Jarvis", img)
speak('Hello, I am Jarvis your personal AI assistant')

while True:
    speak('How can I assist you?')
    command = get_audio()
    if command:
        handle_command(command)

cv2.destroyAllWindows() # destroy all windows
