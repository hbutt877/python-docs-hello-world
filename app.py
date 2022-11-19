from flask import Flask
import openai

app = Flask(__name__)

@app.route("/")
def index():
    return 'Enter prompt in url'

@app.route("/<prompt>")
def dall_e(prompt):
    openai.api_key = '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'
    response = openai.Image.create(
      model='image-alpha-001',
      prompt=prompt,
      size='1024x1024',
      n=1
    )
    return response['data'][0]['url']
