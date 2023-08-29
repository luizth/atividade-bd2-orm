# Atividade BD2 - ORM

Aplicação desenvolvida na disciplina de BD2 para aplicar o uso de bibliotecas de ORM.

#### Modelagem

```
Cliente 1 - N Pedidos
Pedido 1 - N ItensPedido
```

#### Módulos

```
- app: contém o app Flask e a definição das rotas

- config: contém configurações do app (banco de dados, url da api)

- conftest: contém configurações do pytest

- model: contém o modelo e as classes do app

- orm: contém a configuração do ORM, a definição das tabelas e o mapeamento do modelo com o ORM.
```
Foi utilizado o Mapeamento Clássico do SQLAlchemy pois ele permite que façamos uma inversão de dependências. O nosso modelo está separado e não depende do ORM, e sim ao contrário (ORM depende do modelo). Dessa forma, se precisarmos trocar o software de ORM, nosso modelo fica intacto.


---
### Instalando as dependências

```bash
$ python -m venv venv
$ ./venv/Scripts/activate
$ pip install -r requirements.txt
```

---
### Executando a aplicação

```bash
$ python app.py
```

---
### Rotas

```
GET /

GET /clientes

POST /cliente
{
    "nome": str,
    "idade": int,
    "sexo": Sexo[M, F]
}

GET /cliente/<int:cliente_id>

POST /cliente/<int:cliente_id>/pedido

GET /pedido/<int:pedido_id>

POST /pedido/<int:pedido_id>/itens
{
    "quantidade": int,
    "pedido_id": str  # ID do produto é externo
}
```
