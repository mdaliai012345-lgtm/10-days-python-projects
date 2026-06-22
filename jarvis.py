import speech_recognition as sr
import webbrowser
import pyttsx3
import time

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    c = c.lower()
    print("Processing:", c)

    if "google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    else:
        speak("Sorry, I did not understand.")

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio)
            print("Command", command)

            if "jarvis" in command.lower():
                print("Wake word detected")
                speak("Hello")
                time.sleep(2)

                with sr.Microphone() as source:
                    print("Jarvis activated...")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print("Command:", command)

                processCommand(command)

        except Exception as e:
            print("Error:", e)