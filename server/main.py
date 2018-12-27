import logging
import dataclasses

import connexion
from connexion.resolver import RestyResolver
from connexion.apps.flask_app import FlaskJSONEncoder
from flask_cors import CORS


class EnhancedJSONEncoder(FlaskJSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

def main():
    logging.basicConfig(level=logging.INFO)
    connexion_app = connexion.App(__name__, specification_dir='../')
    app = connexion_app.app
    app.json_encoder = EnhancedJSONEncoder
    app.url_map.strict_slashes = False
    connexion_app.add_api('api.yaml',
                        validate_responses=True,
                        strict_validation=True,
                        resolver=RestyResolver('api'),
                        )
    CORS(app)
    app.run(port=8000, debug=True)
