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
                        <input type="text" class="form-control" name="clientName">
                    </div>
                </div>
                <div class="form-group">
                    <label for="eventType">Event Type:</label>
                    <div>
                        <input type="text" class="form-control" name="eventType">
                    </div>
                </div>
                <div class="form-group">
                    <label for="dateFrom">From:</label>
                    <div>
                        <input type="date" class="form-control" id="dateFrom" name="dateFrom">
                    </div>
                    <label for="dateTo">To:</label>
                    <div>
                        <input type="date" class="form-control" id="dateTo" name="dateTo">
                    </div>
                </div>
                <div class="form-group">
                    <label for="attendees">Expected Number of Attendees:</label>
                    <div>
                        <input type="number" class="form-control" id="attendees" name="attendees">
                    </div>
                </div>
                <div class="form-group">
                    <label for="preferences">Preferences:</label>
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
                        <button type="submit" class="btn btn-primary">Submit</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>
  
<script>
import HeaderComponent from '../components/HeaderComponent.vue';
export default {
    name: "CustomerView",
    data() {
        return {
            showForm: false,
        };
    },
    components: {
        HeaderComponent
    }
};
</script>
  
<style></style>