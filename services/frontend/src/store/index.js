import Vue from 'vue'
import Vuex from 'vuex'
import users from './modules/users'
import posts from './modules/posts'
import records from './modules/records'
import createPersistedState from "vuex-persistedstate";
Vue.use(Vuex)

export default new Vuex.Store({
  modules:{
    users,
    posts,
    records,
  },
  plugins: [createPersistedState({
    kye:'keyname',
    path:['user'],
    storage: window.localStorage
  })]
})
