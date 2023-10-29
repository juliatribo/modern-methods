<template>
    <div>
        <HeaderComponent />
        <div class="container mt-5">
            <div v-if="show">
                <button @click="showForm = true" v-if="!showForm" class="btn btn-primary mb-3">Create Event Form</button>
                <form v-if="showForm">
                    <EventFormComponent @saveEventData="(options) => saveData(options)" />
                </form>
                <div v-if="!showForm">
                    <label for="Insert record ID">Event Number:</label>
                    <input type="text" class="form-control" v-model="recordNumberToGet">
                    <button @click="getEventData" class="btn btn-primary mb-3">Get Event</button>
                </div>
            </div>
            <form v-if="showData">
                <div>
                    <div class="form-group">
                        <label for="recordNumber">Record Number:</label>
                        <div>{{ recordNumber }}</div>
                    </div>
                    <div class="form-group">
                        <label for="clientName">Client Name:</label>
                        <div>{{ name }}</div>
                    </div>
                    <div class="form-group">
                        <label for="eventType">Event Type:</label>
                        <div>{{ eventType }}</div>
                    </div>
                    <div class="form-group">
                        <label for="dateFrom">From:</label>
                        <div>{{ dateFrom }}</div>
                    </div>
                    <div class="form-group">
                        <label for="dateTo">To:</label>
                        <div>{{ dateTo }}</div>
                    </div>
                    <div class="form-group">
                        <label for="attendees">Expected Number of Attendees:</label>
                        <div>{{ numAttendees }}</div>
                    </div>
                    <div class="form-group">
                        <label for="preferences">Preferences:</label>
                        <div>
                            <div v-for="preference in selectedPreferences" :key="preference">{{ preference }}</div>
                        </div>
                    </div>
                    <div v-if="selectedPreferences.length !== 0">
                        Selected Preferences:
                        <ul>
                            <li v-for="selectedPreference in selectedPreferences" :key="selectedPreference">{{
                                selectedPreference }}</li>
                        </ul>
                    </div>
                    <div class="form-group">
                        <label for="expectedBudget">Expected Budget:</label>
                        <div>{{ expectedBudget }}</div>
                    </div>
                    <div class="approval-field">
                        <label for="scs-approval">SCS Approval</label>
                        <input type="checkbox" v-model="scsStatus">
                    </div>
                    <div class="approval-field">
                        <label for="finance-report">Finance Report Submitted</label>
                        <input type="checkbox" v-model="financeStatus" disabled>
                    </div>
                    <div class="approval-field">
                        <label for="admin-approval">Admin Manager Approval</label>
                        <input type="checkbox" v-model="adminStatus" disabled>
                    </div>

                    <button @click="updateData">Submit status</button>


                </div>
            </form>
        </div>
    </div>
</template>
  
<script>
import EventFormComponent from '../components/EventFormComponent.vue';
export default {
    name: "CustomerView",
    data: function () {
        return {
            showForm: false,
            showEvent: false,
            recordNumber: "",
            name: "",
            eventType: "",
            dateFrom: "",
            dateTo: "",
            numAttendees: null,
            selectedPreferences: [],
            expectedBudget: null,
            financialData: {},
            showData: false,
            recordNumberToGet: null,
            show: true,
            scsStatus: false,
            adminStatus: false,
            financeStatus: false
        }
    },
    methods: {
        updateData() {
            let mydata = {
                recordNumber: this.recordNumber,
                name: this.name,
                eventType: this.eventType,
                dateFrom: this.dateFrom,
                dateTo: this.dateTo,
                numAttendees: this.numAttendees,
                selectedPreferences: this.selectedPreferences,
                expectedBudget: this.expectedBudget,
                scsStatus: this.scsStatus,
                adminStatus: this.adminStatus,
                financeStatus: this.financeStatus
            };
            this.saveData(mydata);
        },
        getEventData() {

            fetch('http://127.0.0.1:6002/get_event_data/' + this.recordNumberToGet, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log(data);
                    this.recordNumber = data.recordNumber;
                    this.name = data.name;
                    this.eventType = data.eventType;
                    this.dateFrom = data.dateFrom;
                    this.dateTo = data.dateTo;
                    this.showData = true;
                    this.show = false;
                    this.numAttendees = data.numAttendees;
                    this.selectedPreferences = data.selectedPreferences;
                    this.expectedBudget = data.expectedBudget;
                    this.scsStatus = data.scsStatus,
                        this.adminStatus = data.adminStatus,
                        this.financeStatus = data.financeStatus
                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
        },
        saveData(data) {
            const fetchResult = fetch('http://127.0.0.1:6002/add_event', {
                method: "POST",
                body: JSON.stringify(data, null, 2),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            console.log(fetchResult)


        },
        handleFinancialData(data) {
            this.financialData = data;
        }

    },
    components: {
        EventFormComponent
    }
}




</script>

<style scoped>
.event-form {
    margin: 20px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
    max-width: 600px;
    margin: 0 auto;
}

.form-group {
    margin-bottom: 20px;
}

.label {
    font-weight: bold;
}

.input {
    width: 100%;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 3px;
}

.btn {
    background-color: #007BFF;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 3px;
    cursor: pointer;
}

.btn:hover {
    background-color: #0056b3;
}

.value {
    background-color: #f9f9f9;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 3px;
}

.selected-preferences {
    list-style: none;
    padding: 0;
    margin: 0;
}

.selected-preferences li {
    margin-bottom: 5px;
}

.approval-field {
    margin: 10px 0;
}

.approval-field label {
    padding-right: 10px;
    /* Adjust the value to control the spacing */
}

.approval-field input[type="checkbox"] {
    margin-right: 5px;
    /* Small space between checkbox and label */
    transform: scale(1.2);
}
</style>



