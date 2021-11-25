import axios from 'axios';

const state = {
  records: null,
  tableRecords: null,
  tableRawRecords: null,
  rmidRecords: null,
  rsmallRecords: null,
  category: null,
  dashLineData: null,
  dates: null,
  workoutlist: null,
  workoutWholeList: null,
  dateNcat: null,
}

const getters = {
  stateWorkoutList: state => state.workoutlist,
  stateWorkoutWholeList: state => state.workoutWholeList,
  stateRecords: state => state.records,
  stateChartRecords: state => state.records, //그래프를 위한 운동기록 저장.
  stateTableRecords: state => state.tableRecords, //테이블을 전체기록 운동기록 저장
  stateTableRawRecords: state => state.tableRawRecords,
  // stateHeaders: state => state.headers,
  stateDates: state => state.dates,
  stateLineChartRecords: state => state.dashLineData,
  stateRmidRecords: state => state.rmidRecords,
  stateRsmallRecords: state => state.rsmallRecords,
  stateDateNcat : state => state.dateNcat, // calendar에서 운동한 날짜에 종목별로 색상 적용
}

const actions = {
  
  // 운동종목 불러오기
  async loadWorkoutList({commit}){
    const {data} = await axios.get('/workoutlist')
    await commit('setWorkoutList',data)
  },
  //운동기록 저장
  async submitRecords({dispatch},data){
    await axios.post('records',data);
    await dispatch('getRecords') //운동 세트기록 가져오기
    // await dispatch('getChartRecords'); //추가된 기록 가져오기(차트용)
    await dispatch('getTableRecords'); //추가된 기록 가져오기(테이블용)
  },
  // 운동기록 수정
  async updateRecord({dispatch},data){
    await axios.patch(`update/${data.rid}`,data)
    await dispatch('getSpecificDateRecord', data.rdate)
    await dispatch('getChartRecords') // 수정된 기록 가져오기
  },
  // 이전 운동 세트기록 가져오기
  async getRecords({commit}){
    let {data}= await axios.get('records')
    commit('setRecords',data)
  },
  // diary: 차트에 그릴 운동기록 가져오기
  // async getChartRecords({commit}){
  //   let {data} = await axios.get('records');
  //   commit('setChartRecords', data);
  // },
  
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
  setWorkoutList(state, payload){
    var list ={}
    var allList=[]
    for (var i = 0; i < payload.length; i++) {
      var datum = payload[i];
      if (!list[datum.wcategory]) {
        list[datum.wcategory] = [];
      }
      list[datum.wcategory].push(datum.wname);
      allList.push(payload[i].wname)
  }
    state.workoutWholeList = allList;
    state.workoutlist = list;
    
  },
  
  setRecords(state,payload){
    state.records = payload
  },

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
        wcategory: record[i].wcategory,
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
      category.push(record[i].wcategory)
    }
    let categorySet = [... new Set(category)]
    //2. state에서 카테고리에 맞는 데이터 뽑아내기
    let allTableRecords = state.tableRawRecords
    const lineChartData = []
    for(var j=0; j<allTableRecords.length;j++){
      if(categorySet.includes(allTableRecords[j]['wcategory'])){
        lineChartData.push(allTableRecords[j])
      }
    }
    state.dashLineData = lineChartData
  },
  
  // 테이블 데이터 저장하기
  setTable(state, record){
    const tableData=[]
    for(var i=0; i<record.length; i++){
      tableData.push({
        rid: record[i].rid,
        rdate: record[i].rdate,
        wcategory: record[i].wcategory,
        rsmall: record[i].rsmall,
        rweight: record[i].rweight,
        runit: record[i].runit,
        rrep: record[i].rrep,
      })
    }
    console.log(tableData)
    state.tableRecords = tableData
    state.tableRawRecords = tableData
  },

  // 세부 데이터 저장하기
  setSpecific(state, record){
    const wcatArr = []
    const rsmallArr = []
    const datelist=[]
    const rmidCounts= {}
    const rsmallCounts = {}
    for(var j=0; j<record.length; j++){
      wcatArr.push(record[j].wcategory)
      rsmallArr.push(record[j].rsmall)
      datelist.push(record[j].rdate) 
    }
    // 날짜별 종목 array 만들기
    var dates = "rdate"
    var names = "wcategory"
    var result = record.reduce((map,obj)=>{
      if (!map[obj[dates]]) map[obj[dates]]= [];
      [].concat(obj[names]).forEach(x=>{
        let pos = map[obj[dates]].indexOf(x)
        pos === -1 ? map[obj[dates]].push(x) : map[obj[dates]].slice(x,1)
      });
        return map
    },{})
    // console.log(result)
    // console.log(Object.keys(result))
    state.dateNcat = result

    const uniqueDates = [...new Set(datelist)]
    wcatArr.forEach((x)=>{rmidCounts[x] = (rmidCounts[x] || 0) + 1});
    rsmallArr.forEach((x)=>{rsmallCounts[x] = (rsmallCounts[x] || 0) + 1});
    state.dates=uniqueDates
    state.rmidRecords = rmidCounts
    state.rsmallRecords = rsmallArr 
  },
};

export default{
  state,
  getters,
  actions,
  mutations,
}