<template>
    <div>
        <HeaderComponent />
        <div class="container mt-5">
            <button @click="showForm = true" v-if="!showForm" class="btn btn-primary mb-3">Create Event Form</button>
            <form v-if="showForm">
                <div class="form-group">
                    <label for="recordNumber">Record Number:</label>
                    <div>
                        <input type="text" class="form-control" id="recordNumber" name="recordNumber">
                    </div>
                </div>
                <div class="form-group">
                    <label for="clientName">Client Name:</label>
                    <div>
                        <label for="clientName">Client Name:</label>
                        <div>
                            <input v-model="name" type="text" name="clientName">
                        </div>
                    </div>
                </div>
                <div class="form-group">
                    <label for="eventType">Event Type:</label>
                    <div>
                        <label for="eventType">Event Type:</label>
                        <div>
                            <input v-model="eventType" type="text" name="eventType">
                        </div>
                    </div>
                </div>
                <div class="form-group">
                    <label for="dateFrom">From:</label>
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
                    <label for="dateTo">To:</label>
                    <div>
                        <label for="attendees">Expected Number of Attendees:</label>
                        <div>
                            <input v-model="numAttendees" type="number" id="attendees" name="attendees">
                        </div>
                    </div>
                </div>
                <div class="form-group">
                    <label for="attendees">Expected Number of Attendees:</label>
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
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="decorations" name="preferences">
                            <label class="form-check-label" for="decorations">Decorations</label>
                        </div>
                        <!-- Include other preference checkboxes with the same structure -->
                    </div>
                </div>
                <div class="form-group">
                    <label for="expectedBudget">Expected Budget:</label>
                    <div>
                        <div>
                            <button type="submit" class="btn btn-primary">Submit</button>
                        </div>
                    </div>
                </div>
                <div class="form-group">
                    <div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                    </div>
                </div>
            </form>
        </div>
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
