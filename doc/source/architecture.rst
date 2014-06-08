Arquitetura
==============

A Globo Photo tem sua arquitetura pensada para receber novas features
como também na facilidade de melhorar funcionalidades existentes.

Ela foi desenvolvida usando as seguintes tecnologias:

- `Python 2.7`_
- `MySQL 5.6`_
- `Django 1.6`_
- `South 0.8.4`_
- `Pillow 2.4.0`_
- `dj-database-url 0.3.0`_
- `MySQL-python 1.2.5`_

A estrutura do projeto está organizado da seguinte forma::

    ├── bootstrap
    ├── doc
    ├── globophoto
    │   ├── settings.py
    │   ├── templates
    │   │   ├── 404.html
    │   │   ├── 500.html
    │   │   └── base.html
    │   ├── urls.py
    │   ├── wsgi.py
    ├── media
    ├── static
    ├── requirements.txt
    ├── Makefile
    ├── manage.py


- **bootstrap**: Pasta que contêm a função de criar um ambiente virtual e instalar as dependências que estão no `requirements.txt`.
- **doc**: Aonde contêm a documentação do projeto. Lá existem mais detalhes referentes ao mesmo.
- **globophoto**: Pasta do projeto
- **media**: Pasta que será criada quando for inserida fotos no sistema.
- **static**: Contêm os assets do projeto.
- **requirements.txt**: Armazena as dependências do projeto.
- **Makefile**: Arquivo com os comandos mais usados no projeto.
- **manage.py**: Arquivo que acessa os comandos django do projeto.

Como foi visto acima, dentro da pasta `globophoto` existem outros arquivos, que são provenientes a um projeto Django, além do `manage.py`, que são:

- **settings.py**: Arquivo que armazena as configurações gerais do projeto, como conexão com o banco de dados, módulos do sistema, etc.
- **templates**: Contêm os templates usado pelo todo o projeto. Como mostrado existe o `base.html` que possui o layout geral do sistema, o `404.html` que é exigido quando uma página não é encontrada e o `500.html` quando ocorre um erro interno.
- **urls.py**: Todas as rotas usados no sitema estão nesse arquivo.
- **wsgi.py**: Módulo responsável de preparar o projeto para ser iniciado, usando WSGI.

.. _Python 2.7: https://www.python.org/
.. _MySQL 5.6: http://www.mysql.com/
.. _Django 1.6: http://djangoproject.com/
.. _South 0.8.4: http://south.aeracode.org/
.. _Pillow 2.4.0: https://pypi.python.org/pypi/Pillow/
.. _dj-database-url 0.3.0: https://pypi.python.org/pypi/dj-database-url/0.3.0/
.. _MySQL-python 1.2.5: https://pypi.python.org/pypi/MySQL-python/1.2.5/
