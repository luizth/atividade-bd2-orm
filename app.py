from typing import List
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
import model  # importe módulo model
import orm


orm.start_mappers()
engine = create_engine(config.get_db_uri())  # configuração da conexão com o banco de dados (SQLite no exemplo)
orm.metadata.create_all(engine)
get_session = sessionmaker(bind=engine)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    session = get_session()
    print(session.query(model.ItemPedido)._raw_columns)
    return jsonify({'hello': 'world'})


@app.route('/clientes', methods=['GET'])
def get_clientes():
    session = get_session()
    clientes: List[model.Cliente] = session.query(model.Cliente).order_by('id').all()
    return jsonify([cliente.to_json() for cliente in clientes])


@app.route('/cliente', methods=['POST'])
def create_cliente():
    session = get_session()
    data = request.get_json()
    novo_cliente = model.Cliente(nome=data['nome'], idade=data['idade'], sexo=data['sexo'])
    session.add(novo_cliente)
    session.commit()
    return jsonify({'id': novo_cliente.id})


@app.route('/cliente/<int:cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    session = get_session()
    cliente = session.query(model.Cliente).filter_by(id=cliente_id).first()
    if cliente:
        return jsonify(cliente.to_json())
    else:
        return jsonify({'message': 'Cliente não encontrado'}), 404


@app.route('/cliente/<int:cliente_id>/pedido', methods=['POST'])
def create_pedido(cliente_id):
    session = get_session()
    cliente = session.query(model.Cliente).filter_by(id=cliente_id).first()
    if cliente:
        novo_pedido = model.Pedido(cliente=cliente)
        session.add(novo_pedido)
        session.commit()
        return jsonify({'id': novo_pedido.id})
    else:
        return jsonify({'message': 'Cliente não encontrado'}), 404


@app.route('/pedido/<int:pedido_id>', methods=['GET'])
def get_pedido(pedido_id):
    session = get_session()
    pedido = session.query(model.Pedido).filter_by(id=pedido_id).first()
    if pedido:
        return jsonify(pedido.to_json())
    else:
        return jsonify({'message': 'Pedido não encontrado'}), 404


@app.route('/pedido/<int:pedido_id>/itens', methods=['POST'])
def add_item(pedido_id):
    session = get_session()
    pedido = session.query(model.Pedido).filter_by(id=pedido_id).first()
    if pedido:
        data = request.get_json()
        novo_item_pedido = model.ItemPedido(quantidade=data['quantidade'], produto_id=data['produto_id'])

        pedido.adicionar(novo_item_pedido)  # regra de negócio: adicionar item ao pedido

        session.add(novo_item_pedido)
        session.commit()
        return jsonify({'id': novo_item_pedido.id})
    else:
        return jsonify({'message': 'Pedido não encontrado'}), 404


if __name__ == '__main__':
    app.run(host=config.get_host(), port=config.get_port(), debug=True)
