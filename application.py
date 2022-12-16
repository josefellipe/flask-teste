from flask import Flask, request, jsonify
import sqlite3
import requests

application = Flask(__name__)

chave1 = 'Bear'
chave2 = 'er '
chave3 = 'EAAHdsXNAVH8BAPsvbNCBZA1oHYlkZAhivN60QNxbr068Gk0RMxJ9XhHDO8SHolX6XBcW9VkLrOVIpRP4p9J'
chave4 = 'C7pbtLpSLj0JreKC0vcrRHyBsxPCqSEYs3Foiipn9syTGDtEnJ2F8uC7a4Eqycoa54XVt3Vz0ONig1xpqawO13juoVEC09nTvyFadUvKfc4pMFMgN21np3XGOQZAUxcgz2f3BPFUsGIZD'

@application.route('/', methods=['GET'])
def hello_world():
    mensagem = request.query_string
    conexao = sqlite3.connect('testes-aws.db')  
    cursor = conexao.cursor()
    comando = f'INSERT INTO retorno (mensagem) VALUES ("{mensagem.json}")'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
    return mensagem

@application.route('/teste')
def whats():
    url = 'https://graph.facebook.com/v15.0/105066285771857/messages'
    headers = {
        'Authorization' : chave1+chave2+chave3+chave4,
        'Content-Type': 'application/json'
    }
    body = { 
        "messaging_product": "whatsapp", 
        "to": "5551997613120", 
        "type": "template", 
        "template": { 
            "name": "hello_world", 
            "language": { 
                "code": "en_US" 
            } 
        } 
    }
    mensagem = requests.post(url=url, headers=headers, json=body)
    conexao = sqlite3.connect('testes-aws.db')  
    cursor = conexao.cursor()
    comando = f'INSERT INTO retorno (mensagem) VALUES ("{mensagem.json()}")'
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