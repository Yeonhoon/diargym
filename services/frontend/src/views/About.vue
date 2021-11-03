<template>
  <v-container>
    <v-row dense>
      <v-col cols="12">
        <v-card class="mt-5"
          v-for="item in introList"
          :key="item.title"
        >
          <!-- :color= "item.color" -->
          <v-img
            :src="item.src"
          >

          </v-img>
          <v-card-title class="text-h6">
            {{ item.title }}
          </v-card-title>
          <v-divider class="mx-4"></v-divider>
          <v-card-text>
            <p> {{item.content}} </p>
            <blockquote>{{ item.sub }}</blockquote>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    introList:[
      {title:"DIARGYM?",
        content:"DIARY + GYM", 
        sub:"DIARGYM은 운동기록을 저장하는 일기장입니다. 간편하게 운동기록을 관리해보세요.",
        color:"#E8EAF6",
        src:""},
      {title:"왜 운동일지를 작성할까요?", content:"운동기록 확인이 쉽습니다.", sub:"어떤 운동을 했었는지 외우지 마세요!",
       color:"#E3F2FD",
       src:""},
      {title:"DIARGYM의 장점", content:"체계적으로 운동기록을 관리할 수 있습니다.", sub:"차트를 통해 운동 수행능력을 한 눈에 파악할 수 있습니다. 점진적 과부하는 당신의 것입니다!",
      color:"#E0F7FA",
      src:""},
    ]
  })
}
</script>
