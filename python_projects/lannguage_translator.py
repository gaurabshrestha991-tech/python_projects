from deep_translator import GoogleTranslator

text = input("Enter text to translate: ")

language = input("Translate into which language? (e.g. Spanish, Nepali, French): ")

try:
    translator = GoogleTranslator(source="auto", target=language)
    translated_text = translator.translate(text)
    
    print("\nTranslated text: ", translated_text)
    
except Exception as e:
    print("Translation failed: ", e)
