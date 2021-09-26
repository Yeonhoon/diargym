import Vue from 'vue'
import './plugins/axios'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import store from './store'
Vue.config.productionTip = false

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://127.0.0.1:8000'
new Vue({
  router,
  vuetify,
  axios,
  store,
  render: h => h(App)
}).$mount('#app')
