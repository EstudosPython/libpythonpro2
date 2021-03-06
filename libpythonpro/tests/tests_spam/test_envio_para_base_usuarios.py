from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='gustavo', email='gustavoguesser@gmail.com'),
            Usuario(nome='joao', email='gustavoguesser@gmail.com')
        ],
        [
            Usuario(nome='gustavo', email='gustavoguesser@gmail.com'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gustavoguesser@gmail.com',
        'Curso PythonPro',
        'Confira os modulos fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='gustavo', email='gustavoguesser@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@gmail.com',
        'Curso PythonPro',
        'Confira os modulos fantasticos'
    )
    enviador.enviar.assert_called_once_with(
        'luciano@gmail.com',
        'gustavoguesser@gmail.com',
        'Curso PythonPro',
        'Confira os modulos fantasticos'
    )
