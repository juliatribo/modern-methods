<template>
    <div class="event-form">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Event Planning Request Form</title>
        </head>
        <body>
            <div>
                <form>
                    <div class="form-group ">
                        <label >Record Number:</label>
                        <div>
                            <input v-model="recordNumber"  type="text" id="recordNumber" name="recordNumber">
                        </div>
                    </div>
                    <div>
                        <label for="clientName">Client Name:</label>
                        <div>
                            <input v-model="name" type="text" name="clientName">
                        </div>
                    </div>
                    <div>
                        <label for="eventType">Event Type:</label>
                        <div>
                            <input v-model="eventType" type="text" name="eventType">
                        </div>
                    </div>
                    <div>
                        <label for="dateFrom">From:</label>
                        <div>
                            <input v-model="dateFrom" type="date" id="dateFrom" name="dateFrom">
                        </div>
                        <label for="dateTo">To:</label>
                        <div>
                            <input v-model="dateTo" type="date" id="dateTo" name="dateTo">
                        </div>
                    </div>
                    <div>
                        <label for="attendees">Expected Number of Attendees:</label>
                        <div>
                            <input v-model="numAttendees" type="number" id="attendees" name="attendees">
                        </div>
                    </div>
                    <div>
                        <label for="preferences">Preferences:</label>
                        <div>
                            <div>
                                <input type="checkbox" id="decorations" value="decorations" v-model="selectedPreferences">
                                <label for="decorations">Decorations</label>
                            </div>
                            <div>
                                <input type="checkbox" id="parties" value="parties" v-model="selectedPreferences">
                                <label for="parties">Parties</label>
                            </div>
                            <div>
                                <input type="checkbox" id="photosFilming" value="photosFilming"  v-model="selectedPreferences">
                                <label for="photosFilming">Photos/Filming</label>
                            </div>
                            <div>
                                <input type="checkbox" id="breakfast" value="breakfast" v-model="selectedPreferences" >
                                <label for="breakfast">Breakfast</label>
                            </div>
                            <div>
                                <input type="checkbox" id="lunch" value="lunch" v-model="selectedPreferences">
                                <label for="lunch">Lunch</label>
                            </div>
                            <div>
                                <input type="checkbox" id="dinner" value="dinner" v-model="selectedPreferences">
                                <label for="dinner">Dinner</label>
                            </div>
                            <div>
                                <input type="checkbox" id="softDrinks" value="softDrinks" v-model="selectedPreferences">
                                <label for="softDrinks">Soft/Drinks</label>
                            </div>
                        </div>
                    </div>
                    <div v-if="selectedPreferences.length!=0">
                        Selected Preferences:
                            <ul>
                                <li v-for="selectedPreference in selectedPreferences" :key="selectedPreference">{{ selectedPreference }}</li>
                            </ul>
                    </div>
                    <div>
                        <label for="expectedBudget">Expected Budget:</label>
                        <div>
                            <input type="text" id="expectedBudget" name="expectedBudget">
                        </div>
                    </div>
                    <div>
                        <div>
                            <button type="submit" class="btn btn-primary">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </body>
    </div>
</template>

<script>

export default {
    name: "CustomerView",
    data:function () {
        return {
            recordNumber: "",
            name: "",
            eventType: "",
            dateFrom: "",
            dateTo: "",
            numAttendees:null,
            selectedPreferences:[],
            expectedBudget:null
        }
    },
    method:{
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