<template>
    <div>
        <HeaderComponent />

        <div class="sliding-box with-scroll">
            <h4>Tasks</h4>
            <div v-for="(report, index) in tasks" :key="index" class="slide">
                <div class="content">
                    <p><strong>Project Reference:</strong> {{ report.projectReferenceTask }}</p>
                    <p><strong>Description:</strong> {{ report.descriptionTask }}</p>
                    <p><strong>Priority:</strong> {{ report.prio }}</p>
                    <div class="form-group">
                        <p><strong>Comment:</strong> </p>
                        <div>
                            <input type="text" class="form-control" id="textBox" name="textBox" v-model="report.comment">
                        </div>
                        <button @click="submitData(index, report.comment)" class="btn btn-primary mt-3">Submit</button>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import HeaderComponent from '../components/HeaderComponent.vue';
export default {
    name: "PhotographyView",
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
                const response = await fetch('http://127.0.0.1:6002/get_prod_tasks');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                this.tasks = data.prod_tasks.filter((report) => report.comment === "");
            } catch (error) {
                console.error('Error fetching finance reports:', error);
            }
        },
        submitData(index, comment) {
            let mydata = {
                id: this.tasks[index].id,
                projectReferenceTask: this.tasks[index].projectReferenceTask,
                descriptionTask: this.tasks[index].descriptionTask,
                assignTo: this.tasks[index].assignTo,
                prio: this.tasks[index].prio,
                comment: comment
            };
            const fetchResult = fetch('http://127.0.0.1:6002/edit_prod_task', {
                method: "POST",
                body: JSON.stringify(mydata, null, 2),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            console.log(fetchResult)
            window.location.reload()

        }

    },
    components: {
        HeaderComponent
    }
}
</script>
<style>
.sliding-box.with-scroll {
    height: 500px;
    width: 80%;
    /* Set the desired height */
    overflow-y: auto;
    /* Enable vertical scrollbar */
    margin-top: 20px;
    /* Adjust margin-top as needed */
    width: 80%;
    max-width: 800px;
    margin: 20px auto;
    background-color: #f5f5f5;
    padding: 20px;
    border-radius: 10px;
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
</style>