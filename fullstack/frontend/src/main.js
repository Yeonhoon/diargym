import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://127.0.0.1:8000'

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
