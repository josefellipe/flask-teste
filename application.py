from flask import Flask, request
import requests

application = Flask(__name__)

@application.route('/')
def hello_world():
    mensagem = request.json
    return mensagem

if __name__=='__main__':
    application.run()