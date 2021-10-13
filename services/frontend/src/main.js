import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import store from './store'


// import VueCookies from 'vue-cookies'
Vue.config.productionTip = false

// Vue.use(VueCookies)
// Vue.$cookies.config('7d')
axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/';

// axios.interceptors.response.use(undefined, function (error) {
//   if (error) {
//     const originalRequest = error.config;
//     if (error.response.status === 401 && !originalRequest._retry) {
//       originalRequest._retry = true;
//       store.dispatch('logOut');
//       return router.push('/login')
//     }
//   }
// });

new Vue({
  router,
  vuetify,
  axios,
  store,
  render: h => h(App)
}).$mount('#app')
