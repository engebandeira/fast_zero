from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI(title='Minha API')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


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
