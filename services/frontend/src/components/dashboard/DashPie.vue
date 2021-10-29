<template>
  <div>
    <h3 class="text-center">부위별 세트 수</h3>
    <pie-chart
      :chartData=this.dataCollections
      :chartOptions=this.options
    >
    </pie-chart>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import PieChart from '../charts/PieChart.vue'
export default {
  components:{
      PieChart
    },
  data: () => ({
      dataCollections:null,
      options:null,
      backgroundColor:['#F69588', '#889FF6', '#73C470', '#E6C2EC','#C2ECE9','#747171']
  }),
  computed:{
      ...mapGetters(['stateRmidRecords']),
      getPieData(){
          return this.stateRmidRecords
      }
  },
  async mounted(){
    this.dataCollections={
        labels: Object.keys(this.stateRmidRecords),
        datasets:[{
          backgroundColor: this.backgroundColor,
          data: Object.values(this.stateRmidRecords)
        }]
    }
  }
}
</script>