from server import process_add_event


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