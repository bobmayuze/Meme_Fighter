<template>
  <div id="hack-detail-page">
    <template v-for="val,name in data_arr">
      <chart :dataHack="val" :title="name" :flage="change_flag"></chart>
    </template>
  </div>
</template>

<script>
  import {SET_DATA_ARR, SET_IMAGE_DATA, SET_IMAGE_DATA_NAME} from '@/store/mutation-types';
  import chart from '@/components/chart/detail_chart';
  export default {
    data() {
      return {
        data_arr:[],
        change_flag:true,
        val:{},
      }
    },
    components: {
      chart,
    },
    mounted () {
      this.data_arr = this.$store.getters.get_data_arr;
      var socket = io.connect('http://localhost:9090');
      socket.on('news', (data) => {
        if(Array.isArray(data.data_arr)) {
          data.data_arr.forEach((val, index) => {
            this.$store.dispatch(SET_DATA_ARR, {data_name:data.data_name[index], data_val:val});
          })
          this.$store.dispatch(SET_IMAGE_DATA, data.data_arr); //
          this.$store.dispatch(SET_IMAGE_DATA_NAME, data.data_name);
          this.change_flag = !this.change_flag;
          this.data_arr = [];
        }
      });
    },
    watch: {
      change_flag() {
        this.data_arr = this.$store.getters.get_data_arr;
      }
    },
  }
</script>