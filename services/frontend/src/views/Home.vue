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
      <v-flex sm6 offset-sm3 class="d-flex justify-center" mt-5>
          <p v-if="!isLogin">
            <v-btn :to="{name:'Signup'}" color='primary'>Sign Up</v-btn>
            <v-btn :to="{name:'Signin'}" color='primary'>Sign In</v-btn>
          </p>
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
      // getData() {
      //   axios.get('/')
      //   .then((res) => {
      //     this.msg = res.msg
      //   })
      //   .catch(error => {
      //     console.log(error)
      //   })
      // }

    },
    // created(){
    //   this.getData();
    // }

  }
</script>