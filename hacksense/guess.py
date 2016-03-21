import requests

MESSAGE = 'You Rock!'
URL = 'http://192.168.1.110:8080'


def guess(number, message=None):
    m = MESSAGE if message is None else message
    try:
        response = requests.get('%s/guess/%d/%s' % (URL, number, m)).json()
        return response['result']
    except:
        return 'bad guess'
