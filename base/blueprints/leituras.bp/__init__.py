from flask import Blueprint

leituras_bp = Blueprint('leituras', __name__, template_folder='templates')

from leituras import routes