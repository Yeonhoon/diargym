<template>
  <v-card>
    <v-card-title> {{headerTitle}} </v-card-title>
    <v-card-text>
      <slot name="body">
        {{ defaultBodyContent }}
      </slot>
    </v-card-text>
    <v-card-actions class="justify-end mr-2 pb-4">
      <v-btn
        color="warning"
        raised
        dark 
        @click ="$emit('hide')"
      >
        {{footerHideTitle}}
      </v-btn>
      <template v-if="footerSubmit">
        <v-btn
          color="success"
          @click="$emit('submit')"
        >
          {{ footerSubmitTitle }}
        </v-btn>
      </template>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Dialog",
  props: {
    // footerSubmit: {
    //   type: Boolean,
    //   default: true,
    // },
    headerTitle: {
      type: String,
      default: "제목",
    },
    footerSubmitTitle:{
      type: String,
      default: '예'
    }
  },
  data: () => ({
    footerHideTitle: '아니오',
    defaultBodyContent: 'body slot을 작성하라.',
    footerSubmit: true
  })
}
</script>

<style>

</style>