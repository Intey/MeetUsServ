import logging
import dataclasses

# type: ignore
import connexion
# type: ignore
from connexion.resolver import RestyResolver
# type: ignore
from connexion.apps.flask_app import FlaskJSONEncoder
# type: ignore
from flask_cors import CORS


class EnhancedJSONEncoder(FlaskJSONEncoder):
    """
    Json encoder for dataclasses(Python 3.7+)
    """
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
    CORS(app) # for frontend dev
    app.run(port=8000, debug=True)
