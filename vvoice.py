import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def talk(command):
    engine=pyttsx3.init()
    engine.setProperty('voice', voice[0].id)
    engine.say("playing "+ command)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:    
        speak("Good Morning!")

    elif hour>=12 and hour<18:    
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Diego here . how can i help you sir!!!")


def takecommand():
# it takes microphone input from the user and returns string output.
        listner =sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                listner.pause_threshold = 1
            # pause_threshold means we can increase the the time means if we pause it doesn't stop listening it will wait for 1 sec.
                voice=listner.listen(source)

        #  try:
            print("Recognizing...")   
            query =listner.recognize_google(voice, language='en-in')
            print(f"user said: {query}\n")


        except Exception as e:
            print("say that again please...")
            return "None"
        return query
pass


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

    
        elif 'joke' in query:
            speak("jokes for today are")
            speak(pyjokes.get_joke())


        elif 'open youtube' in query:
            speak("entertainment is also important sir . thanks for asking me to open it i m also bored , and it is opening just wait a second sir")
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")


        elif "time" in query:
            speak("sir i have sticked the time on your teminal")
            os.system("time /T")


        elif 'open code' in query:
            speak("opening VS-code")
            codepath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)


        elif 'open notepad'in query:
            speak("opening notepad")
            notepath = "D:\\CODING\\Notepad++\\notepad++.exe"
            os.startfile(notepath)


        elif "weather" in query:
            speak("sir the weather will be displayed on your screen just wait a second")
            os.system("start bingweather:")


        elif "calendar" in query:
            speak("opening calender")
            os.system("start outlookcal:")


        elif "camera" in query:
            speak("opening camera")
            os.system("start microsoft.windows.camera:")


        elif "paint" in query:
            speak("opening paint")
            os.system("mspaint")


        elif "settings" in query:
            speak("opening settings")
            os.system("start ms-settings:")

            
        elif ("screenshot" in query) or ("snip" in query) or ("crop" in query):
            speak("opening snippingTool")
            os.system("SnippingTool")


        elif  ("check" in query) or ("mail" in query) or ("inbox" in query) or ("email" in query) or ("gmail" in query):
            speak("opening mail")
            os.system("start outlookmail:")


        elif "calculator" in query:
            speak("opening calculator")
            os.system("calc")


        elif 'opera'in query:
            speak("opening opera")
            notepath = "C:\\Users\\aman\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.startfile(notepath)


        elif 'cyberpunk'in query:
            speak("opening cyberpunk")
            notepath = "D:\\Games\\Cyberpunk 2077\\bin\\x64\\Cyberpunk2077.exe"
            os.startfile(notepath)


        elif 'nfs'in query:
            speak("opening nfs heat")
            notepath = "D:\\GAMES\\Need for Speed Heat\\NeedForSpeedHeat.exe"
            os.startfile(notepath)


        elif 'assassin creed'in query:
            speak("opening assassin creed valhalla")
            notepath = "D:\\GAMES\\Assassin's Creed Valhalla\\ACValhalla.exe"
            os.startfile(notepath)


        elif 'exit' in query:
            speak("Thanks for giving me your time sir")
            exit()