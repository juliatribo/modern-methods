<template>
    <div>
        <HeaderComponent />
        <div class="container mt-5">
            <button @click="showForm = true" v-if="!showForm" class="btn btn-primary mb-3">Create Financial Request</button>
            <form v-if="showForm">
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
                        <button type="submit" class="btn btn-primary" @click="updateData">Submit</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import HeaderComponent from '../components/HeaderComponent.vue';
export default {
    name: "ServiceView",
    data: function () {
        return {
            showForm: false,
            selectedDepartment: "Service",
            projectReference: Math.floor(Math.random() * 10000) + 1,
            requiredAmount: null,
            reason: ""
        }
    },
    methods: {
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
        handleFinancialData(data) {
            this.financialData = data;
        }

    },
    components: {
        HeaderComponent
    }
}
</script>
<style></style>