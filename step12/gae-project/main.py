import flask


app = flask.Flask(__name__)


@app.route('/')
def root():
    return flask.render_template('index.html')


@app.route('/<page>')
def handle_page(page):
    if page.endswith('.html'):
        return flask.render_template(page)
    else:
        return flask.abort(404)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
