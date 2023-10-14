<template>
    <div>
        <HeaderComponent />
        <div class="container mt-5">
            <button @click="showForm = true" v-if="!showForm" class="btn btn-primary mb-3">Create Financial Request</button>
            <form v-if="showForm">
                <FinancialRequestComponent />
            </form>
        </div>
    </div>
</template>

<script>
import HeaderComponent from '../components/HeaderComponent.vue';
import FinancialRequestComponent from '../components/FinancialRequestComponent.vue';
export default {
    name: "ProductView",
    data() {
        return {
            showForm: false,
        };
    },
    components: {
        HeaderComponent,
        FinancialRequestComponent
    }
}
</script>
<style></style>