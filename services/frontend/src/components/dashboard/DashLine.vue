<template>
  <div>
    <h3 class="text-center">부위별 반복 수</h3>
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