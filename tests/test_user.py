import random
import string

import pytest

BASE_URL = 'https://api-sandbox-jobs.sandbox.packetfabric.net/'
CUSTOMER = 'customer'
USER = 'users'
USER_FULL = '%s%s' % (BASE_URL, USER)


@pytest.fixture(scope="class")
def seed_users(session):
    users = {}

    params = {
        'user_first_name': 'John',
        'user_last_name': 'Doe',
        'user_email': 'john.doe@gmail.com',
        'user_login': (_randomstring(20)),
        'user_password': 'doe',
        'group_name': 'regular',
        'user_phone': '+1 123456789',
        'user_timezone': 'America/Los_Angeles',
        'user_searchable': True,
    }
    r = session.post(USER_FULL, params)
    id_ = r.json()['user_id']
    users[id_] = r.json()
    yield users

    for user in users.keys():
        r = session.delete(USER_FULL + '/' + str(user))
        assert r.json()['message'], 'User Deleted'


def test_get_all_users(session, seed_users):
    r = session.get(USER_FULL)
    r_dict = {x['user_id']: x for x in r.json()}
    for user_id in seed_users.keys():
        _are_equal(seed_users[user_id], r_dict[user_id])


def _randomstring(n=10):
    """Generate a random string of fixed length """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))


def _are_equal(user1, user2):
    assert user1['user_first_name'] == user2['user_first_name']
    assert user1['user_last_name'] == user2['user_last_name']
    assert user1['user_email'] == user2['user_email']
    assert user1['user_login'] == user2['user_login']
    assert user1['user_phone'] == user2['user_phone']
    assert user1['user_timezone'] == user2['user_timezone']
    assert user1['user_searchable'] == user2['user_searchable']
