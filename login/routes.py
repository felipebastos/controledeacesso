from flask import Blueprint, render_template, request
from login import db, loginmanager
from login.entities import Usuario

from flask_login import login_user, logout_user, login_required

bp = Blueprint('rotas', __name__, url_prefix='/')

loginmanager.login_view = '/'

@bp.route('/')
def raiz():
    return render_template('index.html')

@bp.route('/login', methods=['POST'])
def login():
    nome = request.form['nome']
    senha = request.form['senha']

    quem = Usuario.query.filter_by(nome=nome).first()

    if quem is None:
        return 'Não tem esse usuário'
    else:
        if quem.senha == senha:
            login_user(quem)
            return 'fez login'
        else:
            return 'não fez login'

@bp.route('/logout')
@login_required
def sair():
    logout_user()
    return 'saiu com sucesso!'

@loginmanager.user_loader
def user_loader(id):
    return Usuario.query.get(id)