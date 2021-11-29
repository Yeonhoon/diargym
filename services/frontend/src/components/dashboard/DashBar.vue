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
        <v-col class="pl-10">
          <h3>선택</h3>
          <!-- <v-list v-for="(value) in this.checkboxList" :key=value.category>
            <v-list-item 
              v-text="value.category">
            </v-list-item>
          </v-list> -->
        <!-- <div v-for="(value) in this.checkboxList" :key=value.category> -->
          <v-radio-group
            v-model="selectedCat"
            @change="plotDashBar"
            row
          >
            <v-radio
              v-for="(value) in this.checkboxList" :key=value.category
              :label='value.category'
              :value='value.category'
            ></v-radio>
          </v-radio-group>
        <!-- </div> -->
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
    backgroundColor:['#F69588', '#889FF6', '#73C470', '#E6C2EC','#C2ECE9','#747171', '#a2e3eb','#e5eba2'],
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
        dateArr.push(new Date(a.rdate).toLocaleDateString('ko-KR',{month:'long',day:'numeric'}))
        catArr.push(a.rsmall)
        volArr.push(a.value)
      }
      let dateSet = [...new Set(dateArr)].sort()
      let catSet = [...new Set(catArr)]
    //   console.log(this.getDashBarData)
    //   console.log(volArr)
    //   console.log("categry Set: ", catSet)
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
            data: volArr.slice(dateSet.length*b, dateSet.length*(b+1))
          })
        }
      }
    //   console.log("datasets: ", datasets)
      this.datacollection={
        labels: dateSet,
        datasets: datasets
      },
      this.options={
        responsive:true,
        datasets:{
          barPercentage:0.4,
        },
        scales:{
          xAxes:[{
            barPercentage:0.4,
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
              console.log(data.datasets[tooltipItem.datasetIndex].label || '')
              // var x= tooltipItem.index
              return data.datasets[tooltipItem.datasetIndex].label+ ": "+ Math.round(tooltipItem.yLabel,1).toLocaleString() + 'kg'
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
      temp.push(i.wcategory)
    }
    var temp2 =  [...new Set(temp)]
    for(var j of temp2){
      this.checkboxList.push({
        category:j
      })
    }
  }

}
</script>
