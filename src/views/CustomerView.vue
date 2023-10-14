<template>
    <div>
        <body>
            <div>
                <form>
                    <div>
                        <label for="recordNumber">Record Number:</label>
                        <div>
                            <input type="text" id="recordNumber" name="recordNumber">
                        </div>
                    </div>
                    <div>
                        <label for="clientName">Client Name:</label>
                        <div>
                            <input type="text" name="clientName">
                        </div>
                    </div>
                    <div>
                        <label for="eventType">Event Type:</label>
                        <div>
                            <input type="text" name="eventType">
                        </div>
                    </div>
                    <div>
                        <label for="dateFrom">From:</label>
                        <div>
                            <input type="date" id="dateFrom" name="dateFrom">
                        </div>
                        <label for="dateTo">To:</label>
                        <div>
                            <input type="date" id="dateTo" name="dateTo">
                        </div>
                    </div>
                    <div>
                        <label for="attendees">Expected Number of Attendees:</label>
                        <div>
                            <input type="number" id="attendees" name="attendees">
                        </div>
                    </div>
                    <div>
                        <label for="preferences">Preferences:</label>
                        <div>
                            <div>
                                <input type="checkbox" id="decorations" name="preferences">
                                <label for="decorations">Decorations</label>
                            </div>
                            <div>
                                <input type="checkbox" id="parties" name="preferences">
                                <label for="parties">Parties</label>
                            </div>
                            <div>
                                <input type="checkbox" id="photosFilming" name="preferences">
                                <label for="photosFilming">Photos/Filming</label>
                            </div>
                            <div>
                                <input type="checkbox" id="breakfast" name="preferences">
                                <label for="breakfast">Breakfast</label>
                            </div>
                            <div>
                                <input type="checkbox" id="lunch" name="preferences">
                                <label for="lunch">Lunch</label>
                            </div>
                            <div>
                                <input type="checkbox" id="dinner" name="preferences">
                                <label for="dinner">Dinner</label>
                            </div>
                            <div>
                                <input type="checkbox" id="softDrinks" name="preferences">
                                <label for="softDrinks">Soft/Drinks</label>
                            </div>
                        </div>
                    </div>
                    <div>
                        <label for="expectedBudget">Expected Budget:</label>
                        <div>
                            <input type="text" id="expectedBudget" name="expectedBudget">
                        </div>
                    </div>
                    <div>
                        <div>
                            <button type="submit">Submit</button>
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

}

</script>

<style></style>