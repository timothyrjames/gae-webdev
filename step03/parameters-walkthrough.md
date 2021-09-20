# Handling Parameters

## Creating a Form

We'll start from a plain ```index.html``` file. This file can contain a form so
that we can submit parameters easily to our server. Our form HTML will look
something like this:

```html
<section>
    <header>
        <h2>Send a GET Request</h2>
    </header>
    <form method="get" action="/sendget">
        <div>
            Enter something here: <input type="text" name="inputfield">
        </div>
        <div>
            Enter a number here: <input type="number" name="numberfield">
        <div>
            <input type="submit" value="Send a GET!">
        </div>
    </form>
</section>
```

You can see in this section that we are creating a ```form``` element, we are
setting the ```method``` attribute to GET, and we are sending the form data
(using the ```action``` attribute) to /sendget.

If you run the example, you will see that if you enter "something" in the first
field and "19" in the second field, you'll be sent to a url that ends like
this:

```/sendget?inputfield=something&numberfield=19```

Because this is a GET method, the parameters will be included on the URL.

## Processing GET Parameters

In our Python code, we can handle these parameters a few ways; using 
flask.request.args or flask.request.values. See the code below:

```python
@app.route('/sendget')
def send_get():
    param1 = flask.request.args['inputfield']
    param2 = flask.request.args['numberfield']

    page_msg = 'You entered: "%s" and the number "%s"' % (param1, param2)
    return flask.Response(MAIN_CONTENT % (page_msg), mimetype='text/html')
```

This code will retrieve both parameters and create a message for the user. Note
that you could change the URL directly and see results reflected in this page.

## Processing POST Requests

A form for POST requests differs only in the form ```method```:

```html
<form method="post" action="/sendpost">
    <div>
        Enter something here:
    </div>
    <div>
        <textarea name="inputfield"></textarea>
    <div>
        <input type="submit" value="Send a POST!">
    </div>
</form>
```

You'll see that we can set specific methods in our app.route annotation.

```python
@app.route('/sendpost', methods=["POST"])
def send_post():
    param1 = flask.request.form['inputfield']

    page_msg = 'A post parameter was received: %s' % (param1)
    return flask.Response(MAIN_CONTENT % (page_msg), mimetype='text/html')
```

This will prevent the Flask server from responding to GET (or other) request
methods.

## URL Path Parameters

We can also work with parameters from the URL path. Flask's route annotations
have a mechanism for this.

```python
@app.route('/pathpage/<p1>')
def path_page(p1):
    page_content = '<div>The extra part of the path is "%s"</div>' % (p1)

    p = MAIN_CONTENT % (page_content)
    return flask.Response(MAIN_CONTENT % (p), mimetype='text/html')
```

As seen above, we can provide parameters as part of the URL path. Anything that
follows ```/pathpage/``` in our URL (as long as it's a legal path) will be
populated as ```p1```.

## Longer URL Path Parameters

We are not limited to a single path value in this manner; we can use multiple
path values.

```python
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
    return flask.Response(MAIN_CONTENT % (p), mimetype='text/html')
```

Note that all path components must be included in order for this to work.