<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-card elevation="0" color="#f7f7f7">
          <v-card-title class='d-flex justify-center'>
            <h3 class='mt-2'>운동일지 작성</h3>
          </v-card-title>
          <v-divider class="mx-4"></v-divider>
          <v-card-text >
            <diary-input class='d-flex justify-center'>
            </diary-input>
          </v-card-text>
        </v-card>
        <v-card height="550" class="mt-10 mb-10">
          <v-card-title class='d-flex justify-center'>
             <h3 class="mt-3">일별 운동기록</h3>
          </v-card-title>
          <v-card-subtitle class='d-flex justify-center pt-2'>
            <blockquote>단위:볼륨(중량 * 반복 수)</blockquote>
          </v-card-subtitle>
          <v-divider class="mx-4"></v-divider>
          <v-card-text>
            <!-- <diary-chart></diary-chart> -->
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import DiaryInput from '../components/diary/DiaryInput.vue'
// import DiaryChart from '../components/diary/DiaryChart.vue'
// import DiaryCalendar from '../components/diary/DiaryCalendar.vue'
export default {
  name:"Diary",
  components:{
    DiaryInput,
    // DiaryChart
  },
  async created(){
    this.getchart()
    this.loadWorkout()
  },
  methods:{
    getchart(){
      this.$store.dispatch("getChartRecords")
    },
    loadWorkout(){
      this.$store.dispatch("loadWorkoutList")
    }
  }
  
}
</script>