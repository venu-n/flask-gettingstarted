from flask import Blueprint

bp = Blueprint('module1', __name__, url_prefix='/module1', template_folder="templates")

from app.module1 import routes

