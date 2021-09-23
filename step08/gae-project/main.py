import flask


app = flask.Flask(__name__)


# note that we can include several routes for the same function.
@app.route('/')
@app.route('/index.html')
@app.route('/index')
def root():
    # use render_template to convert the template code to HTML.
    # this function will look in the templates/ folder for your file.
    return flask.render_template('index.html', page_title='Main Page')


# note in our previous example we used separate functions for each template.
# we can use our parameterization here to apply templates for many requests.
@app.route('/p/<requested_page>')
def templater(requested_page):
    return flask.render_template(requested_page)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
