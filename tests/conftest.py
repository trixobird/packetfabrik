import pytest
import requests

BASE_URL = 'https://api-sandbox-jobs.sandbox.packetfabric.net/'
LOGIN = "login"
CUSTOMER = 'customer'


@pytest.fixture(scope="module")
def session():
    session = requests.Session()
    login_url = "%s%s" % (BASE_URL, LOGIN)
    params = {
        'user_login': 'george.trichopoulos@gmail.com',
        'user_password': 'BijiezoA*1'
    }
    session.post(login_url, data=params)
    return session
