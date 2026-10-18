import speech_recognition as sr
import webbrowser
import pyttsx3

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis....")

while True:
# Listen for the wake word "Jarvis"
# obtain audio from the microphone
    r = sr.Recognizer()



    # recognize speech using Sphinx
    print("recognizing...")
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2 )
        command = r.recognize_google(audio)
        print(command)
    except Exception as e:
        print("Error; {0}".format(e))