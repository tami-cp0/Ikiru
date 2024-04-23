#!/usr/bin/python3
""" Flask Application """
from models import storage
from api.v1.views import apis
from flask import Flask, make_response, jsonify
from flasgger import Swagger
# from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['DEBUG'] = True
app.register_blueprint(apis)
SWAGGER_URL = '/api/docs'
swagger = Swagger(app)


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port='5000', threaded=True)
