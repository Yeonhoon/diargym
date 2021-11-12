<template>
  <div>
  <v-autocomplete
    label="운동을 검색해보세요"
    filled
    :items="getCateogryList"
    prepend-icon="mdi-database-search"
    v-model="form.small"
  >
  </v-autocomplete>
    <!-- 검색으로 운동 찾기 -->
    <v-expand-transition v-if="search">
      <v-sheet>
        <v-list
        style="max-height: 200px"
        class="overflow-y-auto"
        >
        <v-list-item-group
            v-model="selectedWorkout"
            multiple
            color="indigo"
        >
            <v-list-item
            v-for="(item,i) in getAllList"
            :key="i"
            :value="item"
            >
            <v-list-item-content>
                {{item}}
            </v-list-item-content>
            </v-list-item>
        </v-list-item-group>
        </v-list>
      </v-sheet>
    </v-expand-transition>
  </div>
</template>