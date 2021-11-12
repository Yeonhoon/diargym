<template>
  <div>
    <v-data-table
      :headers=headers
      :items=getData
      :search="search"
      class="elevation-2"
      sort-by="rdate"
      loading=true
      loading-text="운동기록이 존재하지 않습니다."
      mobile-breakpoint="0"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-btn 
            text
            color="green darken-2"
            @click="getAllData"
          >
            전체 기록
          </v-btn>
          <v-dialog
            v-model="dialog"
            max-width="400"
            scrollable
          >
            <template v-slot:activator="{on,attrs}">
              <v-btn
                text
                color="blue darken-3"
                @click="addRecord"
                v-bind="attrs"
                v-on="on"

              >
                기록 추가
              </v-btn>
            </template>
            <!-- dialog Input -->
            <form-dialog
              :headerTitle=headerTitle
              :isAdd=false
              @submit="save"
              @cancel="cancel"
            >
              <template v-slot:body>
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
                  v-model="editedItem.rdate"
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
                  v-model="editedItem.rdate" 
                  @input="menu2 = false"    
                  >
                  </v-date-picker>
                </v-menu>
                <v-select
                  label="대분류"
                  outlined
                  required
                  :items="catLarge"
                  v-model="editedItem.rlarge"
                ></v-select>
                <v-select
                  label="중분류"
                  outlined
                  required
                  :items="catMid"
                  v-model="editedItem.rmid"
                ></v-select>
                <v-text-field
                  required
                  label="종류"
                  outlined
                  v-model="editedItem.rsmall"
                  hint="벤치프레스, 스쿼트, 풀업..." 
                >
                </v-text-field>
              
                <v-text-field
                  label="무게"
                  required
                  v-model="editedItem.rweight"
                >
                </v-text-field>

                <v-select
                  label="단위"
                  :items=weightunit
                  v-model="editedItem.runit"
                  >
                </v-select>
                

                <v-text-field
                  label="반복횟수"
                  placeholder="횟수"
                  required
                  v-model="editedItem.rrep"
                >
                </v-text-field>
                
              </template>
            </form-dialog>
          </v-dialog>
          <v-dialog
            v-model="dialogDelete"
            width="400px"
          >
            <alert-dialog
              :headerTitle=alertDialogTitle
              :isCancelNeeds=true
              @cancel="cancleDelete"
              @confirm="removeRecordComfirm"
            >
              <template v-slot:alert>
                <v-alert 
                  type="error"
                  prominent
                  outlined
                  border="top"
                >
                  이 운동기록을 삭제하시겠습니까?
                </v-alert>
              </template>
            </alert-dialog>
          </v-dialog>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon
          small
          class="mr-2"
          color="black darken-2"
          @click="editRecord(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
          small
          color="red darken-2"
          @click="removeRecord(item)"
        >
          mdi-delete
        </v-icon>
      </template>
      
    </v-data-table>
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex'
import formMixin from '../../mixins/index'
import FormDialog from '../dialogs/FormDialog.vue'
import AlertDialog from '../dialogs/AlertDialog.vue'
export default {
  components:{
    FormDialog,
    AlertDialog
  },
  mixin:[formMixin],
  data: ()=>({
    search:'',
    dialog:false,
    menu2:false,
    alertDialogTitle:'Warning',
    headerTitle:'',
    catLarge:['케이블','머신','바벨','덤벨','맨몸'],
    catMid:['가슴','등','어깨', '이두','삼두','하체','코어'],
    catSmall:'',
    weightunit: ['kg','lb','sec'],
    headers:[
      { text:'일자',align:'center',sortable:true, value:'rdate', width:"110px"},
      { text: '대분류', value: 'rlarge', width:"100px" },
      { text: '중분류', value: 'rmid', width:"100px" },
      { text: '종류', value: 'rsmall', width:"100px" },
      { text: '무게', value: 'rweight', width:"80px" },
      { text: '단위', value: 'runit', width:"80px" },
      { text: '횟수', value: 'rrep', width:"80px" },
      { text: '수정/삭제', value:'actions', sortable:false, width:"100px" },
   ],
    form:{
      date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      large:'',
      mid:'',
      small:'',
      weight:'',
      unit:'',
      reps:'',
    },
    editType:null,
    editedIndex:'',
    editedItem:{
      rdate: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      rlarge:'',
      rmid:'',
      rsmall:'',
      rrep:'',
      rweight:'',
      runit:'',
    },
    defaultItem:{
      rdate: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      rlarge:'',
      rmid:'',
      rsmall:'',
      rrep:'',
      rweight:'',
      runit:'',
    },
    dialogDelete:false,
  }),

  methods:{
    ...mapActions(['deleteRecord','submitRecords', 'updateRecord']),
    getAllData(){
      this.$emit('allData','allData')
    },
    addRecord(){
      this.dialog=true,
      this.headerTitle="기록 추가"
      this.editType="add"
    },
    
    editRecord(item){
      this.dialog=true
      this.headerTitle="기록 수정"
      this.editedItem= Object.assign({}, item)
      this.editType="edit"
    },
    save(){ //운동기록 저장
      try{
        if(this.editType === "edit"){
          console.log(this.editedItem)
          this.updateRecord(this.editedItem)
        }
        else if(this.editType === "add"){
          console.log(this.editedItem)
          this.submitRecords(this.editedItem)
        }
      }
      catch (error) {
        console.log(error)
      }
      this.cancel()
      
    },
    cancel(){
      this.dialog = false
      this.$nextTick(()=>{
        this.editedItem= this.defaultItem
      })
    },
    

    removeRecord(item){
      try {
        this.editedIndex = this.getData.indexOf(item)
        this.editedItem = Object.assign({}, item)
        // console.log("삭제대상 아이템:", this.editedItem)
        this.dialogDelete=true
      }
      catch (error) { 
        console.log(error)
      }
    },
    async removeRecordComfirm(){
      this.deleteRecord(this.editedItem)
      this.cancleDelete()
    },
    async cancleDelete(){
      this.dialogDelete = false
      this.$nextTick(()=>{
        this.editedItem= this.defaultItem
        // console.log("삭제대상 아이템:", this.editedItem)
      })
    }
  },
  computed:{
    ...mapGetters(["stateTableRecords"]), //headers: 'stateHeaders',
    // //헤더 가져오기
    // getHeaders(){
    //   return this.headers
    // },
    // 데이터 가져오기
    getData(){
      // console.log(this.data)
      return this.stateTableRecords
    },
    // AllData(){
    //   return this.stateTableRecords
    // }
  },
}
</script>