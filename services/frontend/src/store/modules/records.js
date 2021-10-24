import axios from 'axios';

const state = {
  records: null,
  tableRecords: null,
  category:null,
  lineChartRecords:null,

   dates:null,
}

const getters = {
  stateChartRecords: state => state.records, //그래프를 위한 운동기록 저장.
  stateTableRecords: state => state.tableRecords, //테이블을 위한 운동기록 저장?
  // stateHeaders: state => state.headers,
  stateDates: state => state.dates,
  stateLineChartRecords: state => state.lineChartRecords
}

const actions = {
  
  //운동기록 저장
  async submitRecords({dispatch},data){
    console.log(data)
    await axios.post('records',data);
    await dispatch('getChartRecords'); 
    await dispatch('getTableRecords');
  },
  // 운동기록 수정
  async updateRecord({dispatch},data){
    console.log(data)
    await axios.patch(`update/${data.rid}`,data)
    await dispatch('getSpecificDateRecord', data.rdate)
    await dispatch('extractDate')
    await dispatch('getChartRecords')
  },
  //운동기록 가져오기
  async getChartRecords({commit}){
    let {data} = await axios.get('records');
    commit('setChartRecords', data);
  },
  
  //테이블 운동기록
  async getTableRecords({commit}){
    let {data} = await axios.get('tables');
    commit('setTable', data)
  },
  
  //datepicker 위한 날짜 추출
  async extractDate({commit}){
    let {data} = await axios.get('tables');
    commit('setDate',data)
  },

  //특정일자의 운동기록 추출
  async getSpecificDateRecord({dispatch,commit},date){
    let {data} = await axios.get(`tables/${date}`)
    commit('setOnedayRecord',data)
    await dispatch('extractDate')
  },
  // 운동기록 삭제
  async deleteRecord({dispatch},data){
    await axios.delete(`delete/${data.rid}`)
    await dispatch('getSpecificDateRecord', data.rdate)
    await dispatch('extractDate')
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
    
    // chart 데이터 저장하기
  //   let uniqueCategory = [...new Set(categorySet)]
  //   const lineChartData=[]
  //   for(var j=0; j<state.records.length; j++){
  //     if(uniqueCategory.includes(state.records[j]['category'])){
  //       lineChartData.push(state.records[j])
  //     }
  //   }
  //   var dates=[]
  //   var chartData=[]
  //   var chartLabel=[]
  //   var datasets=[]
  //   var backgroundColor=['#F69588', '#889FF6', '#73C470', '#E6C2EC']
  //   for(var l=0; l<lineChartData.length; l++){
  //     if(lineChartData[l]['type'] ==='rrep' && lineChartData[l]['value']!==0){
  //       dates.push(lineChartData[l]['rdate'])
  //       chartData.push(lineChartData[l]['value'])
  //       chartLabel.push(lineChartData[l]['category'])
  //     }
  //     // console.log("date: ", dates, "\n", "category: ", chartLabel, "\n", "data: ", chartData)
  //   }

  //   let date = [...new Set(dates)].sort()
  //   let category = [...new Set(chartLabel)]
  //   // let datacollection ={}
  // //dataset 넣기
  //   for(var k=0; k<category.length; k++){
  //     datasets.push({
  //       label:category[k],
  //       fill:false,
  //       borderColor:backgroundColor[k],
  //       data:chartData
  //     })
  //   }
  //   let datacollection={
  //     labels: date,
  //     datasets:datasets
  //   }
  //   state.lineChartRecords = datacollection
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
  },

  setDate(state,record){
    const datelist=[]
    for(var i=0; i < record.length;i++){
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