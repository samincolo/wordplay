#!/usr/bin/env python3
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
global webster

@app.route('/lookup')
def lookup():
    word = request.args.get('word')
    if word not in webster: 
        return jsonify("{} not found.".format(word))
    return jsonify(webster[word])

if __name__ == "__main__":
    with open('/webster/webster.json','r') as f:
        global webster
        webster = json.load(f)
    app.run(host='0.0.0.0')

