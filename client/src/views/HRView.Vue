<template>
    <div>
        <HeaderComponent />
        <div>
            <button @click="createTask" class="btn btn-primary mb-3">Create task</button>
                <form v-if="showTaskForm">
                    <div class="form-container">
                        <div class="form-group">
                            <label>Title:</label>
                            <input type="text" v-model="taskTitle">
                        </div>
                        <div class="form-group">
                            <label>Assigned to:</label>
                            <input type="text" v-model="assigneeName">
                        </div>
                        <div class="form-group">
                            <label for="description-box">Description:</label>
                            <textarea id="description-box" v-model="description" class="large-input" rows="4"></textarea>
                        </div>
                        <div class="form-group">
                            <label>Date due:</label>
                            <input type="date" v-model="dateDue">   
                        </div>
                    <button class="btn btn-primary mb-3" @click="saveTask">Submit task</button>
                </div>
            </form>
        </div>
        <div>
            <button class="btn btn-primary mb-3">Check my tasks names</button>
        </div>
        <div>
            <label for="description-box">Search task ID:</label>
            <input v-model="taskIdTarget"> 
            <button class="btn btn-primary mb-3" @click="getTask">Get task</button>
        </div>
    </div>
</template>

<script>
import HeaderComponent from '../components/HeaderComponent.vue';
export default {
    name: "HRView",
    components: {
        HeaderComponent
    },
    data(){
        return {
            taskID:0,
            showTaskForm:false,
            taskTitle: "",
            description:"",
            assigneeName:null,
            dateDue:"",  
            department:"HR",
            taskIdTarget:""
        }
    },
    methods:{
        createTask(){
            this.showTaskForm=true;
        },
        saveTask() {
            const data = {
                title:this.taskTitle,
                description: this.description,
                assigneeName: this.assigneeName,
                dateDue: this.dateDue,
                department: this.department,
                taskID:String(this.taskID+1)
            };
            const fetchResult = fetch('http://127.0.0.1:6002/add_task', {
                method: "POST",
                body: JSON.stringify(data, null, 2),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            console.log(fetchResult)
        },
        getTask(){
            const fetchResult = fetch('http://127.0.0.1:6002/get_task/'+this.taskIdTarget, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json'
                }
            })
        }
    }
}
</script>

<style>

.input {
    width: 100%;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 3px;
}

.form-group {
    margin-bottom: 20px;
}

.large-input {
  display: block; 
  width: 30%;   
}

.form-container {
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 5px;
  background-color: #f5f5f5;
  margin: 10px;
}

</style>