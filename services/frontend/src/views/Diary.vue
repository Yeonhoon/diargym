<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-card height="300" elevation="5">
          <diary-input>

          </diary-input>

        </v-card>
        <v-card class="mt-10 mb-10">
          <diary-chart
          >

          </diary-chart>
        </v-card>

      </v-flex>
    </v-layout>

  </v-container>
</template>
<script>
import DiaryInput from '../components/diary/DiaryInput.vue'
import DiaryChart from '../components/diary/DiaryChart.vue'
// import DiaryCalendar from '../components/diary/DiaryCalendar.vue'
export default {
  name:"Diary",
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