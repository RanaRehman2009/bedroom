import speech_recognition as sr
import pyttsx3,pywhatkit,datetime,wikipedia,pyjokes,webbrowser,pyautogui

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            global command
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'video search' in command: 
        song = command.replace('video search', '')
        song = song.replace('', '+')
        talk('playing ' + song)
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'bob who is' in command:
        person = command.replace('bob who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        time = datetime.datetime.now().strftime('%Y-%m-%d')
        talk(f'The date is {time}')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'play' in command:
        pyautogui.press('playpause')
    elif 'pause' in command:
        pyautogui.press('playpause')
    elif 'exit' in command:
        exit()
    else:
        pass
while True:
    run_alexa()