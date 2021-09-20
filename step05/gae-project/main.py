import flask


app = flask.Flask(__name__)


# note that we can include several routes for the same function.
@app.route('/')
@app.route('/index.html')
@app.route('/index')
def root():
    return flask.render_template('index.html', page_title='Main Page')


@app.route('/links.html')
def links():
    return flask.render_template('links.html', page_title='Links')


@app.route('/images.html')
def images():
    return flask.render_template('images.html', page_title='Images')


@app.route('/lists.html')
def lists():
    return flask.render_template('lists.html', page_title='Lists')


@app.route('/sections.html')
def sections():
    return flask.render_template('sections.html', page_title='Sections')


@app.route('/tables.html')
def tables():
    return flask.render_template('tables.html', page_title='Tables')


@app.route('/forms.html')
def forms():
    return flask.render_template('forms.html', page_title='Form Elements')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
