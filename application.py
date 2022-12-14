from flask import Flask, request, jsonify
import sqlite3
import requests

application = Flask(__name__)


@application.route('/')
def hello_world():
    return "Hello World"

@application.route('/teste')
def whats():
    url = 'https://graph.facebook.com/v15.0/105066285771857/messages'
    headers = {
        'Authorization' : 'Bearer EAAHdsXNAVH8BAKeABvKvsbkBVg417GKmwgtHO3FcbODOQmlGaC8SdlwJ7bWE0YdQrpU5zqZB7ANV5YhtzBkmtpeUonilcET8jjFCU7210kQEeJtsDxI9iMCFrCqioJhPMg9PHbkD3c2J219H4zC5tBvvM4lZBOtFfDcKxN4IpbHqgevBu4U4WZCDmlZANUt1S3Nn1PFa1J5ARU0A3vQR6Iw63AC8uCUZD',
        'Content-Type': 'application/json'
    }
    body = { 
        "messaging_product": "whatsapp", 
        "to": "", 
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