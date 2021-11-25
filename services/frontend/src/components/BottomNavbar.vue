<template>
    <v-bottom-navigation
      absolute
      shift
      v-if="isLogin"
      color="indigo"
      
    >
        <v-btn 
          :to="{name:'Home'}" 
          exact
        >
          <span>Home</span>
          <v-icon>mdi-home-variant</v-icon>
        </v-btn>
        <v-btn
          exact
        >
          <span>Libary</span>
          <v-icon>mdi-bookmark-box-multiple</v-icon>
        </v-btn>
        <v-btn 
          :to="{name:'Diary'}" 
          exact
        >
          <span>Diary</span>
          <v-icon>mdi-lead-pencil</v-icon>
        </v-btn>
        <v-btn 
          :to="{name:'Dashboard'}" 
          exact
        >
          <span>Dashboard</span>
          <v-icon>mdi-view-dashboard</v-icon>
        </v-btn>
    </v-bottom-navigation>
</template>

<script>
export default {
    name:'BottomNavbar',
    data: ()=> ({
        drawerLogins:[
        {title: 'Home', path:'/', icon: 'mdi-home-variant'},
        {title: 'Diary', path:'/diary', icon: 'mdi-lead-pencil'},
        {title: 'Dashboard', path:'/dashboard', icon: 'mdi-view-dashboard'},
      ],
      drawersNotLogins:[
        {title: 'Home', path:'/', icon: 'mdi-home-variant'},
        {title: 'About', path:'/about', icon: 'mdi-information'},
      ]
    }),
    computed:{
        isLogin () {
      return this.$store.getters.isAuthenticated;
    },
    }
}
</script>