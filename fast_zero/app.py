from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI(title='Minha API')
database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    # user_with_id = UserDB(
    #     username=user.username,
    #     email=user.email,
    #     password=user.password,
    #     id=len(database) + 1)

    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


@app.get(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def read_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Deu ruim! Não Achei...'
        )
    return database[user_id - 1]


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=user_id)

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Deu ruim! Não Achei...'
        )

    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Deu ruim! Não Achei...'
        )

    return database.pop(user_id - 1)


# Exercícios
@app.get(
    '/exercicio-02', status_code=HTTPStatus.OK, response_class=HTMLResponse
)
def exercicio_aula_02():
    return """
           <html>
               <head>
                   <title>Nosso Olá mundo</title>
               </head>
               <body>
                   <h1> Olá Mundo! </h1>
               </body>
           </html>
           """
