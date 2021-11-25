<template>
  <v-row justify="center">
  <v-date-picker 
    v-model="date" 
    elevation="10"
    color="grey dark-2"
    header-color="black"
    :events=getUniqueDates
    event-color="red"
    width=350
    @change="dateclicked"
  >
    <div style="display:none;">{{changeDate}}</div>
  </v-date-picker>
  </v-row>
  
</template>
<script>
  // import EventBus from '../mixins/eventBus'
import { mapGetters } from 'vuex'
  export default {
  props:{
    records:{
      type: Object,
      default: null,
    }
  },
  data () {
    return {
    date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
    datelist: [],
    // uniqueDates:[],
    isDateChanged:false,
    date2:null,
    }
  },
  computed:{
    //운동한 일자 가져오기
    ...mapGetters({uniqueDates: 'stateDates'},{uniqueDatesCat:'stateDateNcat'} ),
    getUniqueDates(){
    //   console.log(this.uniqueDates)
      return this.uniqueDates
    },
    
    //변경된 날짜 내보내기
    changeDate(){
      this.$emit('date',this.date)
      return this.date
    }
  },
  watch:{
    dateChanged(){
      this.date2=this.date
    },
  },
  methods: {
    dateclicked(val){
      var allDates = document.querySelectorAll(".v-date-picker-table .v-btn .v-btn__content");
      var workoutDates = Object.keys(this.records).map(x => parseInt(x.split('-')[2]));
      allDates.forEach((x)=>{
        if (workoutDates.includes(parseInt(val.split('-')[2])) && 
            // this.records[val][0] === '가슴' &&
            parseInt(val.split('-')[2]) == x.innerHTML){
            x.parentNode.style= "background-color: red !important";
        } else {
          x.parentNode.style=""
        }
      })
    },
    setDateColor(){
      var allDates = document.querySelectorAll(".v-date-picker-table .v-btn .v-btn__content");
      var workoutDates = Object.keys(this.records).map(x => parseInt(x.split('-')[2]));
      allDates.forEach((x,i)=>{
        if (workoutDates.includes(parseInt(x.innerHTML))){
          allDates[i].classList.add('date-color');
        }
      })
    },
    // workoutEvents(date) {
    //   if (this.records[date][0] === "가슴") return true
    //   if (this.records[date][0] === '등') return ['red','blue']
    //   return false
    //   const [,, day] = date.split('-')
    //   if (Object.keys(this.records).includes(parseInt(day, 10))) return true
    //   return false
    // }
  },
  mounted(){
    this.setDateColor();
  }
}
</script>
<style>
  .date-color {
    color: #ff0000;
    /* color: rgba(22, 51, 218, 0.842); */
    font-weight:1000;
  }
  .v-btn--active .date-color {
  color: #fff;
  }
</style>