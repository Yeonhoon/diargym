<template>
  <div class='diary-chart'>
    <bar-chart
      :chartData=this.datacollection
      :chartOptions=this.options
    >
    </bar-chart>
  </div>
</template>
<script>
import axios from 'axios'
import BarChart from "../BarChart.vue"
// import moment from 'moment'
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
        backgroundColor:['#F69588', '#889FF6', '#73C470', '#E6C2EC']
        
    }),
    async mounted(){
       await axios.get('/getrecords')
       .then(response => {
            this.rawData = response.data

           for(var i=0; i<this.rawData.length; i++){
               this.dates.push(this.rawData[i]['rdate'])
               this.chartData.push(this.rawData[i]['volume'])
               this.chartLabel.push(this.rawData[i]['category'])
           }

           let date = [...new Set(this.dates)]
           let category = [...new Set(this.chartLabel)]

          //dataset 넣기
          for(var j=0; j<category.length; j++){
            this.datasets.push({
              label:category[j],
              backgroundColor:this.backgroundColor[j],
              data:this.chartData.slice(date.length * j, date.length * (j+1) )
            })
          }
          console.log(this.datasets)
          


           this.datacollection={
              labels: date,
              datasets:this.datasets
                //TODO: dataset에 dictionary 타입으로 데이터 인풋하기.
                
            },
            this.options={
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
                  display:false
                }
            }
       })
       
    },
    computed:{
        dataExtract(){
            return this.rawData
        }
    },


  };

</script>