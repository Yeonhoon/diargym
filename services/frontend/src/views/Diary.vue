<template>
    <v-container>
        <v-layout column>
            <v-flex mt-10>
                <DiaryChart>

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
    }
}
</script>