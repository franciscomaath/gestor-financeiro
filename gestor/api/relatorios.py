from flask import Blueprint, jsonify, request
from sqlalchemy import func
from ..models import Transacao, Categoria, TipoTransacao
from ..extensions import db


relatorios_bp = Blueprint('relatorios_api', __name__)

@relatorios_bp.route('/sumario', methods = ['GET'])
def obter_sumario():
    transacoes_receita = db.session.query(func.sum(Transacao.valor)).filter(Transacao.tipo == TipoTransacao.RECEITA).scalar()

    transacoes_despesa = db.session.query(func.sum(Transacao.valor)).filter(Transacao.tipo == TipoTransacao.DESPESA).scalar

    resposta = {
        'total_receita' : transacoes_receita or 0,
        'total_despesa' : transacoes_despesa or 0,
        'saldo' : (transacoes_receita or 0) - (transacoes_despesa or 0)
    }

    return jsonify(resposta)