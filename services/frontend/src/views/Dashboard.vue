t<template>
  <v-container>
    <v-layout column>
        <v-flex class="d-justify-center mt-10">
          <Calendar
            @date=getDateData 
          >
          <!-- 특정일자 데이터 가져와야함. -->
          </Calendar>
        </v-flex>
        <v-flex mt-10 mr-5 ml-5>
        </v-flex>
        <v-flex mt-8>
          <!-- <dashboard-chart>

          </dashboard-chart> -->
        </v-flex>
        
        <v-flex mt-8>
          <data-table
            @allData=getData
          >
            <!-- :header=this.header
            :data=this.data -->

          </data-table>
        </v-flex>
    </v-layout>
  </v-container>
</template>
<script>

import DataTable from '../components/dashboard/DataTable.vue'
import Calendar from '../components/dashboard/Calendar.vue'
// import DashboardChart from '../components/dashboard/DashboardChart.vue'
// import axios from 'axios'
import { mapGetters } from 'vuex'
  export default {
    components:{
      DataTable, Calendar, 
    //  DashboardChart
      //Calendar2
    }, 
    data: () => ({
      search:'',
      tableData: [],
      categorySet:[],
      rawData:null,
    }),

    // dispatch로 데이터 state에 저장하기
    // async created() {
    //   return await this.$store.dispatch('getTableRecords');
    //   //  this.$store.dispatch('extractDate')
    // },

    computed:{
      ...mapGetters({tableRecord: 'stateTableRecords'}),
      getTableData(){
        return this.tableRecord
      }

    },
 
    methods:{
      // ...mapActions(['getTableRecords']),
      async getData(){
        this.$store.dispatch("getTableRecords")
        // await axios.get('/tables')
        
      },
      async getDateData(date){
        this.$store.dispatch('getSpecificDateRecord', date)
      },

    },

    

  }
</script>