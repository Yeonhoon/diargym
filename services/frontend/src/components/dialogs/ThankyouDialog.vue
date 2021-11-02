<template>
  <v-dialog v-model="dialog" max-width="250">
    <v-card>
      <v-card-title class="justify-center mb-4" style="font-size: 2rem;">
        <div>{{ emoji }}</div>
      </v-card-title>

      <v-card-subtitle class="text-center pb-2 font-weight-bold">
        <div>{{ title }}</div>
      </v-card-subtitle>

      <v-card-text class="text-center">
        <div v-if="firstLineText">{{ firstLineText }}</div>
        <div v-if="secondLineText">{{ secondLineText }}</div>
        <div v-if="thirdLineText">{{ thirdLineText }}</div>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  // props: ["title", "firstLineText", "secondLineText", "ThirdLineText", "btnText", "dialog"],
  props: {
    dialog: Boolean,
    timeout: {
      type: Number,
      default: 1000,
    },

    emoji: String,
    title: String,
    firstLineText: String,
    secondLineText: String,
    thirdLineText: String,
  },
  mounted() {
    setTimeout(() => {
      this.$store.dispatch("closeDialog")
    }, this.timeout)
  },
  // destroyed() {
  //   console.log("destoyed")
  // },
}
</script>

<style></style>