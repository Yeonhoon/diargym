<template>
  <v-card>
    <v-card-title>
      운동기록
      <v-btn text
        color="primary"
        @click="getAllData"
        
      >전체 기록 보기</v-btn>
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers=getHeaders
      :items=tableDatak
      :search="search"
      loading=true
      loading-text="운동기록이 존재하지 않습니다."
    ></v-data-table>
  </v-card>
</template>
<script>
  // import EventBus from '../../mixins/eventBus'
  import { mapGetters } from 'vuex'
  export default {
    props:{
      tableData:{
        type: Array,
        default: null,
      }
    },
    data: ()=>({
      search:'',
    }),

    methods:{
      async getList(){
        return this.tableData
      },
      getAllData(){
        this.$emit('allData','allData')
      }

    },
    mounted(){
      this.getList();
      
    },
    computed:{
      ...mapGetters({headers: 'stateHeaders'}),
      getHeaders(){
        return this.headers
      },
      // getData(){
      //   return this.tableData
      // }



    },
   
    // created(){
    //   EventBus.$on('date', (ebs) =>{
    //     console.log(ebs)
    //   })
    // },
    // computed:{
    // }

  }
</script>