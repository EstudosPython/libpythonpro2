import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_ciar_enviador_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['gustavoguesser@gmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'gustavo_guesser@estudante.sc.senai.br',
        'Cursos PythonPro',
        'Primeira turma enviada'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'food']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'gustavo_guesser@estudante.sc.senai.br',
            'Cursos PythonPro',
            'Primeira turma enviada'
        )
