from transformers import pipeline

model = pipeline("image-classification", model= "microsoft/resnet-50")

photo = input("Enter the photo path: ")

results = model(photo)

print("Prediction: ", results[0]["label"])
print("Confidence: ", round(results[0]["score"] * 100, 2) "%")
