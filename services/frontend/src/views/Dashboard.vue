t<template>
  <v-container>
    <v-layout>
      <v-flex>
        <dash-bar
          :data =getTableData
        ></dash-bar>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex class="mt-10">
        <Calendar
          @date=getDateData 
        >
        </Calendar>
      </v-flex>
      <v-flex mt-8>
        <data-table
          @allData=getTableRecords
        >

        </data-table>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex class="pa-5">
        <v-card height="500px">
          <dash-line></dash-line>
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
      DataTable, Calendar, 
      PieChart,
      DashLine,
      DashBar
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
      //  this.$store.dispatch('extractDate')
    },

    computed:{
      ...mapGetters(['stateTableRecords']),
      getTableData(){
        return this.stateTableRecords
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