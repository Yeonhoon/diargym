<script>
import {Doughnut, mixins} from 'vue-chartjs'
export default {
  name: 'PieChart',
  extends: Doughnut,
  mixins: [mixins.reactiveProp], //chartData가 변경되었을 때 다시 갱신.
  props: {
    chartData: {
      type: Object,
      default: null
    },
    chartOptions:{
      type: Object,
      default:null
    }
    },
    created(){
        },
    // computed:{
    //     GetData(){
    //         return this.chartData, this.chartOptions
    //     }
    // },
    mounted(){

      this.renderChart(this.chartData, this.chartOptions)
            

    },
    watch: {
        chartOptions(){
            // 옵션은 반응형 지원 x ==> 변경 시 재렌더링.
            this.renderChart(this.chartData, this.chartOptions)
        }
    }
}
</script>