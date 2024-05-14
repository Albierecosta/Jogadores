from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/api/formar_equipes', methods=['POST'])
def formar_equipes():
    data = request.get_json()
    nomes = data['nomes']

    nomes_ordenados = sorted(nomes, key=lambda x: int(x.split(" - ")[1]), reverse=True)
    

    num_equipes = (len(nomes) + 4) // 5
    equipes = [[] for _ in range(num_equipes)]

    for i, nome in enumerate(nomes_ordenados):
        index_equipe = i % num_equipes
        equipes[index_equipe].append(nome.split(" - ")[0])

    return jsonify({'equipes': equipes})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
