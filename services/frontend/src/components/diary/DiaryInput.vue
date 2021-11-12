<template>
  <v-container>
    <v-layout column>
      <v-flex>
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
            v-model="form.date"
            label="운동일자"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          >
          </v-text-field>
        </template>
        <v-date-picker 
          width="250"
          v-model="form.date" 
          @input="menu2 = false"  
        >
        </v-date-picker>
      </v-menu>
    </v-flex>
    <v-flex class="mx-1 mb-5">
      <transition-group v-if="this.workoutsheet">
        <v-card
          v-for="(value,index) in selectedWorkout"
          :key="index"
          elevation="0"
          class="mx-0 mb-3"
          style="width:100%"
        >
          <v-card-title><h5>{{value}},{{index}}</h5></v-card-title>
          <v-card-text>
            <div
              v-for="(value, i) in setArr"
              :key="i"
              class="text-xs-center"
            >
              <v-row>
                <v-col cols="6">
                  <v-text-field
                    placeholder="무게"
                    required
                    filled
                    small
                    type="number"
                    :label="value.lab1"
                    v-model="value.weight"
                    @click="inputDialog=true"
                  >
                  </v-text-field>
                </v-col>
                <!-- <v-col cols="4">
                  <v-select
                    label="units"
                    :items="weightunit"
                    v-model="value.unit"
                  >
                  </v-select>
                </v-col> -->
                <v-col cols="6">
                  <v-text-field
                    placeholder="횟수"
                    required
                    :label="value.lab2"
                    v-model="value.reps"
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
        <v-btn
          class="mt-5 white--text"
          large
          color="red lighten-1"
          v-bind="attrs"
          v-on="on"
          width=300
        >
          불러오기
        </v-btn>
      </template>
      <form-dialog
        :headerTitle="`운동 검색`"
        @cancel="hideDialog"
        @add="setWorkout"
        @submit="submit"
        @remove="removeSet"
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
                  <v-icon>mdi-bookmark</v-icon>
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
              filled
              prepend-inner-icon="search" 
              v-model="search" 
              clearable 
              @click:clear="clearSearch">
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
                    <v-list-item-title v-text=item>

                    </v-list-item-title>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-sheet>
          </v-expand-transition>
          <v-snackbar
            timeout="-1"
            v-model="snack"
            text
            color="primary"

          >
            <h3>내가 선택한 운동:</h3>
            <br>
            <p v-for="(item) in selectedWorkout" :key="item">{{item}}</p>
            <!-- {{selectedWorkout}} -->

          </v-snackbar>
        </template>
      </form-dialog>
    </v-dialog>
    </v-flex>
    <validation-observer
      ref="observer"
    >
    
      </validation-observer>
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
    setcount:0,
    snack:false,
    selectedCategory:null,
    selectedWorkout: [],
    isSetEmpty: true,
    workoutsheet:false,
    headerTitle:"운동일지 기록",
    workoutlist: null,
    weightunit: ['kg','lb','sec'],
    form:{
      date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      small:'',
      weight:'',
      unit:'',
      reps:'',
    },
    count:'',
    menu2: false,
    setFields:{},
    setArr:[],
    diaryNotFilled: false,
    diarySuccess: false,
    warningMsg:'',
    search:null,

    }),
  computed:{
    ...mapGetters(['stateWorkoutList','stateWorkoutWholeList']),

    //운동 카테고리로 검색하기
    getCateogryList (){
      return Object.values(this.stateWorkoutList)[this.selectedCategory-1]
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
  },
  // watch에 함수를 직접 연결할수도 있음.
  // watch:{
  //   selectedWorkout: "toggleActive", 
  // },
  methods:{
    toggleActive(i){
      let pos = this.selectedWorkout.indexOf(i)
      pos === -1 ? this.selectedWorkout.push(i) : this.selectedWorkout.splice(pos,1)
      console.log(this.selectedWorkout)
    },
    clearSearch (){
      this.search=""
    },
    ...mapActions(['submitRecords']),
    // async loadWorkout () {
    //   this.loadWorkoutList
    // },
    hideDialog(){
      this.recordDialog=false
      this.diarySuccess=false
      this.diaryNotFilled=false
    },
    async submit(){
      if (this.form.large==="" || this.form.mid === "" || this.form.small === ""){
        this.diaryNotFilled = true
        this.warningMsg = "운동종류가 입력되지 않았습니다!"
      }
      else if (this.setFields.length === 0){
        this.diaryNotFilled = true
        this.warningMsg = "세트가 입력되지 않았습니다!"
      }
      else {
        this.diarySuccess= true
        this.diaryNotFilled=false
        this.warningMsg = ""

        for (var j=0; j<this.setFields.length; j++){
          for(var k=0; k<this.setFields[j].count; k++){
            this.form.reps = this.form.reps + this.setFields[j]['reps'] + " "
            if(this.setFields[j]['unit']==='lb'){
              this.form.weight = this.form.weight + this.setFields[j]['weight']*0.45 + " "
              this.form.unit = this.form.unit + 'kg' + " "
            }
            else if (this.setFields[j]['unit']==='kg'){
              this.form.weight = this.form.weight + this.setFields[j]['weight'] + " "
              this.form.unit = this.form.unit + this.setFields[j]['unit'] + " "
            }
          }
        }
        
        let submitData = {
          'rdate': this.form.date,
          'rlarge': this.form.large,
          'rmid': this.form.mid,
          'rsmall': this.form.small,
          'rweight': this.form.weight,
          'runit': this.form.unit,
          'rrep': this.form.reps
        }
        // console.log(submitData)
        await this.submitRecords(submitData)
        .then(
          this.setFields= [],
          this.form.weight= "",
          this.form.unit="",
          this.form.reps="",
          this.form.count="",
        )
        // timer
        let timer = this.submit.timer
        if (timer) {
          clearTimeout(timer)
        }
        this.submit.timer = setTimeout(()=>{
          this.diarySuccess = false
          this.form.small = ''
        }, 2000)
        this.recordDialog=false
        // 화면 새로고침
        window.location.reload();
      }
    },
    setWorkout(){
      this.workoutsheet=true //운동정보 입력하는 transition 띄우기
      this.dialog=false
    },
    addSet(index){
      if (!Object.keys(this.setFields).includes(index)){
        this.setFields[index]= new Array()
        this.setArr.push({
          lab1:'weight',
          weight:"",
          lab2:"reps",
          reps:"",
          unit:"",
          count:""
        })
        this.setFields[index].push(this.setArr)
        // this.setArr=[]

      } else {
        this.setArr.push({
          lab1:'weight',
          weight:"",
          lab2:"reps",
          reps:"",
          unit:"",
          count:""
        })
        var keys=Object.keys(this.setFields)
        for (var y=0; y< keys.length; y++){
          if (index === keys[y]){
            this.setFields[index].push(this.setArr)
          }
        }
        // this.setArr=[]
      }
      this.isSetEmpty=false
      console.log(this.setFields)
      console.log(this.isSetEmpty)
    },
    removeSet(index){
      this.setFields[index].pop();
      if (this.setFields[index].length===0){
        delete this.setFields[index]
        this.isSetEmpty=true
      }
      console.log(this.setFields)
      console.log(this.isSetEmpty)
      // this.dialog=false
    },

  },
  
}

</script>