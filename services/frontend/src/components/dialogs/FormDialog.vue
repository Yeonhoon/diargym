<template>
  <v-card>
    <v-toolbar dark>{{ headerTitle }}</v-toolbar>
    <v-divider></v-divider>
    <v-card-text
      style="height:350px"
    >
      <slot 
        name="body"
      >
        {{defaultMsg}}  
      </slot>      
    </v-card-text>
    <v-divider></v-divider>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn 
        v-if="isAdd"
        color="red"
        rounded
        text
        @click="$emit('cancel')"
      >
        <b>취소</b>
      </v-btn>
      <v-btn
        v-if="isAdd"
        class="ma-2 " 
        color="blue darken-1"
        text rounded
        @click="$emit('add')">
        <b>운동 추가</b>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>

export default {
  props:{
    headerTitle:{
      type: String,
      default: null
    },
    isAdd:{
      type:Boolean,
      default:true
    }
  },
  name: "FormDialog",
  data: () => ({
    defaultMsg:"slot을 입력하세요",
  })
}
</script>