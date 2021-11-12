<template>
  <v-card>
    <v-toolbar color="primary" dark>{{ headerTitle }}</v-toolbar>
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
      <v-btn 
        v-if="isAdd"
        color="red"
        rounded
        text
        @click="$emit('remove')"
      >
        취소
      </v-btn>
      <v-btn
        v-if="isAdd"
        class="ma-2 " 
        color="blue darken-1"
        text rounded
        @click="$emit('add')">
        운동 추가
      </v-btn>
      <!-- <v-btn 
          class="ma-2 white-text" 
          color="blue darken-1"
          text
          @click="$emit('submit')"
        >
        저장
      </v-btn> -->
    </v-card-actions>
  </v-card>
      <!-- <v-btn
        color="red darken-1"
        text
        @click="$emit('cancel')"
      >
        취소
      </v-btn> -->

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