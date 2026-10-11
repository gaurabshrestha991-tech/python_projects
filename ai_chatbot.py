from openai import OpenAI

client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Answer clearly."
    }
]

print("AI Chatbot is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    if not user_input:
        continue

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        print("Bot is thinking...")

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=messages
        )

        reply = response.output_text

        if reply:
            print("Bot:", reply, "\n")

            messages.append({
                "role": "assistant",
                "content": reply
            })
        else:
            print("The AI returned an empty response.")

    except Exception as error:
        print("API Error:", error)
        messages.pop()
