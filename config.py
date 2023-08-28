
def get_db_uri() -> str:
    return 'sqlite:///clientes.db'


def get_host() -> str:
    return '127.0.0.1'


def get_port() -> str:
    return '5000'


def get_api_url() -> str:
    return f'http://{get_host()}:{get_port()}'
