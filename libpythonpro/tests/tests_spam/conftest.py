import pytest

from libpythonpro.spam.bd import Conexao


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


@pytest.fixture(scope='session')
def conexao():
    #setup
    conexao_obj = Conexao()
    yield conexao_obj
    #tear Down
    conexao_obj.fechar()