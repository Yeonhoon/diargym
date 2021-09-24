<template>
  <v-container>
    <v-layout column>
      <v-flex>
        <h2>회원가입</h2>
        <v-text-field
          v-model= "uname"
          label='Name'>
        </v-text-field>
        <v-text-field
          v-model= "upw"
          label='Password'>
        </v-text-field>
        <v-text-field
          v-model= "uemail"
          label='Email'>
        </v-text-field>
        <v-btn 
          @click= "addUser"
          color='primary'
        >회원가입!</v-btn>

      </v-flex>
      <v-flex mt-10>
        <h2>Result</h2>
        <p>{{data}}</p>
        
      </v-flex>
    </v-layout>
    

  </v-container>
</template>

<script>
import axios from 'axios'
  export default {

    data: () => ({ 
      data: '',
      upw: '',
      uemail: '',
      uname: ''
    }),
    methods: {
      getData(){
        axios.get('/')
          .then( res => {
            this.data = res.data;
          })
          .catch(error => {
            console.log(error);
          })
      },
      
      addUser(){
        axios.post('/newuser',{
          name: this.uname,
          email : this.uemail,
          password: this.upw
        })
        .then(() => {
          this.name = null
          this.uemail = null
          this.password = null
        })
        .catch(error => {
          console.log(error)
        })
      }
    },
    created() {
      this.getData();
    }
  
  }
</script>
