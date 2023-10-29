<template>
    <div>
        <HeaderComponent />
        <div>
            <h3>Human Resources Platform</h3>
            <button @click="createTask" class="btn btn-primary mb-3">Create task</button>
            <form v-if="showTaskForm">
                <div class="form-container">
                    <div class="form-group">
                        <label>TaskID:</label>
                        <input type="text" v-model="taskID" id="taskID" name="taskID" >
                    </div>
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
            <button @click="getTasks" class="btn btn-primary mb-3">Check my tasks</button>
        </div>

        <div v-if="tasks.length > 0" id="app">
            <h4>Task List</h4>
            <ul>
                <li v-for="task in tasks" :key="task">{{ task }}</li>
            </ul>
        </div>

        <div>
            <label>Task id:</label>
            <input type="text" v-model="taskIDtoGet" id="taskIDtoGet" name="taskIDtoGet" >
            <button @click="getTaskwithID" class="btn btn-primary mb-3">Get task</button>
        </div>

        <form v-if="showTask">
            <div class="form-container">
                <div class="form-group">
                    <label>TaskID:</label>
                    {{taskIDtoGet}}
                </div>
                <div class="form-group">
                    <label>Title:</label>
                    {{taskTitle}}
                </div>

                <div class="form-group">
                    <label>Assigned to:</label>
                    {{assigneeName}}
                </div>

                <div class="form-group">
                    <label for="description-box">Description:</label>
                    {{description}}
                </div>

                <div class="form-group">
                    <label>Date due:</label>
                    <div>{{dateDue}}</div>
                    <input type="date" v-model="dateDue">   
                </div>
            </div>
        </form>

</div>
</template>

<script>
import HeaderComponent from '../components/HeaderComponent.vue';
export default {
    name: "HView",
    components: {
        HeaderComponent
    },
    data(){
        return {
            taskID:"",
            showTaskForm:false,
            taskTitle: "",
            description:"",
            assigneeName:null,
            dateDue:"",  
            department:"humanResources",
            tasks:[],
            taskIDtoGet:"",
            showTask:false
        }
    },
    methods:{
        getTasks(){
            const department = "humanResources";
            fetch('http://127.0.0.1:6002/get_tasks/' + department, {
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
                    this.tasks = data.tasks;
                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
        },
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
                taskID:String(this.taskID)
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
        getTaskwithID(){
            this.showTaskForm=false;
            const department = "humanResources";
            fetch('http://127.0.0.1:6002/get_task_by_id/' + department + '/' + this.taskIDtoGet, {
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
                    this.showTask=true,
                    this.taskTitle=data.task.title,
                    this.description=data.task.description,
                    this.assigneeName=data.task.assigneeName,
                    this.dateDue=data.task.dateDue,  
                    this.taskIDtoGet=data.task.taskID
                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
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