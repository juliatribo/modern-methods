<template>
    <div>
        <HeaderComponent />
        <div class="container mt-5">
            <button @click="showForm = true" v-if="!showForm" class="btn btn-primary mb-3">Create Event Form</button>
            <form v-if="showForm">
                <EventFormComponent @saveEventData="(options)=>saveData(options)" />
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
            financialData: {}
        }
    },
    methods: {
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
</style>



