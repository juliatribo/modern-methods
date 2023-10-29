<template>
    <div>
        <HeaderComponent />
        <div class="sliding-box with-scroll">
        <div v-if="!showForm">
                    <label for="Insert record ID">Event Number:</label>
                    <input type="text" class="form-control" v-model="recordNumberToGet">
                    <button @click="getEventData" class="btn btn-primary mb-3">Get Event</button>
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
                    <input type="checkbox" v-model="scsStatus" disabled>
                </div>
                <div class="approval-field">
                    <label for="finance-report">Finance Report Submitted</label>
                    <input type="checkbox" v-model="financeStatus">
                </div>
                <div class="approval-field">
                    <label for="admin-approval">Admin Manager Approval</label>
                    <input type="checkbox" v-model="adminStatus" disabled>
                </div>

                <button @click="updateData">Submit status</button>


            </div>
        </form>
        </div>
        <div class="sliding-box with-scroll">
            <h4>Financial Requests</h4>
            <div v-for="(report, index) in financeReports" :key="index" class="slide">
                <div class="content">
                    <p><strong>Selected Department:</strong> {{ report.selectedDepartment }}</p>
                    <p><strong>Project Reference:</strong> {{ report.projectReference }}</p>
                    <p><strong>Required Amount:</strong> {{ report.requiredAmount }}</p>
                    <div class="reason-and-buttons">
                        <div class="reason-container">
                            <strong>Reason:</strong>
                            <span>{{ report.reason }}</span>
                        </div>
                        <div class="buttons">
                            <button class="btn btn-success" @click="acceptReport(index)">Accept</button>
                            <button class="btn btn-danger" @click="denyReport(index)">Deny</button>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import HeaderComponent from '../components/HeaderComponent.vue';
export default {
    name: "FinanceView",
    components: {
        HeaderComponent
    },
    data() {
        return {
            financeReports: [],
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
    mounted() {
        this.fetchFinanceReports();
    },
    methods: {
        async fetchFinanceReports() {
            try {
                const response = await fetch('http://127.0.0.1:6002/get_finance_data');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                this.financeReports = data.fin_requests;
            } catch (error) {
                console.error('Error fetching finance reports:', error);
            }
        },
        async acceptReport(index) {
            const fetchResult = fetch('http://127.0.0.1:6002/add_accepted_req', {
                method: "POST",
                body: JSON.stringify(this.financeReports[index], null, 2),
                headers: {
                    'Content-Type': 'application/json'
                }
            })

            const keyToDelete = this.financeReports[index].id;
            try {
                const response = await fetch(`http://127.0.0.1:6002/delete_finance_component/${keyToDelete}`, {
                    method: 'DELETE',
                });
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                console.log(data.message);
                this.fetchFinanceReports();
            } catch (error) {
                console.error('Error deleting finance component:', error);
            }
            console.log('Denied report:', this.financeReports[index]);

            console.log(fetchResult);
        },
        async denyReport(index) {
            const fetchResult = fetch('http://127.0.0.1:6002/add_denied_req', {
                method: "POST",
                body: JSON.stringify(this.financeReports[index], null, 2),
                headers: {
                    'Content-Type': 'application/json'
                }
            })

            const keyToDelete = this.financeReports[index].id;
            try {
                const response = await fetch(`http://127.0.0.1:6002/delete_finance_component/${keyToDelete}`, {
                    method: 'DELETE',
                });
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                console.log(data.message);
                this.fetchFinanceReports();
            } catch (error) {
                console.error('Error deleting finance component:', error);
            }
            console.log('Denied report:', this.financeReports[index]);


            console.log(fetchResult);
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
    }

}

</script>
<style>

.sliding-box.with-scroll {
    height: 600px;
    /* Set the desired height */
    overflow-y: auto;
    /* Enable vertical scrollbar */
    margin-top: 10px;
    /* Adjust margin-top as needed */

}

.content-container {
    width: 100%;
    /* Adjust width as needed */
}

.slide {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ddd;
}

.content {
    flex: 1;
}

.reason-and-buttons {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.reason-container {
    display: flex;
    align-items: center;
}

.buttons button {
    margin-left: 10px;
}
</style>