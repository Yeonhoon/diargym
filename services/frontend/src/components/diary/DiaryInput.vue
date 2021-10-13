<template>
    <v-app>
        <v-form>
            <v-row>
                <v-col cols="12" sm="5">
                    <v-date-picker 
                        v-model="form.date" 
                        elevation="10"
                        full-width    
                    >
                    </v-date-picker>
                </v-col>
                <v-col cols="12" sm="1"></v-col>
                <v-col cols="12" sm="6">
                    <div>
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
            </div>
            <br>
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
                    "운동기록 저장 성공!"
                </v-alert>

            </span>
            <validation-observer
                    ref="observer"
            >
            
                <div
                    v-for="(value, i) in setFields"
                    :key="i"
                >
                    <v-row>
                        <v-col cols="12" sm="1"></v-col>
                        <v-col cols="12" sm="3">
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
                        <v-col cols="12" sm="3">
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
                        <v-col cols="12" sm="3">
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
                        <v-col cols="12" sm="1" class="pt-7">
                            <v-btn text 
                                @click="removeSet(i)"
                                color="error"
                                small
                                plain
                        >set {{i+1}}</v-btn>
                        </v-col>
                    </v-row>
                </div>
                    
            </validation-observer>
            <div justify="space-around" align="center">
                <v-btn 
                    class="ma-2 " 
                    color="primary"
                    outlined
                    large
                    @click="addSet">세트 추가</v-btn>
                <v-btn 
                    class="ma-2 white--text" 
                    color="primary" 
                    large
                    @click="submit"
                ><v-icon left>mdi-pencil</v-icon>
                    저장
                </v-btn> 
                </div>
                </v-col>
            </v-row>
        </v-form>
    </v-app>
</template>
<script>
// import {mapActions} from 'vuex'
import axios from 'axios'
import myMixin from '../../mixins/index'
export default {
    mixins:[myMixin],
    data: () => ({
        catLarge:['케이블','머신','바벨','덤벨','맨몸'],
        catMid:['가슴','등','어깨', '이두','삼두','하체','코어'],
        catSmall:'',
        weightunit: ['kg','lb'],
        form:{
            date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
            large:'',
            mid:'',
            small:'',
            weight:'',
            unit:'',
            reps:'',
        },
        setFields:[],
        diaryNotFilled: false,
        diarySuccess: false,
        warningMsg:'',
    }),
    methods:{
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
                await axios.post('adddiary',{
                    'rdate': this.form.date,
                    'rlarge': this.form.large,
                    'rmid': this.form.mid,
                    'rsmall': this.form.small,
                    'rweight': this.form.weight,
                    'runit': this.form.unit,
                    'rrep': this.form.reps
                })
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
                }, 3000)
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
 // let diaryForm = new FormData();
            // diaryForm.append('rdate', this.form.date);
            // diaryForm.append('rlarge',this.form.large);
            // diaryForm.append('rmiddle',this.form.mid);
            // diaryForm.append('rsmall', this.form.small);
            // for(var i=0; i<this.setFields.length; i++){
            //     diaryForm.append('rweight',this.setFields[i]['weight'])
            //     diaryForm.append('rreps',this.setFields[i]['reps'])
            //     diaryForm.append('runit',this.setFields[i]['unit'])
            //     }
</script>

