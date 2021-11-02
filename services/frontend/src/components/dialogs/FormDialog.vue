<template>
  <v-card>
    <v-card-title>{{ headerTitle }}</v-card-title>
      <v-divider></v-divider>
      <v-card-text>
        <slot name="body">
          {{defaultMsg}}  
        </slot>      
      </v-card-text>
    <v-card-actions>
  <v-spacer></v-spacer>
  <v-btn
    color="red darken-1"
    text
    @click="$emit('cancel')"
  >
    취소
  </v-btn>
  <v-btn 
    v-if="isAdd"
    color="red"
    rounded
    text
    @click="$emit('remove')"
  >
    <v-icon>mdi-minus</v-icon>
  </v-btn>
  <v-btn
    v-if="isAdd"
    class="ma-2 " 
    color="blue darken-1"
    text rounded
    @click="$emit('add')">
    <v-icon>mdi-plus</v-icon>
  </v-btn>
    <v-btn 
      class="ma-2 white-text" 
      color="blue darken-1"
      text
      @click="$emit('submit')"
    >
      저장
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