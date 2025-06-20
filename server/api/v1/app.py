"""
REST API Flask app
"""
from flask import Flask, jsonify
from flask_cors import CORS
from server.api.v1.views import app_views


def create_app():
    """ Create a Flask app
    """
    app = Flask(__name__)
    app.register_blueprint(app_views, url_prefix='/api/v1')
    return app


app = create_app()
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    """ Handle 404 errors
    """
    err_message = error.description if hasattr(error, 'description') else 'Not Found'
    return jsonify({'error': err_message}), 404

@app.errorhandler(400)
def bad_request(error):
    """ Handle 400 errors
    """
    err_message = error.description if hasattr(error, 'description') else 'Bad Request'
    return jsonify({'error': err_message}), 400


@app.errorhandler(500)
def internal_server_error(error):
    """ Handle 500 errors
    """
    if hasattr(error, 'description'):
        err_message = error.description 
    else:
        err_message = 'Internal Server Error. Please try again later.'

    return jsonify({'error': err_message}), 500

if __name__ == '__main__':
    app.run(port='5001', host='0.0.0.0', debug=True)
