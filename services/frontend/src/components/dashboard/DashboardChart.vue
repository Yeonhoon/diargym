<template>
    <line-chart
      :chartData=getChartRecords
      :chartOptions=this.options
    >

    </line-chart>
</template>
<script>
import { mapGetters } from 'vuex'
import LineChart from '../LineChart.vue'
export default {
    components:{
        LineChart
    },
    data:()=>({
        options:{
          responsive:true,
          scales:{
              xAxes:[{
                  stacked:true,
                }],
              yAxes:[{
                  stacked:true
                }]
          },
          legend:{
          display:true
          }
    }
    }),
    async created() {
      return await this.$store.dispatch('getChartRecords');
    },

    computed:{
      ...mapGetters({records:'stateLineChartRecords'}),
      getChartRecords(){
        return this.records
      }
    },
    async mounted(){
      
      
    },
}
</script>