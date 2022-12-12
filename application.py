from flask import Flask, request, jsonify
import requests

application = Flask(__name__)

@application.route('/')
def hello_world():
    return "Hello World"

@application.route('/teste', methods=['POST'])
def whats():
    mensagem = request.json
    mensagem = f"Olá {mensagem['nome']}"
    return mensagem

if __name__=='__main__':
    application.run()