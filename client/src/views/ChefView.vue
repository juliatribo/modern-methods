<template>
    <div>
        <HeaderComponent />
        <div class="sliding-box">
            <h2>Tasks</h2>
            <div class="slides">
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
    </div>
</template>

<script>
import HeaderComponent from '../components/HeaderComponent.vue';
export default {
    name: "ChefView",
    data: function () {
        return {
            tasks: []
        }
    },
    mounted() {
        this.fetchTasks();
    },
    methods: {
        async fetchTasks() {
            try {
                const response = await fetch('http://127.0.0.1:6002/get_serv_tasks');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                this.tasks = data.serv_tasks;
            } catch (error) {
                console.error('Error fetching finance reports:', error);
            }
        },

    },
    components: {
        HeaderComponent
    }
}
</script>
<style>
.sliding-box {
    width: 80%;
    max-width: 800px;
    margin: 20px auto;
    background-color: #f5f5f5;
    padding: 20px;
    border-radius: 10px;
}

.slides {
    display: flex;
    flex-direction: column;
}

.slide {
    display: flex;
    flex-direction: column;
    position: relative;
    margin: 10px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #ffffff;
}

.content {
    flex: 1;
}
</style>