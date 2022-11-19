from flask import Flask

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
