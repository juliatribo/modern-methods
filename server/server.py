import json
from typing import Dict

from flask import Flask, request, jsonify

app = Flask(__name__)


def process_add_event(request: Dict):
    with open("data/event.json", "w") as f:
        json.dump(request, f)
    return {"status": "ok"}


@app.route('/get_event_data', methods=['GET'])
def get_data():
    with open("data/event.json", "r") as f:
        event = json.load(f)
    return jsonify(event)


@app.route('/add_event', methods=['POST'])
def add_data():
    request_data = request.get_json()
    response = process_add_event(request_data)
    return jsonify(response)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # prometheus_client.start_http_server(6003)
    app.run(host='0.0.0.0', port=6002, threaded=False)
