t<template>
  <v-container>
    <v-layout column>
        <v-flex class="d-justify-center mt-10">
          <Calendar
            @date="getDateData"
          >

          </Calendar>
        </v-flex>
        <v-flex mt-8>
            <DataTable
              :tableData=this.tableData
              @allData=getData
            >
              <!-- :header=this.header
              :data=this.data -->

            </DataTable>
        </v-flex>
    </v-layout>
  </v-container>
</template>
<script>

import DataTable from '../components/dashboard/DataTable.vue'
import Calendar from '../components/Calendar.vue'
import axios from 'axios'
import { mapGetters } from 'vuex'
  export default {
    components:{
      DataTable,Calendar
    }, 
    data: () => ({
      search:'',
      tableData: [],
      rawData:null,
    }),

    // dispatch로 데이터 state에 저장하기
    async created() {
      return await this.$store.dispatch('getTableRecords'), this.$store.dispatch('extractDate');
    },

    computed:{
      ...mapGetters({tableRecord: 'stateTableRecords'}),
      getTableData(){
        return this.tableRecord
      }

    },
 
    methods:{
      // ...mapActions(['getTableRecords']),
      
      async getData(){
        console.log('전체 데이터 가져오기')
        await axios.get('/tables')
        .then(res=>{
          this.rawData = res.data
          this.tableData=[]
          for(var i=0; i<this.rawData.length; i++){
            this.tableData.push({
              rdate: this.rawData[i].rdate,
              rlarge: this.rawData[i].rlarge,
              rmid: this.rawData[i].rmid,
              rsmall: this.rawData[i].rsmall,
              rweight: this.rawData[i].rweight,
              runit: this.rawData[i].runit,
              rrep: this.rawData[i].rrep,
            })
          }
        })
        .catch(err => {
          console.log("error: ", err)
        })
      },
      async getDateData(date){
        console.log('특정일자 데이터 가져오기')
        await axios.get('/tables/' + date)
        .then(res => {
          this.rawData = res.data
          this.tableData=[]
          for(var i=0; i<this.rawData.length; i++){
            this.tableData.push({
              rdate: this.rawData[i].rdate,
              rlarge: this.rawData[i].rlarge,
              rmid: this.rawData[i].rmid,
              rsmall: this.rawData[i].rsmall,
              rweight: this.rawData[i].rweight,
              runit: this.rawData[i].runit,
              rrep: this.rawData[i].rrep,
            })
          }
        })
        .catch(err => {
          console.log(err)
        })
      },

    },

    

  }
</script>