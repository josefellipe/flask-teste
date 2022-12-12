from flask import Flask, request, jsonify
import requests

application = Flask(__name__)

@application.route('/')
def hello_world():
    return "Hello World"

@application.route('/teste', methods=['GET'])
def whats(mensagem2):
    return mensagem2

if __name__=='__main__':
    application.run()