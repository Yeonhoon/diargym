import axios from 'axios'
const state = {
  dashBar: null,
}

const getters ={
  getDashBar: state => state.dashBar
}

const actions = {
  async importDashBar({ commit },rmid){
    let {data} = await axios.get("dashbar/"+rmid)
    commit('setDashBar',data)
  }
}

const mutations = {
  setDashBar(state, data){
    state.dashBar = data;
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}