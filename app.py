from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['map_data']
collection = db['locations']

@app.route('/locations', methods=['GET'])
def get_locations():
    locations = list(collection.find({}, {'_id': 0, 'name': 1, 'coordinates.lat': 1, 'coordinates.lon': 1}))
    return jsonify(locations)

@app.route('/')
def serve_html():
    return send_from_directory('', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
