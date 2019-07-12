# Tecnologias utilizadas: 
Python 3.5.2 e Django 1.8.3

# Script para a app utilizar o virtualenv

activate_this = '/home/NOMEUSUARIO/.virtualenvs/NOMEVIRTUALENV/bin/activate_this.py'
with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))
