<template>
  <div class='diary-chart'>
    
    <bar-chart>
    </bar-chart>
    <p>{{myData}}</p>
  </div>
</template>
<script>
import axios from 'axios'
import BarChart from "../BarChart.vue"
import moment from 'moment'
  export default {
    name: 'DiaryBarChart',
    components: {BarChart},
    data: () => ({
      loaded: false,
      chartData: null,
    }),
    props: [
      "data", // 시계열 데이터
      "color", // str, 차트 색상
      "legend", // str 차트 범례 바뀔 때 chartoption 변경
      "backdroup", //bool, true -> 차트 비활성화
      "empty", //bool , true -> 데이터 없음 레이어 띄움
      "yAxis"
    ],


  };

</script>