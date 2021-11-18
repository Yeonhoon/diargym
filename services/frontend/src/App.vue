<template>
  <v-app class="mx-auto overflow-hidden">
    <Navbar/> 
    <v-sheet
      class="overflow-y-auto"
      max-height="800"
    >
      <v-main>
        <router-view/>
        <v-speed-dial
          v-model="fab"
          top
          hover
          slide-y-reverse-transition
        >
            <template v-slot:activator>
              <v-btn
                v-model="fab"
                color="blue darken-2"
                dark
                bottom
                right
                fab
              >
                <v-icon v-if="fab">
                  mdi-close
                </v-icon>
                <v-icon v-else>
                  mdi-account-circle
                </v-icon>
              </v-btn>
            </template>
            <v-btn
              fab
              dark
              small
              color="green"
              :to="{name:'Home'}"
            >
              <v-icon>mdi-home</v-icon>
            </v-btn>
            <v-btn
              fab
              dark
              small
              color="indigo"
              :to="{name:'Diary'}"
            >
              <v-icon>mdi-lead-pencil</v-icon>
            </v-btn>
            <v-btn
              fab
              dark
              small
              color="red"
              :to="{name:'Dashboard'}"
            >
              <v-icon>mdi-view-dashboard</v-icon>
            </v-btn>
        </v-speed-dial>
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
