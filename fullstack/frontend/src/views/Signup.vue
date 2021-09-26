<template>
  <v-app id="inspire">
    <v-main>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <!-- <v-alert
              class="mb-3"
              :value="isLoginError"
              type="error" 
            >
              입력하신 값들을 확인해주세요!
            </v-alert> -->
            
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Sign Up</v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-text>
              <validation-observer
                ref="observer"
              >
              <v-form>
                <validation-provider
                  v-slot="{ errors }"
                  name="Name"
                  rules="required|max:10"
                >
                  <v-text-field
                    prepend-icon="person"
                    v-model="uname"
                    :counter="10"
                    :error-messages="errors"
                    label="Name"
                    required
                  ></v-text-field>
                </validation-provider>
                
                <validation-provider
                  v-slot="{ errors }"
                  name="email"
                  rules="required|email"
                >
                  <v-text-field
                    prepend-icon="email"
                    v-model="uemail"
                    :error-messages="errors"
                    label="E-mail"
                    required
                  ></v-text-field>
                </validation-provider>
                <validation-provider
                  rules='required'
                  v-slot="{ errors }"
                  name="password1"
                >
                  <v-text-field 
                    prepend-icon="lock" 
                    v-model= "upw1" 
                    label="Password" 
                    type="password"
                    :error-messages="errors"></v-text-field>
                </validation-provider>
                <validation-provider
                  rules='required|password:@password1'
                  v-slot="{ errors }"
                  name="password2"
                >
                  <v-text-field 
                    prepend-icon="lock" 
                    v-model= "upw2" 
                    label="Password" 
                    type="password"
                    :error-messages="errors"></v-text-field>
                </validation-provider>
              </v-form>
            </validation-observer>
                <!-- <v-form id="signupForm">
                  <v-text-field prepend-icon="person" v-model= "uname" label="Name" type="text"></v-text-field>
                  <span class="warnings">{{uidWarning}}</span>
                  <v-text-field prepend-icon="mail" v-model= "uemail" label="Email" type="email"></v-text-field>
                  <span class="warnings">{{uemailWarning}}</span>
                  <v-text-field prepend-icon="lock" v-model= "upw1" label="Password" type="password"></v-text-field>
                  <v-text-field prepend-icon="lock" v-model= "upw2" label="Check Password" type="password"></v-text-field>
                  <span class="warnings">{{upwWarning}}</span>
                </v-form> -->
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="addUser">Sign Up</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
// import {mapActions} from 'vuex'
import 'material-design-icons-iconfont/dist/material-design-icons.css' 
import axios from 'axios'
import myMixin from '../mixins/index'

  export default {
    mixins:[myMixin],
    data: () => ({
      uname: null,
      uemail: null,
      upw1: null,
      upw2: null,
      uidWarning: null,
      upwWarning: null,
      uemailWarning: null,
    }),
    props: {
      source: String
    },
    methods: {
      addUser(){
        if(this.uname===null | this.uemail === null){
          console.log('입력해라')
        }
        else{
          axios.post('/newuser',{
            name: this.uname,
            email : this.uemail,
            password: this.upw1
          })
          .then(() => {
            this.name = null
            this.uemail = null
            this.password = null
            this.isLoginError = false
            this.$router.push({'name':'Home'})
          })
          .catch(error => {
            console.log(error)
          })
        }
      },
    },
  }
</script>
<style>
  .warnings {
    color:red;
    font-size: small;
  }
</style>