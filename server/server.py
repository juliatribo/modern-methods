import json
from typing import Dict
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def decode_department(department):
    if department == "HR" or department == "humanResources":
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


def process_add_finance_report(new_data):
    filename = 'data/finance_req.json'
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["fin_requests"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    return {"status": "ok"}


def process_add_accepted_req(new_data):
    filename = 'data/finance_req_acc.json'
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["acc_requests"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    return {"status": "ok"}


def process_add_denied_req(new_data):
    filename = 'data/finance_req_den.json'
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["den_requests"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    return {"status": "ok"}


def process_add_product_task(new_data):
    filename = 'data/task_prod.json'
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["prod_tasks"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    return {"status": "ok"}


def process_add_serv_task(new_data):
    filename = 'data/task_serv.json'
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["serv_tasks"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    return {"status": "ok"}


def edit_prod_task(new_data):
    with open("data/task_prod.json", "r") as file:
        data = json.load(file)
        for task in data['prod_tasks']:
            if task['id'] == new_data.get('id'):
                # Update the specific task's comment
                task['comment'] = new_data.get('comment')
                break  # Exit loop once the task is found

    with open("data/task_prod.json", "w") as file:
        json.dump(data, file, indent=4)


def edit_serv_task(new_data):
    with open("data/task_serv.json", "r") as file:
        data = json.load(file)
        for task in data['serv_tasks']:
            if task['id'] == new_data.get('id'):
                # Update the specific task's comment
                task['comment'] = new_data.get('comment')
                break  # Exit loop once the task is found

    with open("data/task_serv.json", "w") as file:
        json.dump(data, file, indent=4)


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


@app.route('/get_finance_accepted', methods=['GET'])
@cross_origin()
def get_finance_accepted_data():
    with open("data/finance_req_acc.json", "r") as f:
        event = json.load(f)
    return jsonify(event)


@app.route('/add_accepted_req', methods=['POST'])
def add_accepted_fin_data():
    print("Running add data")
    request_data = request.get_json()
    response = process_add_accepted_req(request_data)
    return jsonify(response)


@app.route('/get_finance_denied', methods=['GET'])
@cross_origin()
def get_finance_denied_data():
    with open("data/finance_req_den.json", "r") as f:
        event = json.load(f)
    return jsonify(event)


@app.route('/add_denied_req', methods=['POST'])
def add_denied_fin_finance_data():
    print("Running add data")
    request_data = request.get_json()
    response = process_add_denied_req(request_data)
    return jsonify(response)


@app.route('/delete_finance_component/<key_to_delete>', methods=['DELETE'])
def delete_finance_component(key_to_delete):
    try:
        with open("data/finance_req.json", "r") as f:
            data = json.load(f)

        for item in data['fin_requests']:
            if item.get('id') == int(key_to_delete):
                data['fin_requests'].remove(item)
                with open("data/finance_req.json", "w") as f:
                    json.dump(data, f, indent=4)
                return jsonify({'message': f'Successfully deleted {key_to_delete}'}), 200

        return jsonify({'error': f'Key {key_to_delete} not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/add_product_task', methods=['POST'])
def add_product_task():
    print("Running add data")
    request_data = request.get_json()
    response = process_add_product_task(request_data)
    return jsonify(response)


@app.route('/add_service_task', methods=['POST'])
def add_service_task():
    print("Running add data")
    request_data = request.get_json()
    response = process_add_serv_task(request_data)
    return jsonify(response)


@app.route('/get_prod_tasks', methods=['GET'])
@cross_origin()
def get_task_prod():
    with open("data/task_prod.json", "r") as f:
        event = json.load(f)
    return jsonify(event)


@app.route('/get_serv_tasks', methods=['GET'])
@cross_origin()
def get_task_serv():
    with open("data/task_serv.json", "r") as f:
        event = json.load(f)
    return jsonify(event)


@app.route('/edit_prod_task', methods=['POST'])
def edit_task_prod():
    request_data = request.get_json()
    print(request_data)
    edit_prod_task(request_data)
    return jsonify({"status": "Comment edited successfully"})


@app.route('/edit_serv_task', methods=['POST'])
def edit_task_serv():
    request_data = request.get_json()
    print(request_data)
    edit_serv_task(request_data)
    return jsonify({"status": "Comment edited successfully"})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # prometheus_client.start_http_server(6003)
    app.run(host='0.0.0.0', port=6002, threaded=False)
