import Vue from 'vue';
import VueRouter from 'vue-router';
import LoginView from '../views/LoginView.vue';
import FinanceView from '../views/FinanceView.vue';
import ProductView from '../views/ProductView.vue';
import ServiceView from '../views/ServiceView.vue';
import CustomerView from '../views/CustomerView.vue';
import AdminManagerView from '../views/AdminManagerView.vue';
import HRView from '../views/HRView.vue';
import ChefView from '../views/ChefView.vue';
import PhotographyView from '../views/PhotographyView.vue';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'LoginView',
        component: LoginView
    },
    {
        path: '/finance',
        name: 'FinanceView',
        component: FinanceView
    },
    {
        path: '/product',
        name: 'ProductView',
        component: ProductView
    },
    {
        path: '/service',
        name: 'ServiceView',
        component: ServiceView
    },
    {
        path: '/customer',
        name: 'CustomerView',
        component: CustomerView
    },
    {
        path: '/administration',
        name: 'AdminManagerView',
        component: AdminManagerView
    },
    {
        path: '/human-resources',
        name: 'HRView',
        component: HRView
    },
    {
        path: '/chef',
        name: 'ChefView',
        component: ChefView
    },
    {
        path: '/photography',
        name: 'PhotographyView',
        component: PhotographyView
    }
];

const router = new VueRouter({
    mode: 'history',
    routes
});

export default router;