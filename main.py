from flask import Flask
from flask import request
import requests

app = Flask(__name__) 

@app.route("/", methods = ["Get"]) 
def home():
  url = request.args.get("vtt")
  r = requests.get(url, allow_redirects=True)
  r.headers.add("Access-Control-Allow-Origin", "*")
  return r.content

if __name__ == '__main__':
  app.run(port=5000)
