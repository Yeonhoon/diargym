<template>
  <v-container>
    <v-card>
      <h2>This is Home!</h2>
    </v-card>
    <v-layout column>
      <v-flex ma-10>
        <p v-if="isLogin">
          <v-btn
            color="primary"
            @click='logout'
          > 로그아웃
          </v-btn>

        </p>
        <p v-else>
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

        </p>
        <!-- <v-btn
          :to="{name:'write'}"
          color='warning'
        >
          Sign In
        </v-btn> -->
      </v-flex>
      <v-flex>
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