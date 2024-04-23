import speech_recognition as sr
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query


if __name__ == '__main__':
    say("Hello I am Nemo A.I")
    print("Listening....")
    text = takeCommand()
    say(text)
    