from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import yaml
import json
import requests

app = Flask(__name__)
CORS(app)
api = Api(app)

config = yaml.safe_load(open('config.yml'))
username = config['username']
last_fm_api_key = config['last_fm_api_key']
youtube_api_key = config['youtube_api_key']

@app.route('/artists')
def artists():
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={username}&api_key={last_fm_api_key}&format=json"
    response = requests.get(url)
    data = json.loads(response.text)

    res = []
    for a in data["topartists"]["artist"]:
        artist = {}
        artist["name"] = a["name"]
        artist["playcount"] = a["playcount"]
        res.append(artist)
    
    return res

@app.route('/tracks')
def tracks():
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={username}&api_key={last_fm_api_key}&format=json"
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

@app.route('/search_video')
def search_video():
    query = request.args.get('query')
    url = f"https://www.googleapis.com/youtube/v3/search?key={youtube_api_key}&type=video&part=snippet&q={query}"
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)

    id = data["items"][0]["id"]["videoId"]
    print(id)
    return id


if __name__ == '__main__':
    app.run(debug=True)
