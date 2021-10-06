<template>
  <div>
    <v-toolbar
      color="primary"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>
      <v-spacer></v-spacer>
      <v-toolbar-items v-if="isLogin" class="hidden-xs-only">
        <v-btn exact text :to="{name:'Home'}" > <v-icon>mdi-home</v-icon>Home </v-btn>
        <v-btn text @click="logout"> <v-icon>mdi-lock</v-icon> Logout</v-btn>
      </v-toolbar-items>
      <v-toolbar-items v-else >
        <v-btn text 
          exact
          v-for = "item in menuItems"
          :key="item.title"
          :to="item.path"
        >
          <v-icon left>{{item.icon}}</v-icon>
          {{item.title}}

        </v-btn>
      </v-toolbar-items>
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

     
    </v-toolbar>
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