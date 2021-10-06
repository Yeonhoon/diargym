<template>
    <v-form >
        <v-select
            label="대분류"
            :items="catBig"
        ></v-select>
        <v-select
            label="중분류"
            :items="catMid"
        ></v-select>
        <v-select
            label="소분류"
            :items="catSmall"
        >

        </v-select>
        <v-text-field
            label="무게"
        >

        </v-text-field>
        <v-text-field
            label="rep"
        >
            
        </v-text-field>

    </v-form>
</template>
<script>
export default {
    data: () => ({
        catBig:['가슴','등','이두','삼두','하체','코어'],
        catMid:['케이블','머신','바벨','덤벨','맨몸'],
        catSmall:[]
    })
}

</script>