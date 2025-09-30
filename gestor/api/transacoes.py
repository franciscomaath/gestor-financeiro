from flask import Blueprint, jsonify, request
from ..models import Transacao, Categoria
from ..extensions import db

transacoes_bp = Blueprint('transacoes_api', __name__)

# descricao, valor, tipo, categoria_id

@transacoes_bp.route('/transacoes', methods = ['POST'])
def criar_transacao():
    dados = request.get_json()

    if not dados:
        return jsonify({'mensagem': 'A requisição não pode estar vazia.'}), 400

    if 'valor' not in dados:
        return jsonify({'mensagem': 'O campo Valor não pode ficar vazio.'}), 400
    
    if 'tipo' not in dados:
        return jsonify({'mensagem': 'O campo Tipo não pode ficar vazio.'}), 400
    
    if 'categoria_id' not in dados:
        return jsonify({'mensagem': 'O campo Categoria não pode ficar vazio.'}), 400

    categoria_id = dados['categoria_id']
    categoria = Categoria.query.get(categoria_id)

    if not categoria:
        return jsonify({'mensagem': 'Categoria não encontrada.'}), 404

    nova_transacao = Transacao(descricao = dados.get('descricao'), valor = dados['valor'], tipo = dados['tipo'], categoria_id = categoria_id)

    db.session.add(nova_transacao)
    db.session.commit()

    return jsonify(nova_transacao.to_dict()), 201

@transacoes_bp.route('/transacoes', methods = ['GET'])
def listar_transacoes():
    transacoes = Transacao.query.all()

    resultado = []
    for t in transacoes:
        resultado.append(t.to_dict())

    return jsonify(resultado), 200

@transacoes_bp.route('/transacoes/<int:transacao_id>', methods = ['GET'])
def buscar_transacao_id(transacao_id):
    transacao = Transacao.query.get_or_404(transacao_id)
    return jsonify(transacao.to_dict()), 200

# descricao, valor, tipo, categoria_id
@transacoes_bp.route('/transacoes/<int:transacao_id>', methods = ['PUT'])
def atualizar_transacao(transacao_id):
    dados = request.get_json()

    if not dados:
        return jsonify({'mensagem': 'A requisição não pode estar vazia.'}), 400

    transacao = Transacao.query.get_or_404(transacao_id)

    transacao.descricao = dados.get('descricao', transacao.descricao)
    transacao.valor = dados.get('valor', transacao.valor)
    transacao.tipo = dados.get('tipo', transacao.tipo)
    
    if 'categoria_id' in dados:
        nova_categoria_id = dados['categoria_id']
        categoria_existe = Categoria.query.get(nova_categoria_id)
        if not categoria_existe:
            return jsonify({"mensagem": f"A nova categoria de id {nova_categoria_id} não foi encontrada."}, 404)

        transacao.categoria_id = nova_categoria_id

    # if 'tipo' in dados:
    #     transacao.tipo = dados['tipo']
    
    # if 'categoria_id' in dados:
    #     transacao.tipo = dados['categoria_id']

    db.session.commit()

    return jsonify(transacao.to_dict()), 200

@transacoes_bp.route('/transacoes/<int:transacao_id>', methods = ['DELETE'])
def deletar_transacao(transacao_id):
    transacao = Transacao.query.get_or_404(transacao_id)

    db.session.delete(transacao)
    db.session.commit()

    return jsonify({'mensagem': 'Transação deletada com sucesso.'}), 200