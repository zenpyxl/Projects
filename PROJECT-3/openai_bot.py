import openai
openai.api_key = "xyz"
user_inp = input("What do you want to ask?")
completion = openai.ChatCompletion.create(model = "gpt-3.5", messages = [{"role": "user", "content"; user_inp}])
print(completion.choices[0].message.content)