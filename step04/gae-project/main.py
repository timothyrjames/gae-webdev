import flask


app = flask.Flask(__name__)

operators = [
    'plus',
    'minus',
    'times',
    'divided by',
    'to the power of',
]

MAIN_CONTENT = '''<html>
    <head>
        <title>Calculator Example</title>
    </head>
    <body>
        <header>
            <h1>Calculator</h1>
        </header>
        <section>
            <form method="get" action="calculate">
                <input type="number" name="operand1">
                %s
                <input type="number" name="operand2">
                <input type="submit" value="equals">
            </form>
        </section>
        <section>
            %s
        </section>
    </body>
</html>
'''


def get_select():
    result = '<select name="operator">'
    for operator in operators:
        result += '<option>%s</option>' % (operator)
    return result


@app.route('/')
def root():
    return MAIN_CONTENT % (get_select(), '')


@app.route('/calculate')
def calculate():
    param1 = flask.request.args['operand1']
    param2 = flask.request.args['operand2']
    operator = flask.request.args['operator']
    c = 0
    text = '' 

    try:
        # note that while our browser will check that our inputs are numbers,
        # this does not guarantee our script will *receive* numbers.
        operand1 = float(param1)
        operand2 = float(param2)
        if operator == 'plus':
            c = operand1 + operand2
            text = '%s %s %s equals %s' % (operand1, operator, operand2, c)
        elif operator == 'minus':
            c = operand1 - operand2
            text = '%s %s %s equals %s' % (operand1, operator, operand2, c)
        elif operator == 'times':
            c = operand1 * operand2
            text = '%s %s %s equals %s' % (operand1, operator, operand2, c)
        elif operator == 'divided by':
            c = operand1 / operand2
            text = '%s %s %s equals %s' % (operand1, operator, operand2, c)
        elif operator == 'to the power of':
            c = operand1 ** operand2
            text = '%s %s %s equals %s' % (operand1, operator, operand2, c)
        else:
            text = 'That operator is not supported.'
    except:
        text = 'An error occurred.'
    return MAIN_CONTENT % (get_select(), text)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
