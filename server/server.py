import json
from typing import Dict
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def decode_department(department):
    if department=="HR" or department=="humanResources":
        return "human_resources"

def process_add_event(request: Dict):
    record_id = request["recordNumber"]
    with open(f"data/event_requests/event_{record_id}.json", "w") as f:
        json.dump(request, f)
    return {"status": "ok"}

def process_add_task(request: Dict):
    task_id = request["taskID"]
    department = decode_department(request["department"])
    with open(f"data/tasks/{department}/task_{task_id}.json", "w") as f:
        json.dump(request, f)
    return {"status": "ok"}

def process_add_finance_report(request: Dict):
    with open("data/finance_req.json", "w") as f:
        json.dump(request, f)
    return {"status": "ok"}

@cross_origin()
@app.route('/get_event_data/<int:record_id>', methods=['GET'])
def get_data(record_id):
    with open(f"data/event_requests/event_{record_id}.json", "r") as f:
        event = json.load(f)
    return jsonify(event)


@app.route('/add_event', methods=['POST'])
def add_data():
    print("Running add data  ")
    print("data", request.get_json())
    request_data = request.get_json()
    response = process_add_event(request_data)
    return jsonify(response)

@app.route('/add_task', methods=['POST'])
def add_task():
    print("Running add task")
    print("task", request.get_json())
    request_data = request.get_json()
    response = process_add_task(request_data)
    return jsonify(response)

@app.route('/get_finance_data', methods=['GET'])
@cross_origin()
def get_finance_data():
    with open("data/finance_req.json", "r") as f:
        event = json.load(f)
    return jsonify(event)


@app.route('/add_finance_report', methods=['POST'])
def add_finance_data():
    print("Running add data")
    request_data = request.get_json()
    response = process_add_finance_report(request_data)
    return jsonify(response)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # prometheus_client.start_http_server(6003)
    app.run(host='0.0.0.0', port=6002, threaded=False)
