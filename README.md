# ChatGPT audio transcript and summary

## Up and Running

* Make sure you have python 3.7+ installed on your machine
* Make sure you have pip installed on your machine
* Clone the repo
* `pip install -r requirements.txt`
* Add your audio file somewhere relative to this script (the example file is just in the root)
* Call the `transcribe_and_summarize` function with the path to your audio file, e.g.

```
python api.py transcribe_and_summarize "podcast-excerpt.mp3"
```

You can alternatively call just the `transcribe_audio`, or just the `generate_from_prompt` functions, e.g:

```
python api.py transcribe_audio "podcast-excerpt.mp3"
```

or

```
python api.py generate_from_prompt "Generate the name for a podcast about generative AI"
```

