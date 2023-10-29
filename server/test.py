from server import process_add_event, process_get_tasks

import os

def test_process_add_data():
    request = {"recordNumber": 1,
                "name": "natassa",
                "eventType": "dinner",
                "dateFrom": "30/11/1993",
                "dateTo": "30/12/1993",
                "numAttendees":10,
                "selectedPreferences": [],
                "expectedBudget": 3000}
    process_add_event(request)



def test_get_tasks():
    department="human_resources"
    path_to_tasks = f"data/tasks/{department}"
    result = process_get_tasks(path_to_tasks)
    print(result)

# test_process_add_data()
test_get_tasks()