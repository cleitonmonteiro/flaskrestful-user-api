# TIPSTA - This Is a Project of Submissão de Trabalhos Acadêmicos

## Pré-requisitos
* [Python3](https://www.python.org/download/releases/3.0/)

## Instalação e Configuração

Clone o repositório:
```
$ git clone https://github.com/cleitonmonteiro/tipsta.git
```

Crie o ambiente virtual: do :
```
$ python -m venv env
$ source env/bin/activate
```

Intalação dos pacotes:
```
(env)$ pip install -r requirements.txt
```

## Iniciando app [Flask](http://flask.pocoo.org/)
Adicionando as variaveis do sistema:
```
$ export FLASK_APP=run.py
$ export FLASK_CONFIG=development
```
Atualizando Banco de dados
```
$ flask db migrate
$ flask db upgrade
```

Agora basta iniar a app:
```
$ flask run
```
