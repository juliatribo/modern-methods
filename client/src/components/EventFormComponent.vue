<template>
    <form>
        <div class="form-group">
            <label for="recordNumber">Record Number:</label>
            <div>
                <input type="text" class="form-control" id="recordNumber" name="recordNumber" v-model="recordNumber">
            </div>
        </div>
        <div class="form-group">
            <div>
                <label for="clientName">Client Name:</label>
                <div>
                    <input v-model="name" type="text" name="clientName">
                </div>
            </div>
        </div>
        <div class="form-group">
            <div>
                <label for="eventType">Event Type:</label>
                <div>
                    <input v-model="eventType" type="text" name="eventType">
                </div>
            </div>
        </div>
        <div class="form-group">
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
                        <input type="checkbox" id="photosFilming" value="photosFilming" v-model="selectedPreferences">
                        <label for="photosFilming">Photos/Filming</label>
                    </div>
                    <div>
                        <input type="checkbox" id="breakfast" value="breakfast" v-model="selectedPreferences">
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
            <div v-if="selectedPreferences.length != 0">
                Selected Preferences:
                <ul>
                    <li v-for="selectedPreference in selectedPreferences" :key="selectedPreference">{{
                        selectedPreference }}</li>
                </ul>
            </div>
            <div>
                <div class="form-check">
                    <input type="checkbox" class="form-check-input" id="decorations" name="preferences">
                    <label class="form-check-label" for="decorations">Decorations</label>
                </div>
                <div class="form-check">
                    <input type="checkbox" class="form-check-input" id="parties" name="preferences">
                    <label class="form-check-label" for="parties">Parties</label>
                </div>
                <div class="form-check">
                    <input type="checkbox" class="form-check-input" id="photos" name="preferences">
                    <label class="form-check-label" for="photos">Photos/Filming</label>
                </div>
                <div class="form-check">
                    <input type="checkbox" class="form-check-input" id="breakfast" name="preferences">
                    <label class="form-check-label" for="breakfast">Breakfast, lunch, dinner</label>
                </div>
                <div class="form-check">
                    <input type="checkbox" class="form-check-input" id="drinks" name="preferences">
                    <label class="form-check-label" for="drinks">Soft/ hot drinks</label>
                </div>
                <!-- Include other preference checkboxes with the same structure -->
            </div>
        </div>
        <div class="form-group">
            <label for="expectedBudget">Expected Budget:</label>
            <div>
                <input type="text" class="form-control" id="expectedBudget" name="expectedBudget">
            </div>
        </div>
        <div class="form-group">
            <div>
                <button type="submit" class="btn btn-primary" @click="saveData">Submit</button>
            </div>
        </div>
    </form>
</template>
<script>

export default {
    name: "EventFormComponent",
    data() {
        return {
            recordNumber: "",
            name: "",
            eventType: "",
            dateFrom: "",
            dateTo: "",
            numAttendees: null,
            selectedPreferences: [],
            expectedBudget: null
        }
    },
    methods: {
        saveData() {
            this.$emit("saveEventData", {
                recordNumber: this.recordNumber,
                name: this.name,
                eventType: this.eventType,
                dateFrom: this.dateFrom,
                dateTo: this.dateTo,
                numAttendees: this.numAttendees,
                selectedPreferences: this.selectedPreferences,
                expectedBudget: this.expectedBudget
            });
        }
    }

}

</script>