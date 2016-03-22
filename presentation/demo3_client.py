import requests

host = 'http://0.0.0.0:8080'


def g(action, *args):
    url = host+'/'+action
    for arg in args:
        url += '/'+str(arg)
    r = requests.get(url)
    return r.json()


def hi(name):
    return g('hi', name)['return_value']


def bye(name):
    return g('bye', name)['return_value']


if __name__ == '__main__':
    pass
