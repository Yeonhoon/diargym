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
          :to="{name:'Signin'}"
          color='primary'
        >
          Sign In
        </v-btn>
        <!-- <v-btn
          :to="{name:'write'}"
          color='warning'
        >
          Sign In
        </v-btn> -->
      </v-flex>
      <v-flex>
        <p>백엔드에서 받은 메시지: {{msg}}</p>
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
        // isLogin: false,
        msg: null,
      }
    },

    methods: {
      getData() {
        axios.get('/')
        .then((res) => {
          this.msg = res.msg
        })
        .catch(error => {
          console.log(error)
        })
      }

    },
    created(){
      this.getData();
    }

  }
</script>