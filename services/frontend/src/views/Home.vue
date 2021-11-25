<template>
  <v-container mt-12 fluid>
    <v-layout col wrap>
      <v-flex xs12 class='d-flex justify-center mt-15'>
        <h1>DIARGYM</h1>
      </v-flex>
      <v-flex xs12 class="d-flex justify-center">
        <blockquote class="blockquote">
          운동기록을 적어두세요!<br>
          체계적으로 관리하세요! 
        </blockquote>
      </v-flex>
    </v-layout>
    <v-row v-if="isLogin" align="center" justify="center">
      <v-col>
        <div class="text-center">
          <div class="my-2">
            <v-btn :to="{name:'Diary'}" plain color='red lighten-1' rounded large width="250"><strong>운동일지 작성</strong></v-btn>
          </div>
          <div class="my-2">
              <v-btn :to="{name:'Dashboard'}" plain color='primary' rounded large width="250"><strong>대시보드</strong></v-btn>
          </div>
        </div>
      </v-col>
    </v-row>
    <v-row v-else align="center" justify="center">
      <v-col>
        <div class="text-center">
          <div class="my-2">
            <v-btn :to="{name:'Signin'}" plain color='red lighten-1' rounded large width="250">로그인</v-btn>
          </div>
          <div class="my-2 pt-3">
              <v-btn :to="{name:'Signup'}" plain color='primary' rounded large width="250">회원가입</v-btn>
          </div>
        </div>
      </v-col>
    </v-row>
      <v-flex sm6 offset-sm3 class="d-flex justify-center" mt-5 v-if="!isLogin">

      </v-flex>
      <v-flex v-else sm6 offset-sm3 class="d-flex justify-center" mt-5>
      </v-flex>
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
  }
</script>