<template>
  <v-container>
    <v-card>
      <h2>This is Home!</h2>
    </v-card>
    <v-layout column>
      <v-flex ma-10>
        <v-btn
          :to="{name:'Signup'}"
          color='primary'
        >
          Sign Up
        </v-btn>
        <v-btn
          v-if = "!islogin"
          :to="{name:'Signin'}"
          color='primary'
        >
          Sign In
        </v-btn>
        <v-btn
          v-if = "islogin"
          :to="{name:'write'}"
          color='warning'
        >
          Sign In
        </v-btn>
      </v-flex>
      <v-flex>
        <p>유저정보: {{userData}}</p>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import axios from 'axios'
  export default {
    data () {
      return {
        userData: '',
        isLogin: false
      }
    },

    methods: {
      getData(){
        axios.get('/')
          .then( res => {
            this.userData = res.data;
          })
          .catch(error => {
            console.log(error);
          })
      },

    },
    created() {
      this.getData();
    },

  }
</script>