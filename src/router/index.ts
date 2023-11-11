import {createRouter, createWebHistory} from 'vue-router';
import HomeView from '../views/HomeView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/stocks',
      name: 'stocks',
      component: () => import('../views/StocksView.vue'),
    },
    {
      path: '/brokers',
      name: 'brokers',
      component: () => import('../views/BrokersView.vue'),
    },
    // {
    //   path: '/brokers/:id',
    //   name: 'broker',
    //   component: () => import('../views/BrokerView.vue'),
    // },
  ],
});

export default router;
