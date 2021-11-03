<template>
  <v-row justify="center">
    <v-date-picker 
        v-model="date" 
        elevation="10"
        color="green lighten-1"
        header-color="black"
        :events=getUniqueDates
        event-color="red lighten-1"
        width=350
        
    >
    <div style="display:none;">{{changeDate}}</div>
    </v-date-picker>
    
  </v-row>
  
</template>
<script>
  // import EventBus from '../mixins/eventBus'
import { mapGetters } from 'vuex'
  export default {
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
      ...mapGetters({uniqueDates: 'stateDates'}),
      getUniqueDates(){
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
      }
    },
    
    
  }
</script>
