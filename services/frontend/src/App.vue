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
      <bottom-navbar></bottom-navbar>
    </v-sheet>
    <!-- <Footer/> -->
    
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
// import Footer from '@/components/Footer.vue'
import BottomNavbar from '@/components/BottomNavbar.vue'
export default {
  name: 'App',
  components:{
    Navbar,
    BottomNavbar
    // Footer
  },
  data: ()=>({
    direction: 'top',
    fab: false,
    fling: false,
    hover: false,
    tabs: null,
    top: false,
    right: true,
    bottom: true,
    left: false,
    transition: 'slide-y-reverse-transition'
  })
};
</script>
<style>
  /* #create .v-speed-dial {
    position: absolute;
  } */

  /* #create .v-btn--floating {
    position: relative;
  } */
</style>
