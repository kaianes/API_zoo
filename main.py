from flask import Flask, request, jsonify, make_response
from zoo import Animal, Recinto, ReceberVisitantes
from bd import animais

app = Flask(__name__)

# Listas para armazenar animais e recintos (simulando um banco de dados)
lista_animais = animais
lista_recintos = []

# Operações de criação de animais
@app.route('/animais', methods=['POST'])
def criar_animal():
    data = request.json
    nome = data.get('nome')
    especie = data.get('especie')
    novo_animal = Animal(nome, especie)
    lista_animais.append(novo_animal)
    return make_response(jsonify({'message': 'Animal criado com sucesso'}), 201)

# Operações de criação de recintos
@app.route('/recintos', methods=['POST'])
def criar_recinto():
    data = request.json
    nome = data.get('nome')
    especie = data.get('especie')
    novo_recinto = Recinto(nome, especie)
    lista_recintos.append(novo_recinto)
    return make_response(jsonify({'message': 'Recinto criado com sucesso'}), 201)

# Operações de alimentação de animais
@app.route('/animais/<nome>/alimentar', methods=['PUT'])
def alimentar_animal(nome):
    for animal in lista_animais:
        if animal.nome == nome:
            animal.alimentar()
            return make_response(jsonify({'message': 'Animal alimentado com sucesso'}), 200)
    return make_response(jsonify({'message': 'Animal não encontrado'}), 404)

# Operações de recebimento de visitantes
@app.route('/receber_visitantes', methods=['POST'])
def receber_visitantes():
    data = request.json
    num_visitantes = data.get('num_visitantes')
    zoológico = ReceberVisitantes()
    zoológico.atrair_visitantes(num_visitantes)
    zoológico.receber_dinheiro()
    return make_response(jsonify({'message': 'Visitantes atraídos e dinheiro recebido'}), 200)

# Operação para listar todos os animais
@app.route('/animais', methods=['GET'])
def listar_animais():
    lista_animais = [{'nome': animal.nome, 'especie': animal.especie} for animal in lista_animais]
    return make_response(jsonify({'animais': lista_animais}), 200)

if __name__ == '__main__':
    app.run(debug=True)
