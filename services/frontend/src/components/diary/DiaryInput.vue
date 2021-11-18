<template>
  <v-container>
    <v-layout column>
      <v-flex>
        <!-- select date -->
        <v-menu
          v-model="menu2"
          :close-on-content-click="false"
          :nudge-right="40"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
        <template v-slot:activator="{on, attrs}">
          <v-text-field
            class="mt-5"
            v-model="date"
            label="운동일자"
            prepend-icon="mdi-calendar"
            filled
            v-bind="attrs"
            v-on="on"
          >
          </v-text-field>
        </template>
        <v-date-picker 
          width="250"
          v-model="date" 
          @input="menu2 = false"  
        >
        </v-date-picker>
      </v-menu>
    </v-flex>
    <v-flex class="mx-1 mb-5">
      <v-btn
        v-if="this.selectedWorkout.length>=1"
        width="300"
        color="red darken-1"
        text
        small
        @click="clearSelectedWorkout"
      >
        <v-icon>mdi-trash-can-outline</v-icon>
        지우기
      </v-btn>
      <transition-group v-if="this.workoutsheet">
        <v-card
          v-for="(value,index) in selectedWorkout"
          :key="index"
          elevation="0"
          class="mx-0 mb-3"
          style="width:100%"
        >
          <v-card-title><h5>{{value}}</h5></v-card-title>
          <v-card-text
          >
            <!-- v-if="setFields" -->
            <div
              id="input"
              v-for="(val,key, i) in setFields[value]"
              :key="i"
              class="text-xs-center"
            >
              <!-- {{checkWorkout}} -->
              <!-- <p>key:{{key}}</p>
              <p>val:{{val}}</p> -->
              <!-- <p>value:{{value}}</p> -->
              <!-- <p>{{ i }}</p> -->
              <v-row>
                <v-col cols="5">
                  <v-text-field
                    placeholder="무게"
                    required
                    outlined
                    clearable
                    small
                    type="number"
                    :label="val.lab1"
                    v-model="val.weight"
                    @click="inputDialog=true"
                  >
                  </v-text-field>
                </v-col>
                <v-col cols="2">
                  <p>kg</p>
                  <!-- <v-select
                    label="units"
                    single-line
                    menu-props="auto"
                    :items="weightunit"
                    v-model="val.unit"
                  >
                  </v-select> -->
                </v-col>
                <v-col cols="5">
                  <v-text-field
                    placeholder="횟수"
                    outlined
                    clearable
                    required
                    type="number"
                    :label="val.lab2"
                    v-model="val.reps"
                  >
                  </v-text-field>
                </v-col>
                <!-- <v-col cols="3">
                  <v-text-field
                    v-model="value.count"
                    placeholder="세트수"
                    label="sets"
                  >
                  </v-text-field>
                </v-col> -->
              </v-row>
                <v-divider></v-divider>
              </div>
            </v-card-text>
            <v-card-actions 
              v-if="!Object.keys(setFields).includes(value)">
              <v-btn
                block
                @click="addSet(value);"
              >
                세트추가
              </v-btn>
            </v-card-actions>
            <v-card-actions 
              v-else
              class="justify-center"
            >
              <v-btn
                @click="removeSet(value)"
              >
                <strong>-</strong>세트삭제
              </v-btn>
              <v-btn
                @click="addSet(value)"
              >
                <strong>+</strong>세트추가
            </v-btn>
          </v-card-actions>
        </v-card>
      </transition-group>
    </v-flex>
    <!-- <v-dialog
      transition="dialog-bottom-transition"
    >
      <template v-slot:default="inputDialog">
        <v-card>
          <v-toolbar
          color="primary" dark>
            무게, 세트 입력
          </v-toolbar>
          <v-card-text>
            <v-btn>무게추가</v-btn>
          </v-card-text>
          <v-card-actions>
            <v-btn
              text
              @click="inputDialog=false"
            >
              취소
            </v-btn>
          </v-card-actions>
        </v-card>
      </template>
    </v-dialog> -->
    <v-flex>
    <v-btn
      v-if="this.selectedWorkout.length>=1"
      class="mb-5 white--text"
      large
      color="indigo"
      width=300
      @click="submit"
    >
      저장 
    </v-btn>
    <v-dialog transition="dialog-bottom-transition" v-model="dialog">
      <template v-slot:activator="{on,attrs}">
        <v-btn
          color="blue lighten-2 white--text"
          v-bind="attrs"
          v-on="on"
          width=300
          large
        >
          운동 추가하기
        </v-btn>
      </template>
      <form-dialog
        :headerTitle="`운동 검색`"
        @cancel="hideDialog"
        @add="setWorkout"
        @submit="submit"
      >
        <template v-slot:body>
          <v-sheet class="mt-3">
            <v-slide-group
              v-model="selectedCategory"
            >
              <v-slide-item
                v-for="(item,i) in catMid"
                :key=i
                v-slot="{ active, toggle }"
              > 
                <v-btn
                  v-if="i==0"
                  small 
                  rounded
                  outlined
                  :input-value="active"
                  active-class="blue white--text"
                  depressed
                  @click="toggle"
                >
                  <v-icon>mdi-star</v-icon>
                </v-btn>
                <v-btn class="mx-1" 
                  v-else
                  small 
                  rounded
                  outlined
                  :input-value="active"
                  active-class="blue white--text"
                  depressed
                  @click="toggle"
                > 
                  {{item.name}}
                </v-btn>
              </v-slide-item>
            </v-slide-group>
          </v-sheet>
          <v-sheet class="mt-5">
            <v-text-field 
              class="mx-3" 
              flat 
              placeholder="운동을 검색해보세요"
              outlined
              prepend-inner-icon="search" 
              v-model="search" 
              clearable 
              @click:clear="clearSearch"
            >
            </v-text-field>
          </v-sheet>

          <!-- 카테고리로 운동 찾기 -->
          <!-- 키워드 검색 시 카테고리 내에서만 검색 -->
          <v-expand-transition v-if="selectedCategory!=null">
            <v-sheet>
              <v-list
                style="max-height: 200px"
                class="overflow-y-auto"
              >
                <v-list-item-group
                  multiple
                  color="indigo"
                >
                  <!-- v-model="selectedWorkout" -->
                  <v-list-item
                    v-for="(item, i) in getAllList"
                    :key="i"
                    :value="item"
                    @click="toggleActive(item); snack=true"
                  >
                    <v-list-item-content v-text="item"></v-list-item-content>
                    <v-btn 
                      v-if="!isFavorite"
                      icon
                      :append-icon="isFavorite ? 'mdi-star-outline' :'mdi-star'"
                      @click:append="isFavorite = !isFavorite"
                    >
                      <v-icon>
                        mdi-star-outline
                      </v-icon>
                    </v-btn>
                    <v-btn
                      icon
                      v-else
                    >
                      <v-icon color="yellow darken-3">
                        mdi-star
                      </v-icon>
                    </v-btn>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-sheet>
          </v-expand-transition>
          <!-- 선택한 운동 보여주기 -->
          <v-snackbar
            timeout="-1"
            v-model="snack"
            text
            multi-line

          >
            <h3>내가 선택한 운동:</h3>
            <br>
            <p v-for="(item) in selectedWorkout" :key="item">{{item}}</p>
          </v-snackbar>
        </template>
      </form-dialog>
    </v-dialog>
    <!-- 저장한 운동 불러오는 다이어그램 -->
    <v-dialog
      hide-overlay
      transition="dialog-bottom-transition"
      v-model="archiveDialog"
    >
      <template v-slot:activator="{on,attrs}">
        <v-btn
          class="mt-5 white--text"
          large
          color="red lighten-1"
          v-bind="attrs"
          v-on="on"
          width=300
          @click="loadSetInfo"
        >
          불러오기
        </v-btn>
      </template>
      <v-card>
        <v-toolbar dark >운동 불러오기</v-toolbar>
        <v-card-text>
          <v-list>
            <v-list-group
              v-for="(key,i) in Object.entries(loadedSet)"
              :key="i"
            >
              <template v-slot:activator>
                <v-list-item-content>
                  key:{{key}}
                  i:{{i}}
                  <v-list-item-title v-text="key[0]"></v-list-item-title>
                </v-list-item-content>
              </template>
              <v-list-item
                v-for="(sets, name) in key[1]"
                :key="name"
              >
                <template >
                  <v-list-item-action>
                    <v-checkbox 
                      @change="checkboxUpdate"
                      :value="name"
                    ></v-checkbox>
                  </v-list-item-action>
                  <v-list-item-content>
                      <v-list-item-title> {{name}} </v-list-item-title>
                      <v-list-item-content
                        v-for="set in sets"
                        :key="set"
                      >
                        <v-list-item-subtitle>무게: {{set.rweight}}{{set.runit}} | 횟수: {{set.rrep}}회</v-list-item-subtitle>
                      </v-list-item-content>
                  </v-list-item-content>
                </template>
              </v-list-item>
            </v-list-group>
          </v-list>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn
            text
            rounded
            color="error"
            @click="archiveDialog=false"
          >
            취소
          </v-btn>
          <v-btn
            text
            color="primary"
            @click="getPreviousSets"
          >
            불러오기
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    </v-flex>
      <span>
        <v-alert
          v-if="diaryNotFilled"
          color="red lighten-1"
          prominent
          dense
          type="error"
          elevation=2
        >
          {{ warningMsg }}
        </v-alert>
        <v-alert
          v-if="diarySuccess"
          dense
          text
          type="success"
          :value="diarySuccess"
        >
          "저장 성공!"
        </v-alert>
      </span>
    </v-layout>
    
  </v-container>
  
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
import FormDialog from '../dialogs/FormDialog.vue'
import myMixin from '../../mixins/index'
export default {
  mixins:[myMixin],
  name:"DiaryInput",
  components:{
    FormDialog
  },
  data: () => ({
    dialog:false,
    archiveDialog:false,
    inputDialog:false,
    catMid:[
      {name: '', value: '즐겨찾기'},
      {name:'가슴', value: '가슴'},
      {name:'어깨', value: '어깨'},
      {name:'하체', value: '하체'},
      {name:'등', value: '등'},
      {name:'코어', value: '코어'},
      {name:'이두', value: '이두'},
      {name:'삼두', value: '삼두'},
      {name:'유산소', value:'유산소'}
    ],
    isFavorite:false,
    snack:false,
    selectedCategory:null,
    selectedWorkout: [],
    isSetEmpty: true,
    workoutsheet:false,
    headerTitle:"운동일지 기록",
    workoutlist: null,
    weightunit: ['kg','lb','sec'],
    date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
    menu2: false,
    setFields:{},
    setArr:[],
    loadedSet: {},
    setArchive:[],
    diaryNotFilled: false,
    diarySuccess: false,
    warningMsg:'',
    search:null,
    }),
  computed:{
    ...mapGetters(['stateWorkoutList','stateWorkoutWholeList','stateRecords']),

    //운동 카테고리로 검색하기
    getCateogryList (){
      return Object.values(this.stateWorkoutList)[this.selectedCategory-1]
    },

    getRecords(){
      return this.stateRecords
    },
    getAllList (){
      // return this.stateWorkoutWholeList
      return this.getCateogryList.filter(item => {
        if(!this.search) return this.getCateogryList;
          return (
            item.match(this.search)
          )
       }
      )
    },
    checkWorkout(){
      return this.setFields
    },
    // selectedWorkoutList(){
    //   return this.sele
    // }
  },
  // watch에 함수를 직접 연결할수도 있음.
  // watch:{
  //   selectedWorkout: "toggleActive", 
  // },
  methods:{
    // 운동 리스트 클릭하여 선택/선택취소하기
    toggleActive(i){
      let pos = this.selectedWorkout.indexOf(i)
      pos === -1 ? this.selectedWorkout.push(i) : this.selectedWorkout.splice(pos,1)
      console.log(this.selectedWorkout)
    },
    clearSearch (){
      this.search=""
    },
    clearSelectedWorkout(){
      this.selectedWorkout=[]
      this.$forceUpdate()
    },
    //운동세트 기록 가져와 보여주기
    loadSetInfo(){
      var dates = "rdate"
      var names = "wname"
      var result = this.getRecords.reduce((map,obj)=>{
        if (!map[obj[dates]]) map[obj[dates]]= {};
        [].concat(obj[names]).forEach(sub=>{
          if (!map[obj[dates]][sub]) map[obj[dates]][sub] = [];
          map[obj[dates]][sub].push(obj);
        });
        return map
      },{})

      this.loadedSet = result
    },
    checkboxUpdate(wname){
      if (wname !== null){
        this.setArchive.push(wname)
      } else {
        this.setArchive.splice(wname,1)
      }
      console.log(this.setArchive)

    },
    getPreviousSets(){

    },
    hideDialog(){
      this.dialog=false
      this.diarySuccess=false
      this.diaryNotFilled=false
    },
    setWorkout(){
      this.workoutsheet=true //운동정보 입력하는 transition 띄우기
      this.dialog=false
    },
        ...mapActions(['submitRecords']),
    // async loadWorkout () {
    //   this.loadWorkoutList
    // },
    addSet(index){
      if (!Object.keys(this.setFields).includes(index)){
        this.setFields[index]= new Array()
        this.setArr.push({
          workout: index,
          lab1:'weight',
          weight:"",
          lab2:"reps",
          reps:"",
          unit:"",
          count:""
        })
        for(var i=0; i<this.setArr.length; i++){
            if (this.setArr[i].workout === index) {
              this.setFields[index].push(this.setArr[i])    
            }
          } 
        // this.setFields[index].push(this.setArr)
        this.setArr=[]
      } else {
        this.setArr.push({
          workout: index,
          lab1:'weight',
          weight:"",
          lab2:"reps",
          reps:"",
          unit:"kg",
        })
        // var keys=Object.keys(this.setFields)
        for(var j=0; j<this.setArr.length; j++){
          if (this.setArr[j].workout === index) {
            this.setFields[index].push(this.setArr[j])    
            }
          }
        this.setArr=[]
        // for (var y=0; y< keys.length; y++){
          //   if (index === keys[y]){
            //     this.setFields[index].push(this.setArr)
        //   }
        // }
      }
      // 세트 추가한 뒤 강제
      this.$forceUpdate()
      // this.isSetEmpty=false
      console.log(this.setFields)
      console.log(this.setArr)
    },
    removeSet(index){
      this.setFields[index].pop();
      if (this.setFields[index].length===0){
        delete this.setFields[index]
        this.isSetEmpty=true
      }
      this.$forceUpdate()
      // console.log(this.setFields)
      // console.log(this.isSetEmpty)
      // this.dialog=false
    },
    async submit(){
      console.log(this.setFields)
      let a = Object.keys(this.setFields)[0]
      if (this.setFields[a][0].weight === "" || this.setFields[a][0].reps === ""){
          this.diaryNotFilled = true
          this.warningMsg = "운동종류가 입력되지 않았습니다!"
      }
      else {
        this.diarySuccess= true
        this.diaryNotFilled=false
        this.warningMsg = ""
        let wlist = Object.keys(this.setFields)
        for (var j of wlist){ // 운동 종목
          console.log(j)
          var repsArr=[]
          var weightArr =[]
          var unitArr = []
          for(var k=0; k<this.setFields[j].length; k++){ // 각 종목별 세트 수
            console.log("weight: ",this.setFields[j][k].weight)
            console.log("reps: ",this.setFields[j][k].reps)
            repsArr = repsArr + this.setFields[j][k].reps + " "
            weightArr = weightArr + this.setFields[j][k].weight + " "
            unitArr = unitArr + 'kg' + " "
            
            // if(this.setFields[j][k].unit==='lb'){
            //   weightArr = weightArr + this.setFields[j][k].weight*0.45 + " "
            //   unitArr = unitArr + 'kg' + " "
            // }
            // else if (this.setFields[j][k].unit==='kg'){
            //   weightArr = weightArr + this.setFields[j][k].weight + " "
            //   unitArr = unitArr + this.setFields[j][k].unit + " "
            // }
          }
            let submitData = {
              'rdate': this.date,
              'rsmall': j,
              'rweight': weightArr,
              'runit': unitArr,
              'rrep': repsArr
            }

            console.log(submitData)
            await this.submitRecords(submitData)
            .then(
              this.setFields= [],
            )
        }
          // timer
        let timer = this.submit.timer
        if (timer) {
          clearTimeout(timer)
        }
        this.submit.timer = setTimeout(()=>{
          this.diarySuccess = false
        }, 2000)
        this.recordDialog=false
        // 화면 새로고침
        // window.location.reload();
      }
      // if (this.form.small === ""){
      // }
      // else if (this.setFields.length === 0){
      //   this.diaryNotFilled = true
      //   this.warningMsg = "세트가 입력되지 않았습니다!"
      // }
      // else {

        
      //   
      //   // console.log(submitData)
      //   
      // }
    },

  },
  
}

</script>