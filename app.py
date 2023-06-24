from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/api/formar_equipes', methods=['POST'])
def formar_equipes():
    nomes = request.get_json()['nomes']
    random.shuffle(nomes)

    tamanho_equipe = 5

    num_equipes = len(nomes) // tamanho_equipe
    equipes = [nomes[i:i+tamanho_equipe] for i in range(0, num_equipes * tamanho_equipe, tamanho_equipe)]
    
    if len(nomes) % tamanho_equipe != 0:
        equipes.append(nomes[num_equipes * tamanho_equipe:])

    return jsonify({'equipes': equipes})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
