from flask import Blueprint, jsonify, request
from ..models import Categoria
from ..extensions import db

categorias_bp = Blueprint('categorias_api', __name__)

@categorias_bp.route('/categorias', methods=['POST'])
def criar_categoria():
    dados = request.get_json()

    if not dados or 'nome' not in dados:
        return jsonify({'mensagem': 'O campo nome é obrigatório.'})
    
    nova_categoria = Categoria(nome = dados['nome'])

    db.session.add(nova_categoria)
    db.session.commit()

    return jsonify(nova_categoria.to_dict()), 201

@categorias_bp.route('/categorias', methods=['GET'])
def listar_categorias():
    dados = request.get_json()

    if not dados or 'id' not in dados:
        return jsonify({'mensagem': 'O campo id é obrigatório.'})
    
    # TO-DO: terminar função de listar categorias

# TO-DO: terminar restante das rotas: GET, PUT, PATCH, DELETE
