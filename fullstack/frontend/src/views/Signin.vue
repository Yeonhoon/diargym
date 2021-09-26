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
              이메일 혹은 비밀번호가 올바르지 않습니다!
            </v-alert>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Sign in</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <validation-observer>
                  <v-form>
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
                      name="password"
                    >
                      <v-text-field 
                        prepend-icon="lock" 
                        v-model= "upw" 
                        label="Password" 
                        type="password"
                        :error-messages="errors"></v-text-field>
                    </validation-provider>
                  </v-form>
                </validation-observer>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn 
                  color="primary"
                  @click="signin"
                >Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import 'material-design-icons-iconfont/dist/material-design-icons.css' 
import myMixin from '../mixins/index'
import axios from 'axios'
  export default {
    mixins:[myMixin],
    data: () => ({
      drawer: null,
      uemail: null,
      upw: null,
      isLoginError: false
    }),
    props: {
      source: String
    },
    methods:{
      signin(){
        axios.post('/signin',{
          email: this.uemail,
          password: this.upw
        })
        .then(()=> {
          this.uemail= null
          this.upw = null
          this.isLoginError = false
          this.$router.push({'name':'Home'})
        })
        .catch(error => {
          this.isLoginError = true
          console.log(error)
        })

      }
    }
  }
</script>