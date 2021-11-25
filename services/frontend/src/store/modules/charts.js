import axios from 'axios'
const state = {
  dashBar: null,
}

const getters ={
  getDashBar: state => state.dashBar
}

const actions = {
  async importDashBar({ commit },category){
    let {data} = await axios.get("dashbar/"+category)
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