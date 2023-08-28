import model


def test_database_exists(session):
    assert session is not None


def test_cliente_table_exists(session):
    assert len(session.query(model.Cliente).all()) == 0


def test_pedido_table_exists(session):
    assert len(session.query(model.Pedido).all()) == 0


def test_itempedido_table_exists(session):
    assert len(session.query(model.ItemPedido).all()) == 0
