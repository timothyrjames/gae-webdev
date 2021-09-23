import flask


app = flask.Flask(__name__)


MAIN_PAGE = '/s/index.html'

# NOTE the use of absolute paths in MAIN_CONTENT. If we don't use them, then we
# may continue to stack the URL path; our first page will be  /s/index.html -
# without the preceding forward slash, the next link would be 
# /s/pathpage/something, the following would be
# /s/pathpage/something/pathpage/something+else, etc.
MAIN_CONTENT = '''<html>
    <head>
        <title>Server Interaction Examples</title>
    </head>
    <body>
        <header>
            <h1>Server Interaction Examples</h1>
        </header>
        <nav>
            <a href="/">Main Page</a>
            <a href="/pathpage/something">A Page Using a Path</a>
            <a href="/pathpage/something+else">Another Page Using a Path</a>
            <a href="/longpath/path1/path2/path3">A Longer Path Page</a>
        </nav>
        <hr>
        <section>
            %s
        </section>
    </body>
</html>
'''

@app.route('/')
def root():
    return flask.redirect(MAIN_PAGE, code=302)


@app.route('/sendget')
def send_get():
    # We have a few ways to retrieve these parameters.
    # For a GET request, we can use the flask.request.args dictionary.
    param1 = flask.request.args['inputfield']
    param2 = flask.request.args['numberfield']

    # Note that we could also use flask.request.values, which contains both
    # POST and GET parameters.
    # param1 = flask.request.values['inputfield']
    # param2 = flask.request.values['numberfield']

    page_msg = 'You entered: "%s" and the number "%s"' % (param1, param2)

    # A Response object allows us more control than simply returning a string.
    return flask.Response(MAIN_CONTENT % (page_msg), mimetype='text/html')


# By using methods=["POST"] this page can't be directly requested.
@app.route('/sendpost', methods=["POST"])
def send_post():
    # As above, we can use a few mechanisms to retrieve parameters.
    param1 = flask.request.form['inputfield']

    page_msg = 'A post parameter was received: %s' % (param1)
    return flask.Response(MAIN_CONTENT % (page_msg), mimetype='text/html')


@app.route('/pathpage/<p1>')
def path_page(p1):
    page_content = '<div>The extra part of the path is "%s"</div>' % (p1)

    p = MAIN_CONTENT % (page_content)
    return flask.Response(p, mimetype='text/html')


@app.route('/longpath/<p1>/<p2>/<p3>')
def long_path_page(p1, p2, p3):
    page_content = ''
    if p1:
        page_content += '<div>Part 1 of the path is "%s"</div>' % (p1)
    if p2:
        page_content += '<div>Part 2 of the path is "%s"</div>' % (p2)
    if p3:
        page_content += '<div>Part 3 of the path is "%s"</div>' % (p3)

    p = MAIN_CONTENT % (page_content)
    return flask.Response(p, mimetype='text/html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
