from flask import Blueprint
from flask_login import login_required

bp = Blueprint('restrito', __name__, url_prefix='/restrito')

@bp.route('/segredo')
@login_required
def segredo():
    return 'xiu!'