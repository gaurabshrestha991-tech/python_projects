from gtts import gTTs

text = "Hello! Welcome to python text to speech"

tts = gTTs(text=text, lang="en")

tts.save("speech.mp3")

print("Speech Saved as speech.mp3")