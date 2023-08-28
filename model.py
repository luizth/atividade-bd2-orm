from typing import List
from enum import Enum, auto
from dataclasses import dataclass


class Sexo(Enum):
    M = auto()
    F = auto()


class Cliente:
    def __init__(self, nome: str, idade: int, sexo: str):
        self.nome: str = nome
        self.idade: int = idade
        self.sexo: Sexo = sexo
        self._pedidos: List[Pedido] = []

    def registrar(self, pedido):  # Pedido):
        self._pedidos.append(pedido)

    def ver_pedidos(self) -> list:  # List[Pedido]:
        return [pedido.to_json() for pedido in self._pedidos]

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "sexo": self.sexo.name,
            "pedidos": self.ver_pedidos()
        }


class StatusPedido(Enum):
    PENDENTE = auto()
    CANCELADO = auto()
    ENVIADO = auto()
    ENTREGUE = auto()


class Pedido:
    def __init__(self, cliente: Cliente):
        self.cliente: Cliente = cliente
        self.status: StatusPedido = StatusPedido.PENDENTE
        self._itens: List[ItemPedido] = list()

    @property
    def editavel(self) -> bool:
        return self.status == StatusPedido.PENDENTE

    def adicionar(self, item):  # item: ItemPedido
        if self.editavel:
            self._itens.add(item)

    def cancelar(self):
        if self.editavel:
            self.status = StatusPedido.CANCELADO

    def ver_itens(self) -> List[dict]:
        return [item.to_json() for item in self._itens]

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "status": self.status.name,
            "itens": self.ver_itens()
        }


@dataclass
class ItemPedido:
    quantidade: int
    produto_id: int  # ID do produto externo

    def to_json(self):
        return {
            "id": self.id,
            "quantidade": self.quantidade,
            "produto_id": self.produto_id
        }
