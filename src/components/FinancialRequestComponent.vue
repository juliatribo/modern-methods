<template>
    <div>
        <form>
            <div class="form-group">
                <label for="department">Requesting department:</label>
                <div>
                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="prod" name="preferences">
                        <label class="form-check-label" for="prod">Production</label>
                    </div>
                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="financial" name="preferences">
                        <label class="form-check-label" for="financial">Financial</label>
                    </div>

                </div>
            </div>
            <div class="form-group">
                <label for="projectReference">Project Reference:</label>
                <div>
                    <input type="text" class="form-control" id="projectReference" name="projectReference">
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
</template>