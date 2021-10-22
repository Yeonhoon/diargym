import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Signup from '../views/Signup.vue'
import Signin from '../views/Signin.vue'
import Diary from '../views/Diary.vue'
import Profile from '../views/Profile.vue'
// import Dashboard from '../views/Dashboard.vue'
import state from '../store/index'
Vue.use(VueRouter)

// const requireAuth=() => (to,from,next)=>{
//   if(state.getters.isAuthenticated){
//     return next()
//   }
//   else next('/login')
// }

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: "/register",
    name: 'Signup',
    component: Signup,
  },
  {
    path: "/login",
    name: 'Signin',
    component: Signin,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },

  {
    path:'/diary',
    name: 'Diary',
    component: Diary,
    meta:{requiresAuth: true}
  },
  {
    path:'/dashboard',
    name:'Dashboard',
    component: () => import(/* webpackChunkName: "about" */ '../views/Dashboard.vue'),
    meta:{requiresAuth: true}

  },
  {
    path:'/profile',
    name: 'Profile',
    component:Profile,
    meta:{requiresAuth: true}
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


router.beforeEach((to,from,next)=>{
  if (to.matched.some(record => record.meta.requireAuth)){
    if(state.getters.isAuthenticated){
      next();
      return
    }
    next('/login');
  } else {
    next();
  }
})


export default router
