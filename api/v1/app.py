#!/usr/bin/python3
""" Flask Application """
from models import storage
from api.v1.views import apis
from flask import Flask, make_response, jsonify
from flasgger import Swagger
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(apis)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "http://100.26.157.241"}})


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@app.errorhandler(429)
def handle_rate_limit_exceeded(e):
    return make_response(jsonify({
        "error": "Rate limit exceeded. Please try again later."
    }), 429)


app.config['SWAGGER'] = {
    'title': 'Ikiru RESTful API',
    'uiversion': 3,
    'openapi': '3.0.3',
    'version': '1.0',
    'description': 'API documentation for the Ikiru Restful API',
    'contact': [
        {
            'name': 'Oluwatamilore Olugbesan',
            'email': 'findtamilore@gmail.com'
        },
        {
            'name': 'Solomon Ayofemi',
            'email': 'solomonayofemi@gmail.com'
        },
        {
            'name': 'Huclark Vanderpuye',
            'email': 'vhuclark@gmail.com'
        }
    ],
    'license': {
        'name': 'MIT License',
        'url': 'https://opensource.org/licenses/MIT'
    },
    'url_prefix': '/api/v1',
    "specs_route": "/docs"
}
Swagger(app)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port='5000', threaded=True)
