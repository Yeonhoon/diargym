<template>
    <v-app>
        <v-form>
            <v-col class='d-flex justify-center mb-5' >
                <h1>운동일지 작성</h1>
            </v-col>
            <v-row
                class="justify-center mt-3"
            >
                <v-dialog
                    v-model="dialog"
                    max-width="400"
                    scrollable
                >
                    <template v-slot:activator="{on,attrs}">
                        <v-btn
                            color="primary"
                            text
                            v-bind="attrs"
                            v-on="on"
                        >
                            <v-icon>mdi-pen</v-icon>
                            기록 추가
                        </v-btn>

                    </template>
                    <!-- show modals -->
                    <v-card>
                        <v-card-title>운동 정보 입력</v-card-title>
                        <v-divider></v-divider>
                        <v-card-text>
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
                        <v-select
                            label="대분류"
                            outlined
                            required
                            :items="catLarge"
                            v-model="form.large"
                        ></v-select>
                        <v-select
                            label="중분류"
                            outlined
                            required
                            :items="catMid"
                            v-model="form.mid"
                        ></v-select>
                        <v-text-field
                            required
                            label="종류"
                            outlined
                            v-model="form.small"
                            hint="벤치프레스, 스쿼트, 풀업..." 
                        >
                        </v-text-field>
                        <validation-observer
                            ref="observer"
                        >
                        <div
                            v-for="(value, i) in setFields"
                            :key="i"
                        >
                            <v-row>
                                <v-col cols="4">
                                <validation-provider
                                        v-slot="{ errors }"
                                        rules="required"
                                        name ="무게"
                                >
                                    <v-text-field
                                        placeholder="무게"
                                        required
                                        :error-messages="errors"
                                        :label="value.lab1"
                                        v-model="value.weight"
                                    >
                                    </v-text-field>
                                </validation-provider>
                                </v-col>
                                <v-col cols="4">
                                <validation-provider
                                    v-slot="{ errors }"
                                    rules="required"
                                    name ="단위"
                                >
                                    <v-select
                                        label="단위"
                                        :items="weightunit"
                                        :error-messages="errors"
                                        v-model="value.unit"
                                    >
                                    </v-select>
                                </validation-provider>
                                </v-col>
                                <v-col cols="4">
                                <validation-provider
                                    v-slot="{ errors }"
                                    rules="required"
                                    name ="반복횟수"
                                >
                                    <v-text-field
                                        placeholder="횟수"
                                        required
                                        :error-messages="errors"
                                        :label="value.lab2"
                                        v-model="value.reps"
                                    >
                                    </v-text-field>
                                </validation-provider>
                                </v-col>
                                <v-col cols="6">
                                    <v-btn text 
                                        @click="removeSet(i)"
                                        color="error"
                                        small
                                        plain
                                >set {{i+1}}</v-btn>
                                </v-col>
                            </v-row>
                        <v-divider></v-divider>
                        </div>
                    
                    </validation-observer>
                    <span>
                        <v-alert
                            v-if="diaryNotFilled"
                            color="red lighten-2"
                            prominent
                            dense
                            type="error"
                            elevation=2
                        >
                            {{warningMsg}}
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
                </v-card-text>
                <v-card-actions>
                    <v-spacer>
                    </v-spacer>
                    <v-btn
                        color="red darken-1"
                        text
                        @click="dialog=false"
                    >
                        취소
                    </v-btn>
                    <v-btn 
                        class="ma-2 " 
                        color="blue darken-1"
                        text
                        @click="addSet">
                    
                        세트 추가
                    </v-btn>
                    <v-btn 
                        class="ma-2 white--text" 
                        color="blue darken-1"
                        text
                        @click="submit"
                    >
                        저장
                    </v-btn> 
                </v-card-actions>
                </v-card>
            </v-dialog>
        </v-row>
        </v-form>
    </v-app>
</template>
<script>
import {mapActions} from 'vuex'
// import axios from 'axios'
import myMixin from '../../mixins/index'
export default {
    mixins:[myMixin],
    data: () => ({
        catLarge:['케이블','머신','바벨','덤벨','맨몸'],
        catMid:['가슴','등','어깨', '이두','삼두','하체','코어'],
        catSmall:'',
        weightunit: ['kg','lb','sec'],
        form:{
            date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
            large:'',
            mid:'',
            small:'',
            weight:'',
            unit:'',
            reps:'',
        },
        dialog:false,
        menu2: false,
        setFields:[],
        diaryNotFilled: false,
        diarySuccess: false,
        warningMsg:'',
    }),
    
    methods:{
        ...mapActions(['submitRecords']),
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

                for (var j=0; j < this.setFields.length; j++){
                    this.form.weight = this.form.weight + this.setFields[j]['weight'] + " "
                    this.form.unit = this.form.unit + this.setFields[j]['unit'] + " "
                    this.form.reps = this.form.reps + this.setFields[j]['reps'] + " "
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
                await this.submitRecords(submitData)
                .then(
                    this.setFields= [],
                    this.form.weight= "",
                    this.form.unit="",
                    this.form.reps=""

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
                this.dialog=false
                // 화면 새로고침
                window.location.reload();
            }
        },
        addSet(){
            this.setFields.push({
                lab1:'weight',
                weight:"",
                lab2:"reps",
                reps:"",
                unit:""
            })
        },
        removeSet(index){
            this.setFields.splice(index,1)
        }
    },
    
}

</script>

