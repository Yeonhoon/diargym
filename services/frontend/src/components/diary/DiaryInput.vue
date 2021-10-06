<template>
    <v-app>
        <v-flex>
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
        <v-btn @click="submit">저장</v-btn>
        <v-btn @click="addSet">+</v-btn>
        </v-flex>
        <v-flex
            v-for="(value, i) in setFields"
            :key="i"
        >
            
            <v-row>
                <v-col cols="12" sm="1"><span>set {{i+1}}</span></v-col>
                <v-col cols="12" sm="5">
                    <v-text-field
                        outlined
                        placeholder="무게"
                        :label="value.lab1"
                        v-model="value.weight"
                    >
                    </v-text-field>

                </v-col>
                <v-col cols="12" sm="5">
                    <v-text-field
                        outlined
                        placeholder="반복횟수"
                        :label="value.lab2"
                        v-model="value.reps"
                    >
                    </v-text-field>
                </v-col>
                <v-col cols="12" sm="1">
                    <v-btn @click="removeSet(i)">-</v-btn>
                </v-col>
            </v-row>
            <!-- TODO: 단위 checkbox -->

        </v-flex>
    </v-app>
   
</template>
<script>
export default {
    data: () => ({
        catBig:['가슴','등','이두','삼두','하체','코어'],
        catMid:['케이블','머신','바벨','덤벨','맨몸'],
        catSmall:[],
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