<template>
  <div>
    <thankyou-dialog
      v-if="getDialogToggle"
      :dialog="getDialogToggle"
      :emoji="getDialogInfo.emoji"
      :title="getDialogInfo.title"
      :firstLineText="getDialogInfo.firstLineText"
      :secondLineText="getDialogInfo.secondLineText"
    >
    </thankyou-dialog>
    <v-app-bar
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <span>
      <v-icon>mdi-dumbbell</v-icon>
        DIARGYM
      </span>
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
      temporary
      bottom
      app
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
      <v-switch
        class="pl-5"
        inset
        :label="$vuetify.theme.dark ?'밝게' :'어둡게'"
        v-model="$vuetify.theme.dark"
        persistent-hint
      >
      </v-switch>
      <v-divider></v-divider>

      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-if="isLogin"
          active-class="deep-blue--text text--accent-4"
        >
          <v-list-item
            v-for="item in drawerLogins"
            :key="item.title"
            :to="item.path"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
        <v-list-item-group
          v-else
        >
          <v-list-item exact
            v-for="item in drawersNotLogins"
            :key="item.title"
            :to="item.path"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>


<script>
import ThankyouDialog from './dialogs/ThankyouDialog.vue';
import { mapGetters } from 'vuex'
export default {
  components: { ThankyouDialog },
  name: 'NavBar',
  computed: {
    ...mapGetters(['getDialogToggle', 'getDialogInfo']),
    isLogin () {
      return this.$store.getters.isAuthenticated;
    },
    currentUser (){
      return this.$store.getters.stateUser.uid;
    }
  },
  data(){
    return{
      isDark: false,
      drawer : false,
      fab: false,
      menuItems: [
          // { title: 'Home', path: '/', icon: 'home' },
        { title: 'Sign Up', path: '/register', icon: 'face' },
        { title: 'Sign In', path: '/login', icon: 'lock_open' }
      ],
      menuLogins:[
          // { title: 'Home', path: '/', icon: 'home' },
          { title: 'Diary', path: '/diary', icon: 'face' },
          { title: 'Dashboard', path: '/dashboard', icon: 'lock_open' }
      ],
      drawerLogins:[
        {title: 'Home', path:'/', icon: 'mdi-home-variant'},
        {title: 'About', path:'/about', icon: 'mdi-information'},
        {title: 'Diary', path:'/diary', icon: 'mdi-lead-pencil'},
        {title: 'Dashboard', path:'/dashboard', icon: 'mdi-view-dashboard'},
        {title: 'My Page', path:'/profile', icon: 'mdi-weight-lifter'},
      ],
      drawersNotLogins:[
        {title: 'Home', path:'/', icon: 'mdi-home-variant'},
        {title: 'About', path:'/about', icon: 'mdi-information'},
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