import flask
import google.cloud.logging
import logging

app = flask.Flask(__name__)


@app.route('/')
@app.route('/index.html')
def root():
    logging.info('Someone opened the main page.')
    return '<html><body>This page logs an info message.</body></html>'


@app.route('/warn')
def warning():
    logging.warning('Someone opened the warning page.')
    return '<html><body>This page logs a warning message.</body></html>'


@app.route('/error')
def error():
    logging.error('Someone opened the error page.')
    return '<html><body>This page logs an error message.</body></html>'


@app.route('/gcl')
def setup_cloud_logging():
    # This will enable cloud logging; instead of selecting 'stderr' you will
    # need to select 'app' and expand the jsonPayload to see messages after
    # running this code.

    # Also note that requirements.txt will need to reference the Google Cloud
    # Logging library.
    client = google.cloud.logging.Client()
    client.get_default_handler()
    client.setup_logging()
    return '<html><body>cloud logging set up.</body></html>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)