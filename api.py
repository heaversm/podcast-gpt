import os
import dotenv
import openai

config = dotenv.dotenv_values(".env")
openai.api_key = config['OPENAI_API_KEY']

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a tagline for an ice cream shop",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].text)