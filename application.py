from flask import Flask, request, jsonify
import sqlite3
import requests

application = Flask(__name__)


@application.route('/')
def hello_world():
    return "Hello World"

@application.route('/teste')
def whats():
    conexao = sqlite3.connect('testes-aws.db')
    mensagem = request.json
    cursor = conexao.cursor()
    comando = f'INSERT INTO retorno (mensagem) VALUES ("{mensagem}")'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
    return mensagem['hub_challenge']

@application.route('/consulta', methods=['GET'])
def consultar():
    conexao = sqlite3.connect('testes-aws.db')
    cursor = conexao.cursor()
    comando = "SELECT * FROM retorno"
    cursor.execute(comando)
    mensagem = cursor.fetchall()
    cursor.close()
    conexao.close()
    return mensagem

if __name__=='__main__':
    application.run()