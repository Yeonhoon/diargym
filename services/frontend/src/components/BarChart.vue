<script>
// import axios from 'axios'
import {Bar, mixins} from 'vue-chartjs'
// import {locale} from 'moment'

export default {
    name: 'Barchart',
    extends: Bar,
    mixins: [mixins.reactiveProp], //chartData가 변경되었을 때 다시 갱신.
    props: {
        chartData: {
            type: Array,
            default: null
        },
    },
    computed:{
        GetData(){
            console.log(this.chartData)
            return this.chartData
        }
    },
    mounted(){
        // console.log("Chart Data: ",this.chartData)
        // console.log(this.chartData.label)
        this.renderChart({
            labels:['10-10','10-11','10-12'],
            datasets:[
                {
                    label:['등'],
                    data:['200','300','500'],
                    backgroundColor: '#f87979',
                },
                {
                    label:['가슴'],
                    data:['300','500','600'],
                    backgroundColor: '#3D5B96',
                }
                
                ]
            },
            {
                responsive:true,
                scales:{
                    xAxes:[{
                        stacked:true,
                    }],
                    yAxes:[{
                        stacked:true
                    }]
                }
            }
            )
            // labels: this.chartData[0].labels,
            // datasets:[
            //     {
            //         label:this.chartData[0].label,
            //         backgroundColor: this.chartData[0].backgroundColor,
            //         data: this.chartData[0].data
            //     }
            // ]
    }
   

    // watch: {
    //     chartOptions(){
    //         // 옵션은 반응형 지원 x ==> 변경 시 재렌더링.
    //         this.renderChart(this.chartData, this.chartOptions)
    //     }
    // }

}
</script>