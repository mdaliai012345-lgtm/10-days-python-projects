
from openai import OpenAI
client = OpenAI(api_key = '''key'')
while True:
    user = (input("You: "))
    if user.lower() == "bye":
        print("Bot : Good bye!")
        break
    response = client.responses.create(
        model = "gpt-5.5",
        input=user
    )
    print("Bot:",response.output_text)