import flask
import json
import logging
import slapp


app = flask.Flask(__name__)


@app.route('/get-data')
def get_data():
    response_json = json.dumps({
        'Text': 'This content was loaded from the server.',
    })
    # we use the Response object here so that we can easily set the mimetype
    # without mimetype, some browsers may not handle the response properly.
    return flask.Response(response_json, mimetype='application/json')


@app.route('/')
def shopping_list():
    return flask.redirect("/s/index.html", code=302)


@app.route('/load-sl-items')
def load_sli_items():
    # first we load the list items
    logging.info('loading list items.')
    sl_list = slapp.get_list_items()

    # next we convert them to dictionaries and then json
    dictionaries = convert_to_dicts(sl_list)
    response_json = json.dumps(dictionaries)
    return flask.Response(response_json, mimetype='application/json')


@app.route('/save-item', methods=['POST'])
def save_item():
    # retrieve the parameters from the request
    q = flask.request.form['quantity']
    title = flask.request.form['title']
    item_id = None
    if 'id' in flask.request.form:
        item_id = flask.request.form['id']

    json_result = {}
    try:
        if item_id:
            logging.info('saving existing list item')
            slapp.save_list_item(item_id, title, q)
        else:
            logging.info('creating new list item')
            slapp.create_list_item(title, q)
        json_result['ok'] = True
    except Exception as exc:
        logging.info(str(exc))
        json_result['error'] = 'The item was not saved.'

    return flask.Response(json.dumps(json_result), mimetype='application/json')


@app.route('/delete-item', methods=['POST'])
def delete_item():
    # retrieve the parameters from the request
    sli_id = flask.request.form['id']
    json_result = {}
    try:
        logging.info('deleting item for ID: %s' % (sli_id))
        slapp.delete_list_item(sli_id)
        json_result['ok'] = True
    except Exception as exc:
        loggging.info(str(exc))
        json_result['error'] = 'The item was not removed.'

    return flask.Response(json.dumps(json_result), mimetype='application/json')


# here we use a Flask shortcut to pull the itemid from the URL.
@app.route('/get-item/<itemid>')
def get_item(itemid):
    logging.info('retrieving item for ID: %s' % (itemid))
    item = slapp.get_list_item(itemid)
    d = item.to_dict()
    json_response = json.dumps(d)
    return flask.Response(json_response, mimetype='application/json')


def convert_to_dicts(obj_list):
    result = []
    for obj in obj_list:
        result.append(obj.to_dict())
    return result


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
