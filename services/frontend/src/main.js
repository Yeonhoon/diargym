import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import ThankyouDialog from './components/dialogs/ThankyouDialog'
// import VueCompositionAPI from '@vue/composition-api'
// import pageTitle from './mixins/pageTitle'
Vue.config.productionTip = false
// Vue.mixin(pageTitle)
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
axios.defaults.baseURL = 'http://118.67.132.200:5000';

new Vue({
  router,
  vuetify,
  axios,
  store,
  ThankyouDialog,
  render: h => h(App)
}).$mount('#app')
