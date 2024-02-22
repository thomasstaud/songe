from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import yaml
import json
import requests

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

config = yaml.safe_load(open('config.yml'))
username = config['username']
api_key = config['api_key']

@app.route('/artists')
def artists():
    url = f"http://ws.audioscrobbler.com/2.0/?method=library.getartists&api_key={api_key}&user={username}&format=json"
    response = requests.get(url)
    data = json.loads(response.text)

    res = []
    for a in data["artists"]["artist"]:
        artist = {}
        artist["name"] = a["name"]
        artist["playcount"] = a["playcount"]
        res.append(artist)
    
    return res

@app.route('/tracks')
def tracks():
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={username}&api_key={api_key}&format=json"
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)

    res = []
    for t in data["toptracks"]["track"]:
        track = {}
        track["name"] = t["name"]
        track["artist"] = t["artist"]["name"]
        track["playcount"] = t["playcount"]
        res.append(track)
    
    return res

if __name__ == '__main__':
    app.run(debug=True)
