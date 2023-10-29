<template>
    <div>
        <HeaderComponent />

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
            financeReports: []
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