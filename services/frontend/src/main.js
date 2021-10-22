import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

axios.interceptors.response.use(undefined, function(error){
  if (error){
    const originalRequest = error.config;
    if(error.response.status == 401 && !originalRequest._retry){
      originalRequest._retry = true;
      store.dispatch('logOut');
      return router.push('/login')
    }
  }
})


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

const EventBus = new Vue();

new Vue({
  router,
  vuetify,
  axios,
  store,
  EventBus,
  render: h => h(App)
}).$mount('#app')
