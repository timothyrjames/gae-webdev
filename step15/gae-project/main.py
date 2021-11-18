import flask
import json
import logging
import myapp


app = flask.Flask(__name__)


@app.route('/')
def request_root():
    logging.info('Request for root page.')
    return "<html><body>This is the main page.</body></html>"


@app.route('/template.html')
def request_template():
    logging.info('Request for template.')
    return flask.render_template('template.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
