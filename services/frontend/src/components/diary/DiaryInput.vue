<template>
    <v-app>
        <div>
            <v-select
                label="대분류"
                outlined
                required
                :items="catBig"
                v-model="big"
            ></v-select>
            <v-select
                label="중분류"
                outlined
                required
                :items="catMid"
                v-model="mid"
            ></v-select>
            <v-select
                label="소분류"
                outlined
                required
                :items="catSmall"
                v-model="small"
            >
            </v-select>
        </div>
        <br>
        <div
            v-for="(value, i) in setFields"
            :key="i"
        >
            <v-row>
                <v-col cols="12" sm="2" class="mt-2 mr-2">
                    <v-btn text disabled>set {{i+1}}</v-btn>
                </v-col>
                <v-col cols="12" sm="4">
                    <v-text-field
                        outlined
                        placeholder="무게"
                        :label="value.lab1"
                        v-model="value.weight"
                    >
                    </v-text-field>
                </v-col>
                <v-col cols="12" sm="4">
                    <v-text-field
                        outlined
                        placeholder="반복횟수"
                        :label="value.lab2"
                        v-model="value.reps"
                    >
                    </v-text-field>
                </v-col>
                <v-col cols="12" sm="1" >
                    <v-btn 
                        class="mt-3"
                        color="error"
                        rounded
                        outlined
                        plain
                        large
                        @click="removeSet(i)"
                    >
                        <v-icon>mdi-minus</v-icon>
                    </v-btn>
                </v-col>
            </v-row>
            <!-- TODO: 무게단위 checkbox -->
        </div>
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
    </v-app>
   
</template>
<script>
export default {
    data: () => ({
        catBig:['케이블','머신','바벨','덤벨','맨몸'],
        catMid:['가슴','등','이두','삼두','하체','코어','어깨'],
        catSmall:['3세트','4세트','5세트','장연훈바부'],
    
        big:'',
        mid:'',
        small:'',
        setFields:[],
    }),
    methods:{
        submit(){
            console.log(this.big)
        },
        addSet(){
            this.setFields.push({
                lab1:'weight',
                weight:"",
                lab2:"reps",
                reps:""

            })
        },
        removeSet(index){
            this.setFields.splice(index,1)
        }
    }
    
}

</script>