<template>
    <div>
        <HeaderComponent />
        <div class="container mt-5">
            <div class="stack">
                <button @click="showForm = true" v-if="!showForm" class="btn btn-primary mb-3">
                    Create Financial Request
                </button>
                <form v-if="showForm">
                    <div class="form-group">
                        <label for="projectReference">Project Reference:</label>
                        <div>
                            <input type="text" class="form-control" id="projectReference" name="projectReference"
                                v-model="projectReference">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="requiredAmount">Required Amount:</label>
                        <div>
                            <input type="text" class="form-control" id="requiredAmount" name="requiredAmount"
                                v-model="requiredAmount">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="reason">Reason:</label>
                        <div>
                            <input type="text" class="form-control" id="reason" name="reason" v-model="reason">
                        </div>
                    </div>
                    <div class="form-group">
                        <div>
                            <button type="submit" class="btn btn-primary" @click="updateData">
                                Submit
                            </button>
                        </div>
                    </div>
                </form>
            </div>
            <button @click="showTask = true" v-if="!showTask" class="btn btn-primary mb-3">
                Create Task
            </button>
            <form v-if="showTask">
                <div class="form-group">
                    <label for="projectReferenceTask">Project Reference:</label>
                    <div>
                        <input type="text" class="form-control" id="projectReferenceTask" name="projectReferenceTask"
                            v-model="projectReferenceTask">
                    </div>
                </div>
                <div class="form-group">
                    <label for="descriptionTask">Description:</label>
                    <div>
                        <input type="text" class="form-control" id="descriptionTask" name="descriptionTask"
                            v-model="descriptionTask">
                    </div>
                </div>
                <div>
                    <b-dropdown text="Assign to:" variant="assignedTo" class="m-2">
                        <b-dropdown-item @click="setToPhoto" href="#">Photography subteam</b-dropdown-item>
                    </b-dropdown>
                </div>
                <div>
                    <b-dropdown text="Priority" variant="priority" class="m-2">
                        <b-dropdown-item @click="setPrioLow" href="#">Low</b-dropdown-item>
                        <b-dropdown-item @click="setPrioMed" href="#">Medium</b-dropdown-item>
                        <b-dropdown-item @click="setPrioHigh" href="#">High</b-dropdown-item>
                    </b-dropdown>
                </div>
                <div class="form-group">
                    <div>
                        <button type="submit" class="btn btn-primary" @click="updateTask">
                            Submit
                        </button>
                    </div>
                </div>

            </form>


            <div class="boxes-container">
                <div class="sliding-box">
                    <h4>Accepted Financial Requests</h4>
                    <div v-for="(report, index) in acceptedReq" :key="index" class="slide">
                        <div class="content">
                            <p><strong>Project Reference:</strong> {{ report.projectReference }}</p>
                            <p><strong>Required Amount:</strong> {{ report.requiredAmount }}</p>
                            <p><strong>Reason:</strong> {{ report.reason }}</p>
                        </div>
                    </div>
                </div>
                <div class="sliding-box">
                    <h4>Denied Financial Requests</h4>
                    <div v-for="(report, index) in deniedReq" :key="index" class="slide">
                        <div class="content">
                            <p><strong>Project Reference:</strong> {{ report.projectReference }}</p>
                            <p><strong>Required Amount:</strong> {{ report.requiredAmount }}</p>
                            <p><strong>Reason:</strong> {{ report.reason }}</p>
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
    name: "ProductView",
    data: function () {
        return {
            showForm: false,
            showTask: false,
            selectedDepartment: "Production",
            projectReference: null,
            requiredAmount: null,
            reason: "",
            acceptedReq: [],
            deniedReq: [],
            projectReferenceTask: null,
            descriptionTask: "",
            assignTo: "",
            prio: ""

        }
    },
    mounted() {
        this.getAcceptedReq();
        this.getDeniedReq();
    },
    methods: {
        async getAcceptedReq() {
            try {
                const response = await fetch('http://127.0.0.1:6002/get_finance_accepted');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                this.acceptedReq = data.acc_requests.filter((report) => report.selectedDepartment === "Production");
            } catch (error) {
                console.error('Error fetching finance reports:', error);
            }
        },
        async getDeniedReq() {
            try {
                const response = await fetch('http://127.0.0.1:6002/get_finance_denied');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                this.deniedReq = data.den_requests.filter((report) => report.selectedDepartment === "Production");
            } catch (error) {
                console.error('Error fetching finance reports:', error);
            }
        },
        updateData() {
            let mydata = {
                selectedDepartment: this.selectedDepartment,
                projectReference: this.projectReference,
                requiredAmount: this.requiredAmount,
                reason: this.reason
            };
            this.saveData(mydata);
        },
        saveData(data) {
            const fetchResult = fetch('http://127.0.0.1:6002/add_finance_report', {
                method: "POST",
                body: JSON.stringify(data, null, 2),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            console.log(fetchResult)


        },
        updateTask() {
            let mydata = {
                projectReferenceTask: this.projectReferenceTask,
                descriptionTask: this.descriptionTask,
                assignTo: this.assignTo,
                prio: this.prio
            };
            this.saveTask(mydata);
        },
        saveTask(data) {
            const fetchResult = fetch('http://127.0.0.1:6002/add_product_task', {
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
        },
        setPrioLow() {
            this.prio = "Low";
        },
        setPrioMed() {
            this.prio = "Medium";
        },
        setPrioHigh() {
            this.prio = "High";
        },
        setToPhoto() {
            this.assignTo = "Photography";
        }

    },
    components: {
        HeaderComponent
    }
}
</script>
<style>
.boxes-container {
    display: flex;
    margin-top: 20px;
}

.sliding-box {
    flex: 1;
    width: 45%;
    margin-right: 20px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
}

.slides {
    display: flex;
    flex-direction: column;
}

.slide {
    margin: 10px;
    padding: 10px;
    border: 1px solid #e1e1e1;
    border-radius: 5px;
    background-color: #ffffff;
    display: flex;
    justify-content: space-between;
}

.button-container {
    margin-top: 10px;
}

/* Adjusted styles */
button {
    margin-right: 20px;
}
</style>