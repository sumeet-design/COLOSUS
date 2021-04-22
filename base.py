import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.runAndWait()

head="avinash"
# speak function convert  text to audio
def speak(text):
    engine.say(text)
    engine.runAndWait()
# speak("Intilializing  assistant.....")
speak("Hello There ,please conform your identity")


def work():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening......")
        speak("listening.......")

        audio = r.listen(source)

    try :
        print("thinkingg.....")
        speak("thinking.....")
        query=r.recognize_google(audio)
        print(f"user said: {query}\n")

    except Exception as e:
        print(" repeat again....sorry for inconvenience")
        print(e)
        speak("repeat again....sorry for inconvenience")
        query="none"
    return query

#work()

query=work()
if 'sumit' in query.lower():
    head = 'sumeet'
else:
    head = 'avinash'
def wishme():
    hour = int(datetime.datetime.now().hour)
    #print(hour)
    if hour>=0 and hour <12:
        speak("good morning "+head+".........how may i help you")

    elif hour>=12 and hour<18:
        speak("good afternoon "+head+".........how may i help you")

    else:
        speak("good evening "+head+".........how may i help you")
wishme()
query = work()
#adding functionality for doing basic work................
if 'wikipedia' in query.lower():
    speak('Searching Wikipedia......')
    query=query.replace("Wikipedia","")
    result=wikipedia.summary(query , sentences=2)
    print(result)
    speak(result)
elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")
    # query = work()
elif 'open google' in query.lower():
    webbrowser.open("google.com")
elif 'open amazon' in query.lower():
    webbrowser.open("amazon.com")
elif 'today news' in query.lower():
    webbrowser.open("https://www.indiatoday.in/news.html")
elif  'search' in query.lower():
    x=query.replace("search","")
    webbrowser.open(x)
elif 'play music' in query.lower():
    music="D:\\OLD SONG"
    songs=os.listdir(music)
    os.startfile(os.path.join(music,songs[4]))
elif 'photo' in query.lower():
    photo="D:\\photos"
    images=os.listdir(photo)
    os.startfile(os.path.join(photo,images[1]))
elif 'the time' in query.lower():
    time=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Rimjhim man time is{time}")
query = work()





