import flask
import json
import logging
import myapp


app = flask.Flask(__name__)


@app.route('/')
def request_root():
    logging.info('Request for root page.')
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
