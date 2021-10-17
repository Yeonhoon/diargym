<template>
    <v-row justify="center">
            <v-date-picker 
                v-model="date" 
                elevation="10"
                color="green lighten-1"
                header-color="primary"
                :events=getUniqueDates
                event-color="red lighten-1"
                width=500
                ref="date"
            >
            </v-date-picker>
            <!-- <div>{{changeDate}}</div> -->
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
        isDateChanged:false

      }
    },

    computed:{
      ...mapGetters({uniqueDates: 'stateDates'}),
      getUniqueDates(){
        return this.uniqueDates
      },
      changeDate(){
        this.$emit('date',this.date)
        console.log(this.date)
        return this.date
      }
    },
    
    
  }
</script>
