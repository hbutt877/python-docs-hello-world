from flask import Flask
import openai

app = Flask(__name__)

@app.route("/")
def index():
    return 'Enter prompt in url'

@app.route("/<prompt>")
def dall_e(prompt):
    ss = 'C9V0sXMQcUcG8fYF1/oW8xCpUbBdjmTjxXAEnDJ+33f/1VAvfvvnTT39AEvbr+tRO+0n*h0Nn04g9RXLyYAlSm7HbAA==*42GLI+/rI36BYed8H5990w==*lG/00+obfXnDThUy3UMQLQ=='
    openai.api_key = cryptocode.decrypt(ss, "mypassword")
    response = openai.Image.create(
      model='image-alpha-001',
      prompt=prompt,
      size='1024x1024',
      n=1
    )
    return response['data'][0]['url']
