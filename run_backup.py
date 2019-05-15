from flask_failsafe import failsafe
from gevent import monkey
from gevent.pywsgi import WSGIServer
from werkzeug.debug import DebuggedApplication
from werkzeug.serving import run_with_reloader

# @failsafe
# def failsafe_app():
#     from app import create_app
#     return create_app()


# app = failsafe_app()


@run_with_reloader
def run():

    app.debug = app.config['DEBUG']

    print('Starting server at %s listening on port %s %s' %
          (app.config['HOST'], app.config['PORT'], 'in DEBUG mode'
          if app.config['DEBUG'] else ''))

    if app.config['DEBUG']:
        http_server = WSGIServer((app.config['HOST'], app.config['PORT']),
                                 DebuggedApplication(app))
    else:
        if app.config['REQUEST_LOGGING']:
            http_server = WSGIServer((app.config['HOST'], app.config['PORT']),
                                     app)
        else:
            http_server = WSGIServer(
                (app.config['HOST'], app.config['PORT']), app, log=None)

    http_server.serve_forever()