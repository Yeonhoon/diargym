import axios from 'axios';

const state = {
  records: null,
  tableRecords: null,
  tableRawRecords: null,
  rmidRecords: null,
  rsmallRecords: null,
  category:null,
  dashLineData:null,
  dates:null,
}

const getters = {
  stateChartRecords: state => state.records, //그래프를 위한 운동기록 저장.
  stateTableRecords: state => state.tableRecords, //테이블을 전체기록 운동기록 저장
  stateTableRawRecords: state => state.tableRawRecords,
  // stateHeaders: state => state.headers,
  stateDates: state => state.dates,
  stateLineChartRecords: state => state.dashLineData,
  stateRmidRecords: state => state.rmidRecords,
  stateRsmallRecords: state => state.rsmallRecords,
}

const actions = {
  
  //운동기록 저장
  async submitRecords({dispatch},data){
    console.log(data)
    await axios.post('records',data);
    await dispatch('getChartRecords'); //추가된 기록 가져오기(차트용)
    await dispatch('getTableRecords'); //추가된 기록 가져오기(테이블용)
  },
  // 운동기록 수정
  async updateRecord({dispatch},data){
    console.log(data)
    await axios.patch(`update/${data.rid}`,data)
    await dispatch('getSpecificDateRecord', data.rdate)
    await dispatch('getChartRecords') // 수정된 기록 가져오기
  },
  // diary: 운동기록 가져오기
  async getChartRecords({commit}){
    let {data} = await axios.get('records');
    commit('setChartRecords', data);
  },
  
  //테이블 운동기록
  async getTableRecords({commit}){
    let {data} = await axios.get('tables');
    commit('setTable', data) // 테이블 전체 기록
    commit('setSpecific',data) // 세부 데이터 저장: rmid, rsmall, rdate
  },
  
  //특정일자의 운동기록 추출
  async getSpecificDateRecord({commit},date){
    let {data} = await axios.get(`tables/${date}`)
    commit('setOnedayRecord', data)
    commit('setSpecificCategory',data)
  },

  // 운동기록 삭제
  async deleteRecord({dispatch},data){
    await axios.delete(`delete/${data.rid}`)
    await dispatch('getSpecificDateRecord', data.rdate)
    await dispatch('getChartRecords')
  },
  
}

const mutations = {
  setChartRecords(state, records){
    state.records = records;
  },
  // 날짜 click => data table에 그 날짜 데이터 + 그 날짜 차트 그리기
  setOnedayRecord(state, record){
    const tableData=[]
    const categorySet=[]

    // table 불러오기
    for(var i=0; i<record.length; i++){
      tableData.push({
        ruserid:record[i].ruserid,
        rid: record[i].rid,
        rdate: record[i].rdate,
        rlarge: record[i].rlarge,
        rmid: record[i].rmid,
        rsmall: record[i].rsmall,
        rweight: record[i].rweight,
        runit: record[i].runit,
        rrep: record[i].rrep,
      }),
      categorySet.push(record[i].rmid)
    }
    state.tableRecords = tableData
  },
  setSpecificCategory(state,record){
    //1. 필요한 카테고리 찾기
    const category = []
    for(var i=0; i<record.length; i++){
      category.push(record[i].rmid)
    }
    let categorySet = [... new Set(category)]

    //2. state에서 카테고리에 맞는 데이터 뽑아내기
    let allTableRecords = state.tableRawRecords
    const lineChartData = []
    for(var j=0; j<allTableRecords.length;j++){
      if(categorySet.includes(allTableRecords[j]['rmid'])){
        lineChartData.push(allTableRecords[j])
      }
    }
    state.dashLineData = lineChartData
    
  },
  
  setTable(state, record){
    const tableData=[]
    for(var i=0; i<record.length; i++){
      tableData.push({
        rid: record[i].rid,
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
    state.tableRawRecords = tableData
  },
  setSpecific(state, record){
    const rmidArr = []
    const rsmallArr = []
    const datelist=[]
    const rmidCounts= {}
    const rsmallCounts = {}
    for(var j=0; j<record.length; j++){
      rmidArr.push(record[j].rmid)
      rsmallArr.push(record[j].rsmall)
      datelist.push(record[j].rdate) 
    }
    const uniqueDates = [...new Set(datelist)]
    rmidArr.forEach((x)=>{rmidCounts[x] = (rmidCounts[x] || 0) + 1});
    rsmallArr.forEach((x)=>{rsmallCounts[x] = (rsmallCounts[x] || 0) + 1});
    state.dates=uniqueDates
    state.rmidRecords = rmidCounts
    state.rsmallRecords = rsmallArr 
  },

  // setDate(state,record){
  //   const datelist=[]
  //   for(var i=0; i < record.length;i++){
  //     datelist.push(record[i].rdate)
  //   }
  //   const uniqueDates = [...new Set(datelist)]
  //   state.dates=uniqueDates
  // }
};

export default{
  state,
  getters,
  actions,
  mutations,
}