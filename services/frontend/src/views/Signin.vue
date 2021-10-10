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
                      name="Name"
                      rules="required"
                    >
                      <v-text-field
                        prepend-icon="person"
                        v-model="form.uname"
                        :error-messages="errors"
                        label="ID"
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
                        v-model="form.upw" 
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
                  @click="login"
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
import {mapActions} from 'vuex'
  export default {
    mixins:[myMixin],
    data(){
      return {
        drawer: null,
        form: {
          uname: null,
          upw: null,
      },
        isLoginError: false

      }
    },
    props: {
      source: String
    },
    methods:{
      ...mapActions(['logIn']),
      async login(){
        const User = new FormData();
        User.append('username', this.form.uname);
        User.append('password', this.form.upw);
        try {
          await this.logIn(User);
          this.$router.push('/')
        }
        catch (error){
          this.isLoginError = true
          throw "로그인 실패"
        }





      }
    }
  }
</script>