<template>
  <v-app id="inspire">
    <v-main>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-alert
              class="mb-3"
              :value="isLoginError"
              type="error" 
            >
              입력하신 값들을 확인해주세요!
            </v-alert>
            
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
                  rules="required|max:16"
                >
                  <v-text-field
                    prepend-icon="person"
                    v-model="form.uname"
                    :counter="16"
                    :error-messages="errors"
                    label="ID"
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
                    v-model="form.uemail"
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
                    v-model="form.upw" 
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
                    v-model="form.upw2" 
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
import {mapActions} from 'vuex'
import 'material-design-icons-iconfont/dist/material-design-icons.css' 
import myMixin from '../mixins/index'
export default {
  mixins:[myMixin],
  data: () => ({
    form:{
      uname: null,
      uemail: null,
      upw1: null,
      upw2: null,
    },
    isLoginError: false
  }),
  props: {
    source: String
  },
  methods: {
    ...mapActions(['register']),
    async addUser(){
      try {
        await this.register(this.form)
        this.$router.push({'name':'Home'})
        this.isLoginError = false
      }
      catch (error) {
        this.isLoginError = true
        throw 'User name already exists.'
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