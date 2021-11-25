<script>
import {Line} from 'vue-chartjs'

export default {
  name: 'LineChart',
  extends: Line,
  // mixins: [mixins.reactiveProp], 
  //chartData가 변경되었을 때 다시 갱신.
  props: {
    chartData: {
      type: Array,
      default: null
    },
    chartOptions:{
      type: Object,
      default:null
    }
  },
  data: ()=>({
    dates:[],
    chartDatasets:[],
    chartLabel:[],
    datasets:[],
    borderColor:['#F69588', '#889FF6', '#73C470', '#E6C2EC']
  }),
  mounted(){
    this.renderLineChart();
  },
  computed:{
    dataOfChart(){
      return this.chartData;
    }
  },
  methods:{
    renderLineChart(){
      // console.log(this.dataOfChart)
      for(var i=0; i<this.dataOfChart.length; i++){
        this.dates.push(this.dataOfChart[i]['rdate'])
        this.chartDatasets.push(this.dataOfChart[i]['rrep'])
        this.chartLabel.push(this.dataOfChart[i]['wcategory'])
      }
      let date = [...new Set(this.dates)].sort()
      let rmidCat = [...new Set(this.chartLabel)]

      var outerDict=[]
      var innerDict={}
      var count = 0
      for(var y=0; y<rmidCat.length;y++){
        for(var x of date){
          for(var z=0; z<this.dataOfChart.length; z++){
            if(this.dataOfChart[z].rmid === rmidCat[y] && this.dataOfChart[z].rdate===x){
              count += this.dataOfChart[z].rrep
            }
          }
          innerDict[x]=count
          count = 0
        } 
        outerDict.push(innerDict)
        this.datasets.push({
          label:rmidCat[y],
          borderColor: this.borderColor[y],
          fill:false,
          data:Object.values(outerDict[y])
        })
        innerDict={}
      }

      var datacollection = {
        datasets:this.datasets,
        labels:date
      }
      this.renderChart(datacollection, this.chartOptions)
      this.datasets = []
      this.dates=[]
      this.chartDatasets=[]
      this.chartLabel=[]
      outerDict=[]
    }
  },

  watch: {
    chartData(){
      this.$data._chart.destroy();
      this.renderLineChart();
    },
    // chartOptions(){
    //   // 옵션은 반응형 지원 x ==> 변경 시 재렌더링.
    //   this.renderChart(this.data, this.chartOptions)
    // }
  }
}
</script>