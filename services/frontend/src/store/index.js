import Vue from 'vue'
import Vuex from 'vuex'
import users from './modules/users'
import records from './modules/records'
import charts from './modules/charts'
import createPersistedState from "vuex-persistedstate";
Vue.use(Vuex)

export default new Vuex.Store({
  modules:{
    users,
    records,
    charts
  },
  plugins: [createPersistedState({
    key:'keyname',
    path:['users'],
    storage: window.localStorage
  })]
})
