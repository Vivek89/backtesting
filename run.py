from flask import Flask
from flask_restplus import Api
from api.resource_things.view import resource_things
from api.second_thing.view import second_things

app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE')


@app.route('/')
def sample():
    return "Hello World"


def main():
    app.register_blueprint(resource_things, url_prefix='/api')
    app.register_blueprint(second_things, url_prefix='/api')

    Api(app, doc='/docs', version='1.0', title='GAUSS BackTesting API', description='Api for GAUSS Backtesting Application!')

    app.run(host=app.config['FLASK_HOST_NAME'], port=app.config['FLASK_PORT_NO'], debug=True)


if __name__ == '__main__':
    main()