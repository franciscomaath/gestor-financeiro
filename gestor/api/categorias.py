from flask import Blueprint, jsonify, request
from ..models import Categoria
from ..extensions import db

categorias_bp = Blueprint('categorias_api', __name__)

@categorias_bp.route('/categorias', methods=['POST'])
def criar_categoria():
    dados = request.get_json()

    if not dados or 'nome' not in dados:
        return jsonify({'mensagem': 'O campo nome é obrigatório.'}), 400
    
    nova_categoria = Categoria(nome = dados['nome'])

    db.session.add(nova_categoria)
    db.session.commit()

    return jsonify(nova_categoria.to_dict()), 201

@categorias_bp.route('/categorias', methods=['GET'])
def listar_categorias():
    categorias = Categoria.query.all()

    resultado = []
    for c in categorias:
        resultado.append(c.to_dict())

    return jsonify(resultado)
    

@categorias_bp.route('/categorias/<int:categoria_id>', methods=['GET'])
def buscar_categoria_id(categoria_id):
    categoria = Categoria.query.get_or_404(categoria_id)

    return jsonify(categoria.to_dict())


@categorias_bp.route('/categorias/<int:categoria_id>', methods = ['PUT'])
def atualizar_categoria(categoria_id):
    dados = request.get_json()

    if not dados or 'nome' not in dados:
        return jsonify({'mensagem': 'O campo nome é obrigatório.'})
    
    nome = dados['nome']
    categoria = Categoria.query.get_or_404(categoria_id)

    categoria.nome = nome
    db.session.commit()

    return categoria.to_dict()


@categorias_bp.route('/categorias/<int:categoria_id>', methods = ['DELETE'])
def deletar_categoria(categoria_id):
    categoria = Categoria.query.get_or_404(categoria_id)

    db.session.delete(categoria)
    db.session.commit()

    return jsonify({'mensagem': 'Categoria deletada com sucesso.'}), 200