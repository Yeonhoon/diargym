<template>
  <v-app id="inspire">
    <v-main>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-alert
              class="mb-3"
              :value="isSignupError"
              type="error" 
            >
              입력하신 값들을 확인해주세요!
            </v-alert>
            
            <v-card class="elevation-12" ref="form">
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
                  name="ID"
                  rules="required|max:16"
                >
                <v-text-field
                    prepend-icon="mdi-key"
                    v-model="form.uid"
                    :counter="16"
                    :error-messages="errors"
                    label="아이디"
                    required
                  ></v-text-field>
                <v-btn 
                  text color="red darken-3"
                  @click="duplicationCheck"
                >
                  중복확인
                </v-btn>
                </validation-provider>

                <validation-provider
                  v-slot="{ errors }"
                  name="이름"
                  rules="required|max:16"
                >
                  <v-text-field
                    prepend-icon="person"
                    v-model="form.uname"
                    :counter="16"
                    :error-messages="errors"
                    label="이름"
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
                    label="이메일"
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
                    label="비밀번호" 
                    :type="showpw ?'text' :'password'"
                    :append-icon="showpw ? 'mdi-eye' :'mdi-eye-off'"
                    :error-messages="errors"
                    @click:append="showpw = !showpw"
                  ></v-text-field>
                </validation-provider>
                <validation-provider
                  rules='required|password:@password1'
                  v-slot="{ errors }"
                  name="password2"
                >
                  <v-text-field 
                    prepend-icon="lock" 
                    v-model="form.upw2" 
                    label="비밀번호 재입력" 
                    :type="showpw ?'text' :'password'"
                    :append-icon="showpw ? 'mdi-eye' :'mdi-eye-off'"
                    :error-messages="errors"
                    @click:append="showpw = !showpw"
                  ></v-text-field>
                </validation-provider>
              </v-form>
            </validation-observer>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn text color="error" :to="{name:'Home'}">취소</v-btn>
                <v-btn text color="primary" @click="submit">가입</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapActions } from 'vuex'
import 'material-design-icons-iconfont/dist/material-design-icons.css' 
import myMixin from '../mixins/index'
export default {
  mixins:[myMixin],
  data: () => ({
    form:{
      uid: null,
      uname:null,
      uemail: null,
      upw1: null,
      upw2: null,
    },
    showpw:false,
    signupForm:false,
    isSignupError: false
  }),

  props: {
    source: String
  },

  methods: {
    ...mapActions(['register','checkID']),
    async duplicationCheck(){
      this.checkID(this.uid)
    },
    async submit(){
      this.$refs.observer.validate() //프로미스 객체: .then 등으로 호출
      .then((val)=>{
        if(val){
          this.register(this.form)
          this.$router.push({'name':'Home'})
        }
      })
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