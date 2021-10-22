<script>
import {Line, mixins} from 'vue-chartjs'

export default {
    name: 'LineChart',
    extends: Line,
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