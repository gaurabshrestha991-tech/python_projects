import time

text = "Python is a simple and powerful programming language."

print("Typing Speed Test")
print("-----------------")
print("Type the following sentence")
print(text)

input("\nPress Enter to start....")

start = time.time()
typed = input("\nType here:")
end = time.time()

time_taken = end - start
words = len(typed.split())
wpm = (words / time_taken) * 60

correct = sum(a == b for a, b in zip(text, typed))
accuracy = (correct / len(text)) * 100

print("\n--- Result ---")
print(f"Time Taken : {time_taken:.2f} seconds")
print(f"Speed      : {wpm:.2f} WPM")
print(f"Accuracy   : {accuracy:.2f}%")

if typed == text:
    print("Status       : Correct Text")
else:
    print("Status       : Incorrect Text")
    print("\nOrginal Text:")
    print(text)
    print("\nYour Text: ")
    print(typed)
    
    