import requests as requests


def bucar_avatar(usuario):
    """
    busca o avatar do nome de usuario
    :param usuario:
    :return:
    """
    url = f"https://api.github.com/users/{usuario}"
    resp = requests.get(url)
    return resp.json()['avatar_url']


