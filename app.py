from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    length = request.args.get('length')
    if length == None:
        password = 'Generar clave'

    else:
        chart = list('0123456789')
        if request.args.get('uppercase'):
            chart.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
        if request.args.get('lowercase'):
            chart.extend(list('abcdefghijklmnñopqrstuvwxyz'))
        if request.args.get('simbol'):
            chart.extend(list('#$%/&!?'))

        password = ''
        for x in range(int(length)):
            password += random.choice(chart)

    return render_template('index.html', password = password)


if __name__ == '__main__':
    app.run(debug=True)
