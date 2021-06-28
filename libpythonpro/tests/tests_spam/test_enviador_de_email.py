import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_ciar_enviador_email():
    enviador= Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['gustavoguesser@gmail.com', 'foo@bar.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    destinatarios = ['gustavoguesser@gmail.com', 'foo@bar.com.br']

    resultado=enviador.enviar(
        destinatario,
        'gustavo_guesser@estudante.sc.senai.br',
        'Cursos PythonPro',
        'Primeira turma enviada'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'food']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'gustavo_guesser@estudante.sc.senai.br',
            'Cursos PythonPro',
            'Primeira turma enviada'
        )
    