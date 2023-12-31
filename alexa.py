import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.say('My name is Alexa')
engine.runAndWait()
engine.say('What can I do for you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print (command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        print(song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk(time)

    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)

    elif 'what is' in command:
        person = command.replace('what is','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('Sorry, I have a headache')

    elif 'single' in command:
        talk('No, I am in a relationship with wifi')

    elif 'joke' in command:
        jokes = pyjokes.get_joke()
        print(jokes)
        talk(jokes)

    elif 'sleep' in command:
        print('Goodbye. I am going to sleep')
        talk('Goodbye. I am going to sleep')

    else:
        print('PLease say the command again.')
        talk('PLease say the command again.')

while True:
    run_alexa()
