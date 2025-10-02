from .extensions import db
import enum

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)

    transacoes = db.relationship('Transacao', back_populates = 'categoria')

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome
        }
    
class TipoTransacao(enum.Enum):
    RECEITA = 'receita'
    DESPESA = 'despesa'

class Transacao(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    descricao = db.Column(db.String(250), nullable = True)
    valor = db.Column(db.Float, nullable = False)
    tipo = db.Column(db.Enum(TipoTransacao), nullable = False, default = TipoTransacao.DESPESA)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable = False)

    categoria = db.relationship('Categoria', back_populates = 'transacoes')

    def to_dict(self):
        # categoria = Categoria.query.get(self.categoria_id)

        return {
            'id': self.id,
            'descricao': self.descricao,
            'valor': self.valor,
            'tipo': self.tipo.value,
            'categoria_id': self.categoria.nome
        }