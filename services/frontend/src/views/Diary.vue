<template>
    <v-container>
        <v-layout column>
            <v-flex mt-10>
                <h1>최근 일주일 운동기록</h1>
                <h5>단위:볼륨(중량 * 반복 수)</h5>
                <DiaryChart
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
import DiaryChart from '../components/diary/DiaryChart.vue'
// import DiaryCalendar from '../components/diary/DiaryCalendar.vue'
export default {
    components:{
        DiaryInput, DiaryChart
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