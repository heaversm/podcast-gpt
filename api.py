import os
import sys
import dotenv
import openai

config = dotenv.dotenv_values(".env")
openai.api_key = config['OPENAI_API_KEY']

# USAGE: python api.py generate_from_prompt "This is a prompt"

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

#USAGE: python api.py transcribe_audio "path/to/file.mp3"
def transcribe_audio(fileLoc):
  audio_file= open(fileLoc, "rb")
  transcript = openai.Audio.transcribe("whisper-1", audio_file)
  print(transcript.text)
  return transcript.text

def transcribe_and_summarize(fileLoc):
  transcript = transcribe_audio(fileLoc)
  if transcript is not None:
    prompt = "Summarize the following audio transcript. Provide the topic of conversation as well as any key people mentioned or highlights:\n\n" + transcript
    summary = generate_from_prompt(prompt)
    print(summary)

   
if __name__ == '__main__':

  if len(sys.argv) > 2:
    globals()[sys.argv[1]](sys.argv[2])
  else:
    print("Please provide a function to call as well as the function argument")
  
  

