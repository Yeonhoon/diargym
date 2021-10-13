<template>
    <v-container>
        <v-layout column>
            <v-flex mt-10>
                <DiaryChart
                    :chartData="this.chartData"
                >

                </DiaryChart>
            </v-flex>
            <v-flex mt-10 pa-12>
                <v-col cols="12" sm="12">
                        <DiaryInput>

                        </DiaryInput>
                </v-col>
            </v-flex>

        </v-layout>
    </v-container>
</template>
<script>
import DiaryInput from '../components/diary/DiaryInput.vue'
import DiaryChart from '../components/BarChart.vue'
import axios from 'axios'
// import DiaryCalendar from '../components/diary/DiaryCalendar.vue'
export default {
    data: () => ({
        rawData:'',
        chartData:[],
        chartLabel:[],
        datasetsData:[],
        datasetsLabel:[],
        labels : [],
        
    }),
    components:{
        DiaryInput, DiaryChart
    },
    async mounted(){
       await axios.get('/getrecords')
       .then(response => {
           for(var i=0; i<response.data.length; i++){
               this.labels.push(response.data[i]['rdate'])
               this.datasetsLabel.push(response.data[i]['rmid']),
               this.datasetsData.push(response.data[i]['rweight']*response.data[i]['rrep'])
            }
            this.chartData.push({
                data:this.datasetsData,
                labels:this.labels,
                label:this.datasetsLabel,
                ackgroundColor: '#f87979',
                pointBackgroundColor: 'white',
                borderWidth: 1,
                pointBorderColor: '#249EBF',
            })

           console.log(this.labels)
           console.log(this.chartData)
           this.rawData = response.data //[0]['rdate']
           console.log("부모: ", this.rawData)
       })
       
    },
    computed:{
        dataExtract(){
            return this.rawData
        }
    },
    // async mounted(){
    //     await console.log(this.rawData)
    // }
    // mounted(){
    //     for(var i=0; i<this.rawData.data.length;i++){
    //            console.log(i)
    //            this.chartData.append({key:'Date', value:this.rawData.data[i]['rdate']})
    //        }
    // }
}
</script>