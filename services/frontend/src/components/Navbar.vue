<template>
  <div>
    <v-app-bar
      color="primary"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
     
      <v-spacer></v-spacer>
      <v-menu>
        <template v-slot:activator="{on, attrs}">
          <v-btn
            text
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </template>
        <v-list
          v-if="isLogin"
        >
          <v-list-item>
            <v-list-item-title :to="{name:'Home'}">Home</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title @click="logout">logout</v-list-item-title>
          </v-list-item>
        </v-list>
        <v-list v-else>
          <v-list-item
            v-for = "item in menuItems"
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
            "Application"
          </v-list-item-title>
          <v-list-item-subtitle
             v-if="isLogin"
          >
            {{this.currentUser}}님 반갑습니다!
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
    isLogin: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
  data(){
    return{
      drawer : false,
      currentUser: null,
       menuItems: [
          { title: 'Home', path: '/', icon: 'home' },
          { title: 'Sign Up', path: '/register', icon: 'face' },
          { title: 'Sign In', path: '/login', icon: 'lock_open' }
        ],
    }
  },
  methods:{
    async logout(){
      await this.$store.dispatch('logOut');
      this.$router.push('/login');
    },
    async login(){
      this.$router.push('/')
    },

  },
  mounted(){
    this.currentUser = this.$store.getters.stateUser.uid;
  }
}
</script>