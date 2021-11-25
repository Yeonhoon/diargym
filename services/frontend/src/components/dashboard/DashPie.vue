<template>
  <div>
    <h3 class="text-center">부위별 세트 수</h3>
    <pie-chart
      :chartData=this.dataCollections
      :chartOptions=this.options
      :width="300"
      :height="300"
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
      options:{
        tooltips:{
          enabled:true,
          callbacks: {
            title: (tooltipItem, data) => data['datasets'][0]['data'][tooltipItem['index']],
            label: (tooltipItem, data) => {
              console.log(data.datasets[tooltipItem.datasetIndex].label || '')
              // var x= tooltipItem.index
              return data.datasets[tooltipItem.datasetIndex].label+ ": "+ Math.round(tooltipItem.yLabel,1).toLocaleString() + '회'
            }
          }
        },
      },
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