<template>
  <div class='diary-chart'>
    <h1>최근 일주일 운동기록</h1>
    <p>단위:볼륨(중량 * 반복 수)</p>
    <bar-chart
      :chartData=this.datacollection
      :chartOptions=this.options
    >
    </bar-chart>
  </div>
</template>
<script>
import BarChart from "../BarChart.vue"
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
        backgroundColor:['#F69588', '#889FF6', '#73C470', '#E6C2EC']
        
    }),
    async created() {
      return await this.$store.dispatch('getRecords');
    },

    computed:{
      ...mapGetters({records:'stateRecords'}),
      checkRecords(){
        return this.records
      }
    },

    async mounted(){
      for(var i=0; i<this.records.length; i++){
          this.dates.push(this.records[i]['rdate'])
          this.chartData.push(this.records[i]['volume'])
          this.chartLabel.push(this.records[i]['category'])
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

      this.datacollection={
        labels: date,
        datasets:this.datasets
          
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
            display:true
          }
      }

       
    },


  };

</script>