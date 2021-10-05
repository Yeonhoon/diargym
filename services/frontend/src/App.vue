<template>
  <v-app>
    <Navbar/> 
    <!-- <v-menu 
        class="hidden-md-and-up"
        bottom
        left
        offset-y>
        <template
          v-slot: activator="{on}">
          <v-btn icon><v-icon v-on="on">mdi-account</v-icon></v-btn>
        </template>
        <v-list>
          <v-list-item :to="{name:'mypage'}">마이 페이지</v-list-item>
          <v-list-item @click="logout">로그아웃</v-list-item>
        </v-list>
      </v-menu> -->
    <v-main>
      <router-view/>
    </v-main>

  </v-app>



</template>

<script>
import Navbar from '@/components/Navbar.vue'
export default {
  name: 'App',
  components:{
    Navbar
  },
};
</script>
