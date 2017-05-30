from flask import Flask, render_template, jsonify, url_for, request
import webbrowser


app = Flask(__name__, static_path='')

import os
import sys
import json
import time

@app.route('/')
def index():
    return 'Welcome to the STRIPS fiesta!'


@app.route('/alert', methods=['GET'])
def alert():
    pass
    return ''


@app.route("/data")
def data():
    text = open('/Users/max/PycharmProjects/strips_flask/src/static/dota.json', 'r').read()
    return text


@app.route('/index')
def test():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return render_template('hello.html', name='Max')


@app.route('/<task>/<domain>/<problem>') # Декоратор
def solve(task, domain, problem):
    os.system('python ../src/pyperplan.py ../benchmarks/{}/{}.pddl ../benchmarks/{}/{}.pddl &'.format(task, domain, task, problem))
    time.sleep(5)
    return render_template('index.html')


@app.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Error')
    func()
    return 'Server shutting down...'


def work():
    app.debug = True
    app.run()


if __name__ == '__main__':
    app.debug = True
    app.run()
