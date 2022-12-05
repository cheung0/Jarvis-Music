import speech_recognition as sr 
import webbrowser

r = sr.Recognizer()
url = 'https://www.youtube.com/watch?v=_KzHGbpxMOY&ab_channel=88rising'
url2 = 'https://youtu.be/VjsUHemfqjQ?t=2'

with sr.Microphone() as source:
    audio_data = r.record(source, duration=3)
    print("Recognizing...")

    # for chinese (Taiwan)
    # text = r.recognize_google(audio_data, language='zh-TW')

    text = r.recognize_google(audio_data, show_all=False)
    print(text)
    if text == 'Jarvis play California':
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        webbrowser.get(chrome_path).open(url)
    else:
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        webbrowser.get(chrome_path).open(url2)
