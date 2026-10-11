from transformers import pipeline
from PIL import Image


print("Loading AI model....")

model = pipeline("image-classification", model="farleyknight-org-username/MNIST_784")

print("Model loaded!")

image_path = input("Enter the image path: ")
