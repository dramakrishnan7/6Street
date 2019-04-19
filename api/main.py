from flask import Flask, request, jsonify, send_from_directory, render_template
import logging
import os

app = Flask(__name__)


@app.route('/api/check', methods=['GET', 'POST'])
def api_check():
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

@app.route('/api/search/', methods=['GET', 'POST'])
def search():
    # here we want to get the title of song (i.e. ?song=Thriller)
    song = request.args.get('song')
    resp = jsonify(success=True, song=song)
    resp.status_code = 200
    return resp

if __name__=="__main__":
    app.run()