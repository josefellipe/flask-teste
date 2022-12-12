from flask import Flask, request, jsonify
import sqlite3
import requests

application = Flask(__name__)
conexao = sqlite3.connect('testes-aws.db')

@application.route('/')
def hello_world():
    return "Hello World"

@application.route('/teste', methods=['POST'])
def whats():
    mensagem = request.json
    cursor = conexao.cursor()
    comando = f'INSERT INTO retorno (mensagem) values ("{mensagem}")'
    cursor(comando)
    conexao.commit()
    return mensagem['hub_challenge']

if __name__=='__main__':
    application.run()