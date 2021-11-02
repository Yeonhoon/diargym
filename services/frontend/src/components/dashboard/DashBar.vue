<template>
    <div>
        <v-row>
          <v-col class="pl-10 pt-10">
              <h3>종류 선택</h3>
          <p v-for="(value) in this.checkboxList" :key=value.rmid>
            <v-radio-group
              v-model="selectedCat"
              @change="drawChart"
            >
              <v-radio 
                :label='value.rmid'
                :value='value.rmid'
              ></v-radio>
            </v-radio-group>
          </p>
          </v-col>
          <v-col class="pa-7">
            <bar-chart
              id="barChart"
              :chartData=this.datacollection
              :chartOptions=this.options
            >
            </bar-chart>
          </v-col>
        </v-row>
    </div>
</template>
<script>
import BarChart from '../charts/BarChart.vue'
import { mapGetters } from 'vuex'
export default {
  components: { BarChart },
  props:{
      data:{
          type: Array,
          default:null,
      }
  },
  data: () => ({
    checkboxList:[],
    selectedCat:null,
    datacollection:null,
    options:null,
    backgroundColor:['#F69588', '#889FF6', '#73C470', '#E6C2EC','#C2ECE9','#747171'],
    barChart:null,
    // chartData:[],
  }),

  computed:{
    ...mapGetters(['stateTableRawRecords']),
    getRecords(){
        return this.stateTableRawRecords
    },
  },

  methods:{
    drawChart(){
      const dates=[]
      const category=[]
      const volumes=[]
      const datasets=[]
      
      for(var i of this.getRecords){
          if(i.rmid === this.selectedCat){
            dates.push(i.rdate)
            category.push(i.rsmall)
            volumes.push(i.rweight * i.rrep)
          }
      }
        let labels= [...new Set(dates)].sort()
        let categorySet = [...new Set(category)]
      for(var j=0; j<categorySet.length; j++){
        datasets.push({
          label:categorySet[j],
          backgroundColor: this.backgroundColor[j],
          data: volumes.slice(labels.length*j, labels.length*(j+1))
         })
       }
        console.log(datasets)
      
      this.datacollection={
          labels: labels,
          datasets: datasets
      }
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
                userCallback: (value)=>{
                  value = value.toString();
                  value=value.split(/(?=(?:...)*$)/);
                  value = value.join(',');
                  return value
                },
              }
            }]
          },
          legend:{
            display:true
          },
          // plugins:{
          //   datalabels:{
          //     formatter: (value)=>{
          //       return value +"vol"
          //     }
          //   }
          // }

      }
    //   console.log(this.datacollection)

    }
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
