<template>
  <div>
    <v-app-bar
      color="primary"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      DIARGYM
      <v-spacer></v-spacer>
      <v-btn text icon @click="toHome">
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-menu>
        <template v-slot:activator="{on, attrs}">
          <v-btn
            text
            v-bind="attrs"
            v-on="on"
            rounded
          >
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </template>
        <v-list
          v-if="isLogin"
        >
          <v-list-item 
            v-for="item in menuLogins"
            :key="item.title"
            :to="item.path">
            <v-list-item-title>{{item.title}}</v-list-item-title>
          </v-list-item>
          <v-list-item  @click="logout">
            <v-list-item-title>logout</v-list-item-title>
          </v-list-item>
        </v-list>
        <v-list v-else>
          <v-list-item
            v-for ="item in menuItems"
            :key="item.title"
            :to="item.path"
          >
            <v-list-item-title>
              {{item.title}}
            </v-list-item-title>

          </v-list-item>
        </v-list>
      </v-menu>
     
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            DIARGYM
          </v-list-item-title>
          <v-list-item-subtitle
             v-if="isLogin"
          >
            {{currentUser}}님 반갑습니다!
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>

      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-if="isLogin"
          active-class="deep-blue--text text--accent-4"
        >
          <v-list-item exact
            :to="{name:'Home'}"
          >
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item
            @click="logout"
          >
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
          <v-list-item
            to="/profile"
          >
            <v-list-item-title>My page</v-list-item-title>
          </v-list-item>
          <v-list-item
            to="/diary"
          >
            <v-list-item-title>Diary</v-list-item-title>
          </v-list-item>
          <v-list-item
            to="/dashboard"
          >
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item>

          
        </v-list-item-group>
        <v-list-item-group
          v-else
        >
          <v-list-item exact
            :to="{name:'Home'}"
          >
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>


<script>
export default {
  name: 'NavBar',
  computed: {
    isLogin () {
      return this.$store.getters.isAuthenticated;
    },
    currentUser (){
      return this.$store.getters.stateUser.uid;
    }
  },
  data(){
    return{
      drawer : false,
      menuItems: [
          // { title: 'Home', path: '/', icon: 'home' },
          { title: 'Sign Up', path: '/register', icon: 'face' },
          { title: 'Sign In', path: '/login', icon: 'lock_open' }
        ],
      menuLogins:[
          // { title: 'Home', path: '/', icon: 'home' },
          { title: 'Diary', path: '/diary', icon: 'face' },
          { title: 'Dashboard', path: '/dashboard', icon: 'lock_open' }
      ]
    }
  },
  methods:{
    toHome(){
      this.$router.push('/')
    },

    async logout(){
      await this.$store.dispatch('logOut');
      this.$router.push('/');
    },
    async login(){
      this.$router.push('/')
    },

  },
  mounted(){
    
  }
}
</script>