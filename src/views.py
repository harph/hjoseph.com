from flask import render_template
from flask.views import MethodView
from jinja2 import Environment, FileSystemLoader


class IndexView(MethodView):
    def get(self):
        return render_template('index.html')
