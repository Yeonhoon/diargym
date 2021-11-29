<template>
  <div>
    <line-chart
      :chartData=ChartRecords
      :chartOptions=this.options
      :width="300"
      :height="300"
    >
    </line-chart>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import LineChart from '../charts/LineChart.vue'
export default {
    components:{
      LineChart
    },
    data:()=>({
      datacollection:null,
      options:{
        tooltips:{
        enabled:true,
        callbacks: {
        title: (tooltipItem, data) => data['datasets'][0]['data'][tooltipItem['index']],
        label: (tooltipItem, data) => {
            console.log(data.datasets[tooltipItem.datasetIndex].label || '')
            // var x= tooltipItem.index
            return data.datasets[tooltipItem.datasetIndex].label+ ": "+ Math.round(tooltipItem.yLabel,1).toLocaleString() + 'kg'
        }
        }
      },
        // maintainAspectRatio:true
      },
    }),

    computed:{
      ...mapGetters(['stateLineChartRecords']),
      ChartRecords(){
        return this.stateLineChartRecords
      },
    },
    methods:{
    },
    

}
</script>