from flask import Flask, request, jsonify
import sqlite3
import requests

application = Flask(__name__)


@application.route('/')
def hello_world():
    return "Hello World"

@application.route('/teste', methods=['POST'])
def whats():
    mensagem = request.json
    return mensagem['hub_challenge']

if __name__=='__main__':
    application.run()