<template>
    <div>
      <v-row>
        <v-col class="pa-3">
          <bar-chart
            id="barChart"
            :chartData=this.datacollection
            :chartOptions=this.options
          >
          </bar-chart>
        </v-col>
        <v-col class="pl-10 pt-10">
          <h3>선택</h3>
        <p v-for="(value) in this.checkboxList" :key=value.rmid>
          <v-radio-group
            v-model="selectedCat"
            @change="plotDashBar"
          >
            <v-radio 
              :label='value.rmid'
              :value='value.rmid'
            ></v-radio>
          </v-radio-group>
        </p>
        </v-col>
      </v-row>
    </div>
</template>
<script>
import BarChart from '../charts/BarChart.vue'
import { mapGetters, mapActions } from 'vuex'
export default {
  components: { BarChart },
  data: () => ({
    checkboxList:[],
    selectedCat:null,
    datacollection:null,
    options:null,
    backgroundColor:['#F69588', '#889FF6', '#73C470', '#E6C2EC','#C2ECE9','#747171'],
    barChart:null,
    // chartData:[],
  }),
  props:{
    barData:{
      type: Array,
      default: null,
    }
  },

  computed:{
    ...mapGetters(['stateTableRawRecords','getDashBar']),
    getRecords(){
      return this.stateTableRawRecords
    },
    getDashBarData(){
      return this.getDashBar
    }
  },
  watch:{
    
  },

  methods:{
    ...mapActions(['importDashBar']),
    async plotDashBar(){
      await this.importDashBar(this.selectedCat)
      const dateArr = []
      const catArr = []
      const volArr = []
      const datasets = []
      for(var a of this.getDashBarData) {
        dateArr.push(a.rdate)
        catArr.push(a.rsmall)
        volArr.push(a.value)
      }
      console.log(volArr)
      let dateSet = [...new Set(dateArr)].sort()
      let catSet = [...new Set(catArr)]

      for (var b=0; b<catSet.length; b++){
        if (dateSet.length===1){
          datasets.push({
            label:catSet[b],
            backgroundColor: this.backgroundColor[b],
            data: volArr.slice(b+0,b+1)
        })
        } else {
          datasets.push({
            label:catSet[b],
            backgroundColor: this.backgroundColor[b],
            data: volArr.slice(catSet.length*b, catSet.length*(b+1))
          })
        }
      }
      console.log(datasets)
      this.datacollection={
        labels: dateSet,
        datasets: datasets
      },
       this.options={
          responsive:true,
          scales:{
            xAxes:[{
              stacked:true,
              scaleLabel:{
                display:true,
                labelString:'일자'
              }
            }],
            yAxes:[{
              stacked:true,
              scaleLabel:{
                // display:true,
                // labelString:''
              },
              ticks:{
                beginAtZero: true,
              }
            }]
          },
          tooltips:{
            enabled:true,
            callbacks: {
              title: (tooltipItem, data) => data['datasets'][0]['data'][tooltipItem['index']],
              label: (tooltipItem, data) => {
                var x= tooltipItem.index
                // console.log(data.datasets[tooltipItem.datasetIndex].label || '')
                return data.datasets[x].label+ ": "+ Math.round(tooltipItem.yLabel,1).toLocaleString() + 'kg'
              }
              
            }
          },
          legend:{
            display:true
          },
      }
    },
  },

  mounted(){
    var temp=[]
    for(var i of this.getRecords){
        temp.push(i.rmid)
    }
    var temp2 =  [...new Set(temp)]
    for(var j of temp2){
      this.checkboxList.push({
          rmid:j
      })
    }
  }

}
</script>
