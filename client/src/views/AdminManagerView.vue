<template>
    <div>
        <HeaderComponent />
        <div v-if="!showData">
            <label for="Insert record ID">Record Number:</label>
            <input type="text" class="form-control" v-model="recordNumberToGet">
            <button @click="getEventData"  class="btn btn-primary mb-3">Get Event</button>
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
                    <li v-for="selectedPreference in selectedPreferences" :key="selectedPreference">{{ selectedPreference }}</li>
                </ul>
                </div>
                <div class="form-group">
                <label for="expectedBudget">Expected Budget:</label>
                <div>{{ expectedBudget }}</div>
                </div>
                <div class="approval-field">
                    <label for="scs-approval">SCS Approval</label>
                    <input type="checkbox" v-model="scsStatus" disabled>
                </div>
                <div class="approval-field">
                    <label for="finance-report">Finance Report Submitted</label>
                    <input type="checkbox" v-model="financeStatus" disabled>
                </div>
                <div class="approval-field">
                    <label for="admin-approval">Admin Manager Approval</label>
                    <input type="checkbox" v-model="adminStatus">
                </div>


                <button @click="updateData">Submit status</button>


            </div>
        </form>
    </div>
</template>

<script>
import HeaderComponent from '../components/HeaderComponent.vue';
export default {
    name: "AdminManagerView",
    components: {
        HeaderComponent
    },
    data: function () {
        return {
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
            recordNumberToGet:null,
            show:true,
            scsStatus:false,
            adminStatus:false,
            financeStatus:false
        }
    },
    methods: {
        updateData(){
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
        getEventData(){
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
                    this.recordNumber=data.recordNumber;
                    this.name = data.name;
                    this.eventType = data.eventType;
                    this.dateFrom = data.dateFrom;
                    this.dateTo = data.dateTo;
                    this.showData = true;
                    this.show=false;
                    this.numAttendees = data.numAttendees;
                    this.selectedPreferences = data.selectedPreferences;
                    this.expectedBudget = data.expectedBudget;
                    this.scsStatus=data.scsStatus,
                    this.adminStatus=data.adminStatus,
                    this.financeStatus=data.financeStatus
                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
        },
    }
}

</script>

<style>

</style>

