import flask
from google.cloud import datastore


app = flask.Flask(__name__)


def get_client():
    # Note that if we want to specify a project here, we could do it like this:
    # return datastore.Client('your-project-id')
    # Calling Client() with no argument will access the environment variables
    # for your project - which will be fine for your deployed application.
    return datastore.Client()


def create_thing():
    client = get_client()
    # Calling key without an ID will generate (an int) one for you.
    key = client.key('an_entity_type_name')
    return datastore.Entity(key)


def retrieve_thing(id):
    client = get_client()
    # Make sure this is an int; string will yield a different result.
    # It's OK to use strings instead, but make sure you're consistent.
    key = client.key('an_entity_type_name', int(id))
    return client.get(key)


def update_thing(thing):
    client = get_client()
    client.put(thing)


def delete_thing(id):
    client = get_client()
    key = client.key('an_entity_type_name', int(id))
    client.delete(key)


def get_things():
    result = []
    client = get_client()
    query = client.query(kind='an_entity_type_name')
    for entity in query.fetch():
        result.append(entity)
    return result


def show_things():
    things_list = get_things()
    return flask.render_template('index.html', things=things_list)


@app.route('/')
def handle_request_root():
    return show_things()


@app.route('/edit-thing', methods=['POST', 'GET'])
def handle_request_edit_thing():
    id = flask.request.values['id']
    ds_thing = retrieve_thing(id)
    return flask.render_template('edit-thing.html', thing=ds_thing)


@app.route('/delete-thing', methods=['POST', 'GET'])
def handle_request_delete_thing():
    id = flask.request.values['id']
    delete_thing(id)
    return show_things()


@app.route('/create-thing', methods=['POST', 'GET'])
def handle_request_create_thing():
    text = flask.request.values['text']
    thing = create_thing()
    thing['text'] = text
    update_thing(thing)
    return show_things()


@app.route('/update-thing', methods=['POST', 'GET'])
def handle_request_update_thing():
    text = flask.request.values['text']
    id = flask.request.values['id']
    thing = retrieve_thing(id)
    thing['text'] = text
    update_thing(thing)
    return show_things()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

