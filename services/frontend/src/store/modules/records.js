import axios from 'axios';


const state = {
  diary: null,
  record: null
}

const getters = {
  stateDiary: state => state.diary,
  stateRecord: state => state.record

}


const actions = {
  async addDiary(form){
    
    await axios.post('/adddiary', form,{
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      }
    })
    .then(response => {
      console.log('response: ', JSON.stringify(response, null,2))
    })
    .catch(error => {
      console.log("failed", error)
      // await dispatch('getDiary')
    })
  },
  // async getDiary({commit}){
  //   let {data} = await axios.get('adddiary');
  //   commit('setDiary', data);
  // }

}

const mutations = {
  setDiary(state, diary){
    state.diary = diary;
  },
  setRecord(state, record){
    state.record = record
  }
};

export default{
  state,
  getters,
  actions,
  mutations,

}