#!/usr/bin/env python
from flask import Flask, send_from_directory
import os.path

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<string:path>', methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    if os.path.isfile('dist/' + path):
        return send_from_directory('dist', path)
    else:
        return send_from_directory('dist', 'index.html')


if __name__ == '__main__':
    app.run()
