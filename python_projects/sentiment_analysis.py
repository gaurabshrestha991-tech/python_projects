from transformers import pipeline

print("Loading AI model....")
analyzer = pipeline("sentiment-analysis")

print("Sentiment Analyzer is ready!")

text = input("\nEnter a sentence: ")

result = analyzer(text)[0]

label = result["label"]
confidence = result["score"] * 100

print(f"Label: {label}")
print(f"Confidence: {confidence:.2f}%")
