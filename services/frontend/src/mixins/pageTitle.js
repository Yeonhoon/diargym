import Vue from 'vue';

const suffix = 'DIARGYM';
const pageTitle = {
  watch: {
    vuePageTitle(to){
      document.title=`${to}${suffix}`
    }
  }
};

Vue.mixin(pageTitle)
