<template>
  <div>
    <bar-chart
      :chartData=this.datacollection
      :chartOptions=this.options
    >
    </bar-chart>
  </div>
</template>
<script>
import BarChart from "../charts/BarChart.vue"
import {mapGetters} from 'vuex'
  export default {
    name: 'DiaryBarChart',
    components: {BarChart},
   data: () => ({
      datacollection:null,
      options:null,
      rawData:[],
      chartData:[],
      chartLabel:[],
      dates : [],
      datasets:[], 
      backgroundColor:['#F69588', '#889FF6', '#73C470', '#E6C2EC','#C2ECE9','#747171']
    }),

    methods:{
      getCharts(){
        return this.$store.dispatch('getChartRecords')
      }
    },

    computed:{
      ...mapGetters({records:'stateChartRecords'}),
      checkRecords(){
        return this.records
      }
    },

    async mounted(){
      for(var i=0; i<this.records.length; i++){
        if(this.records[i]['type'] ==='volume'){
          this.dates.push(this.records[i]['rdate'])
          this.chartData.push(this.records[i]['value'])
          this.chartLabel.push(this.records[i]['category'])
        }
      }

      let date = [...new Set(this.dates)].sort()
      let category = [...new Set(this.chartLabel)]
    //dataset 넣기
      for(var j=0; j<category.length; j++){
        this.datasets.push({
          label:category[j],
          backgroundColor:this.backgroundColor[j],
          data:this.chartData.slice(date.length * j, date.length * (j+1) )
        })
      } 

      this.datacollection={
        labels: date, // 최근 7일 데이터만 보여주기
        datasets:this.datasets
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
                userCallback: (value)=>{
                  value = value.toString();
                  value=value.split(/(?=(?:...)*$)/);
                  value = value.join(',');
                  return value
                },
              }
            }]
          },
          tooltips:{
            enabled:true,
            callbacks: {
              title: (tooltipItem, data) => data['datasets'][0]['data'][tooltipItem['index']],
              // label: (tooltipItem, data) => data['datasets'][0]['data'][tooltipItem['index']]
            }
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

       
    },


  };

</script>