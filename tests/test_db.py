from fast_zero.models import User


def test_create_user(session):
    user = User(username='test', email='test@test.com', password='secret')
    session.add(user)

    assert user.username == 'test'
    assert user.password == 'secret'
