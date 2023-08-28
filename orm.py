from sqlalchemy import MetaData, Table, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import registry, relationship

import model


mapper_registry = registry()
metadata = MetaData()

clientes = Table(
    'clientes',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nome', String(255)),
    Column('idade', Integer),
    Column('sexo', Enum(model.Sexo))
)

pedidos = Table(
    'pedidos',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('status', Enum(model.StatusPedido)),
    Column('cliente_id', ForeignKey('clientes.id'))
)

itens_pedido = Table(
    'itens_pedido',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('quantidade', Integer),
    Column('produto_id', String(255), nullable=False),  # ID do produto externo
    Column('pedido_id', ForeignKey('pedidos.id'))
)


def start_mappers():
    mapper_registry.map_imperatively(
        model.Cliente,
        clientes,
        properties={
            '_pedidos': relationship(model.Pedido, backref='pedidos', order_by=pedidos.c.id)
        }
    )
    mapper_registry.map_imperatively(
        model.Pedido,
        pedidos,
        properties={
            'cliente': relationship(model.Cliente, backref='clientes'),
            '_itens': relationship(model.ItemPedido, backref='itens_pedidos', order_by=itens_pedido.c.id)
        }
    )
    mapper_registry.map_imperatively(model.ItemPedido, itens_pedido,)
