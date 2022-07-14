import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MyAccount from '../views/Account/dashboard/MyAccount.vue'
import Portfolio from '../views/Account/Portfolio.vue'
import Market from '../views/Account/Market/Market.vue'
import OrderHistory from '../views/Account/Order/OrderHistory.vue'
import SingleOrder from '../views/Account/Market/SingleOrder.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path:'/signup',
      name:'signup',
      component:SignUp

    },
    {
      path:'/login',
      name:'login',
      component:LogIn
    },
    {
      path:'/my-account',
      name:'my-account',
      component:MyAccount
    },
    {
      path:'/market',
      name:'market',
      component:Market
    },
    {
      path:'/portfolio',
      name:'portfolio',
      component:Portfolio
    },
    {
      path:'/order-history',
      name:'order-history',
      component:OrderHistory
    },
    {
      path:'/order',
      name:'order',
      component:SingleOrder,
      props:true
    }
  ]
})

export default router
