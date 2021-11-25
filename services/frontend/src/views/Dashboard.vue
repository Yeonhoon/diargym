<template>
  <v-container>
    <v-layout row>
      <v-flex class="mt-10">
        <Calendar
          @date=getDateData
          :records=getUniqueDateCategory
        >
        </Calendar>
      </v-flex>
      <v-flex mt-8 pl-5 pr-5>
        <v-card>
          <v-toolbar flat color="grey lighten-2" class='d-flex justify-center' >
            <h2>
              운동기록 테이블
            </h2>
          </v-toolbar>
          <v-card-text>
            <data-table
              title="운동"
              @allData=getTableRecords
            >
            </data-table>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex>
        <v-card class='mt-10 mb-5' elevation="5">
          <v-card-title class='mt-5 d-flex justify-center'>
            <h3>부위별 세부운동 그래프</h3>
          </v-card-title>
          <v-card-subtitle class='d-flex justify-center'>
            단위: 볼륨(중량*반복수)</v-card-subtitle>
          <v-divider class="mx-4"></v-divider>
          <v-card-text>
            <dash-bar
            ></dash-bar>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex class="pa-5">
        <v-card height="500px">
          <v-card-title class='d-flex justify-center'>
            <h3>부위별 반복수 추세</h3>
          </v-card-title>
          <v-divider class="mx-4"></v-divider>
          <v-card-text>
            <dash-line></dash-line>
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex class="pa-5">
        <v-card height="500px">
          <pie-chart></pie-chart>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>

import DataTable from '../components/dashboard/DataTable.vue'
import Calendar from '../components/dashboard/Calendar.vue'
import PieChart from '../components/dashboard/DashPie.vue'
import DashLine from '../components/dashboard/DashLine.vue'
import DashBar from '../components/dashboard/DashBar.vue'
// import axios from 'axios'
import { mapGetters } from 'vuex'
  export default {
    components:{
      DataTable, 
      Calendar, 
      PieChart,
      DashLine,
      DashBar,
    }, 
    data: () => ({
      search:'',
      tableData: [],
      categorySet:[],
      rawData:null,
    }),

    // dispatch로 데이터 state에 저장하기
    async created() {
      this.getTableRecords()
    },

    computed:{
      ...mapGetters(['stateTableRecords','stateDateNcat']),
      getTableData(){
        return this.stateTableRecords
      },
      // 운동한 일자 + 그 날 종목
      getUniqueDateCategory(){
        return this.stateDateNcat
      },
    },
 
    methods:{
      // ...mapActions(['getTableRecords']),
      async getTableRecords(){
        this.$store.dispatch("getTableRecords")
        // await axios.get('/tables')
      },

      async getDateData(date){
        this.$store.dispatch('getSpecificDateRecord', date)
      },

    },

    

  }
</script>