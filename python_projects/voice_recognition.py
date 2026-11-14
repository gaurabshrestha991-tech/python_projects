import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    
    print("Adjusting microphone....")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    
    print("listening ... Speak something!")
    
    try:
        
        audio = recognizer.listen(source)
        
        print("Recognizer your voice....")
        
        text = recognizer.recognize_google(audio)
        
        print("you said:", text)
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
        
    except sr.RequestError:
        print("Could not connect to the recognition service.")
        
        
