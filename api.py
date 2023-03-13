import os
import sys
import dotenv
import openai

config = dotenv.dotenv_values(".env")
openai.api_key = config['OPENAI_API_KEY']

# COMMAND LINE USAGE:
# python api.py generate_from_prompt "This is a prompt"

def generate_from_prompt(promptString):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=promptString,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  print(response.choices[0].text)

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])