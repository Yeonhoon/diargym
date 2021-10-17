import axios from 'axios';


const state = {
  records: null,
  tableRecords: null,
  headers:[
    { text:'일자',align:'center',sortable:true,value:'rdate'},
    { text: '대분류', value: 'rlarge' },
    { text: '중분류', value: 'rmid' },
    { text: '소분류', value: 'rsmall' },
    { text: '무게', value: 'rweight' },
    { text: '단위', value: 'runit' },
    { text: '반복횟수', value: 'rrep' },
   ],
   dates:null,

}

const getters = {
  stateRecords: state => state.records,
  stateTableRecords: state => state.tableRecords,
  stateHeaders: state => state.headers,
  stateDates: state => state.dates,

}

const actions = {
  
  async submitRecords({dispatch},data){
    await axios.post('records',data);
    await dispatch('getRecords')
  },

  async getRecords({commit}){
    let {data} = await axios.get('records');
    commit('setRecords', data);
  },
  async getTableRecords({commit}){
    let {data} = await axios.get('tables');
    commit('setTable', data)
  },
  async extractDate({commit}){
    let {data} = await axios.get('tables');
    commit('setDate',data)
  },
 

}

const mutations = {
  setRecords(state, records){
    state.records = records;
  },
  setTable(state, record){
    const tableData=[]
    for(var i=0; i<record.length; i++){
      tableData.push({
        rdate: record[i].rdate,
        rlarge: record[i].rlarge,
        rmid: record[i].rmid,
        rsmall: record[i].rsmall,
        rweight: record[i].rweight,
        runit: record[i].runit,
        rrep: record[i].rrep,
      })
    }
    state.tableRecords = tableData
  },

  setDate(state,record){
    const datelist=[]
    for(var i=0; i<record.length;i++){
      datelist.push(record[i].rdate)
    }
    const uniqueDates = [...new Set(datelist)]
    state.dates=uniqueDates

  }
};

export default{
  state,
  getters,
  actions,
  mutations,

}