<template>
    <p>유저정보: {{userData}}</p>
</template>
<script>
import axios from 'axios'
export default {
    methods:{
        data(){
            return{
                userData: null
            }
        },
        getData(){
            axios.get('/users/whoami')
              .then( res => {
                this.userData = res.data;
              })
              .catch(error => {
                console.log(error);
              })
          },

    }
}
</script>