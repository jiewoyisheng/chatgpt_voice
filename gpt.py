import openai

openai.api_key = "sk-xxx"  #API Key

def getgpt(msg):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=msg,
                                        max_tokens=2048,
                                        temperature=1.2)
    return completion.choices[0].message.content
