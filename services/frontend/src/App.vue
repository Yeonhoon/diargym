<template>
  <v-app class="mx-auto overflow-hidden">
    <Navbar/> 
    <v-sheet
      class="overflow-y-auto"
      max-height="800"
    >
      <v-main>
        <router-view/>
      </v-main>
    </v-sheet>
      <!-- <Footer/> -->
  
  </v-app>



</template>

<script>
import Navbar from '@/components/Navbar.vue'
// import Footer from '@/components/Footer.vue'
export default {
  name: 'App',
  components:{
    Navbar
  },
};
</script>