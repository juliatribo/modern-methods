<template>
    <div>
        <HeaderComponent />
        <div class="sliding-box">
            <h4>Tasks</h4>
            <div class="slides">
                <div v-for="(report, index) in tasks" :key="index" class="slide">
                    <div class="content">
                        <p><strong>Project Reference:</strong> {{ report.projectReferenceTask }}</p>
                        <p><strong>Description:</strong> {{ report.descriptionTask }}</p>
                        <p><strong>Priority:</strong> {{ report.prio }}</p>
                        <div>
                            <button class="btn btn-success" @click="Comment(index)">Add comment</button>
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
                this.tasks = data.prod_tasks;
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