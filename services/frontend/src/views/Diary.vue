<template>
    <v-container>
        <v-layout column>
            <v-flex mt-8>
                
                <DiaryChart
                >

                </DiaryChart>
            </v-flex>
            <v-flex pa-5>
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
    async created(){
        this.getchart()
    },
    methods:{
        getchart(){
            this.$store.dispatch("getChartRecords")
        }
    }
    
}
</script>