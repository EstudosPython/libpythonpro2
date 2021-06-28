from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='gustavo', email='gustavoguesser@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id,int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='gustavo', email='gustavoguesser@gmail.com'),
                Usuario(nome='joao', email='gustavoguesser@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()





