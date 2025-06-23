from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmar)
    assert response.json() == {'message': 'Hello World'}


def test_exercicio_ola_mundo_em_html(client):
    response = client.get('/exercicio-02')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo! </h1>' in response.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'password': 'secret',
            'username': 'alice',
            'email': 'alice@example.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'alice@example.com',
        'username': 'alice',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'email': 'alice@example.com',
                'username': 'alice',
            }
        ]
    }


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'email': 'alice@example.com',
        'username': 'alice',
    }


def test_read_user_not_found(client):
    response = client.get('/users/3')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'email': 'bob@example.com',
            'username': 'bob',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'email': 'bob@example.com',
        'username': 'bob',
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'email': 'bob@example.com',
            'username': 'bob',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user_not_found(client):
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'email': 'bob@example.com',
        'username': 'bob',
    }
