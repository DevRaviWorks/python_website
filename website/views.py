from flask import Blueprint

views = Blueprint("views",__name__)

@views.route('/')
def home():
    pass
    return "<h1>test</h1>"
