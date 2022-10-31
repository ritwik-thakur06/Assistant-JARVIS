# PACKAGES
import datetime
import pyttsx3  #text-to-speech conversion package
import speech_recognition as sr   # for microphone input from user
#Install PyAudio package later on as it requires to take audio access from microphone
import wikipedia 
import webbrowser
import os
import smtplib

# INITIALIZATIONS:

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')
# print(voices[0].id)  
engine.setProperty('voice', voices[0].id)


# FUNCTIONS:

def speak(audio):
    engine.say(audio)  
    engine.runAndWait()  


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis sir. Please tell me how may I help you")


def takeCommand():
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

# Note: To access this email feature by using your Gmail account is not possible now, as the less secure app access has been removed by Google, which is the imp part to send emails
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email@gmail.com', 'your-pass')
    server.sendmail('your-email@gmail.com', to, content)
    server.close()

# MAIN FUNCTION:
if __name__ == "__main__":
    #FUNCTION_CALLED:
    
    #uncomment the below code
    #speak("Ritwik is a gentlemen. He always respect others. He build this assistant to make others life easier. You can give me some more input");

    wishMe()

    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "") #here wikipedia is the string that we replace with empty ""
            results = wikipedia.summary(query, sentences=2)  #here wikipedia is our import module
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open cricbuzz' in query:
            webbrowser.open("cricbuzz.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open codewithharry' in query:
            webbrowser.open("codewithharry.com")

        elif 'open crichd' in query:
            webbrowser.open("https://crichd.vip/web")

        elif 'open hotstar' in query:
            webbrowser.open("hotstar.com")

        elif 'open sonyliv' in query:
            webbrowser.open("https://sonyliv.com/")

        elif 'play music' in query:
            # music_dir = "C:\\Users\\Ritwik Thakur\\Music"
            music_dir = "(Enter your music folder path just like above)"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}\n")

        elif 'open code' in query:
            # codePath = "D:\\Program_Files\\Microsoft VS Code\\Code.exe"
            codePath = "(Enter your vs code path just like above)"
            os.startfile(codePath)

        elif 'email to ritwik' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sender-email@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir! I am not able to send this email.")


        elif 'bye' or 'quit' or 'shutdown' or 'shut' in query:
            speak("Bye sir! have a nice day. I'll see you later")
            exit()
            
      
