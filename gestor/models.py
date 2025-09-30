from .extensions import db
import enum

class Categoria:
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)

    transacoes = db.relationship('Transacao', back_populates = 'transacao')

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome
        }
    
class TipoTransacao(enum.Enum):
    RECEITA = 'receita'
    DESPESA = 'despesa'

class Transacao:
    id = db.Column(db.Integer, primary_key = True)
    descricao = db.Column(db.String(250), nullable = True)
    valor = db.Column(db.Float, nullable = False)
    tipo = db.Column(db.SQLEnum(TipoTransacao), nullable = False, default = TipoTransacao.DESPESA)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable = False)

    categoria = db.relationship('Categoria', back_populates = 'transacoes')