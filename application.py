from flask import Flask, request
import requests

application = Flask(__name__)

@application.route('/')
def hello_world():
    try:
        mensagem = request.json
        return mensagem
    except:
        return "Hello World"

if __name__=='__main__':
    application.run()