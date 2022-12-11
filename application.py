from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    mensagem = request.json
    return mensagem

if __name__=='__main__':
    app.run()