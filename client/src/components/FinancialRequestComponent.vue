<template>
    <div>
        <form>
            <div class="form-group">
                <label for="department">Requesting department:</label>
                <div>
                    <div class="form-check">
                        <input type="radio" class="form-check-input" id="prod" name="department" value="Production">
                        <label class="form-check-label" for="prod">Production</label>
                    </div>
                    <div class="form-check">
                        <input type="radio" class="form-check-input" id="financial" name="department" value="Financial">
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
                <label for="requiredAmount">Required Amount:</label>
                <div>
                    <input type="text" class="form-control" id="requiredAmount" name="requiredAmount">
                </div>
            </div>
            <div class="form-group">
                <label for="reason">Reason:</label>
                <div>
                    <input type="text" class="form-control" id="reason" name="reason">
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