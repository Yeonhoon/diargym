<template>
  <v-container mt-15>
    <v-layout col wrap>
      <v-flex xs12 class='d-flex justify-center'>
        <h1>Welcome!</h1>
      </v-flex>
      <v-flex xs12 class="d-flex justify-center">
        <blockquote class="blockquote">
          Test Web Application by Yeonhoon <br>
          with Vue.js & FastAPI & PostgreSQL
        </blockquote>
      </v-flex>
      <v-flex sm6 offset-sm3 class="d-flex justify-center" mt-5 v-if="!isLogin">
        <v-btn :to="{name:'Signup'}" color='primary' text>Sign Up</v-btn>
        <v-btn :to="{name:'Signin'}" color='primary' text >Sign In</v-btn>
      </v-flex>
      <v-flex sm6 offset-sm3 class="d-flex justify-center" mt-5 v-else>
            <v-btn :to="{name:'Diary'}" color='primary' text>운동일지 작성</v-btn>
            <v-btn :to="{name:'Dashboard'}" color="error" text>대시보드</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import {mapActions} from 'vuex'
  export default {
    name: 'Home',
    data () {
      return {
        userData: '',
        // isLogin: false,
        msg: null,
      }
    },
    computed:{
      isLogin: function(){
        return this.$store.getters.isAuthenticated
      }
    },
    methods: {
      ...mapActions(['logOut']),
      async logout(){
        await this.logOut();
        this.$router.push("About")
      },
    },
    // created(){
    //   this.getData();
    // }
  }
</script>