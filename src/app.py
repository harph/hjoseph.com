from flask import Blueprint, Flask
from urls import URL_RULES


class WebApp(object):
    def __init__(self):
        self._app = None
        pass

    def _create_blueprint(self):
        blueprint = Blueprint('hjoseph.com', __name__)
        # Add URL rules
        for rule in URL_RULES:
            blueprint.add_url_rule(**rule)
        return blueprint

    def create_app(self):
        if not self._app:
            app = Flask(__name__)
            app.config.from_object('config')
            blueprint = self._create_blueprint()
            app.register_blueprint(blueprint, url_prefix='')
            self._app = app
        return self._app
