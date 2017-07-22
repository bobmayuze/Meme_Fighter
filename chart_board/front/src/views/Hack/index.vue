<template>
  <div id="hack-page">
    hack-page
    <template v-for="item in dataHack">
      {{item}}
    </template>
    <chart :dataHack="dataHack" :dataName="dataName"></chart>
  </div>
</template>

<script>
  import {SET_DATA_ARR, SET_IMAGE_DATA, SET_IMAGE_DATA_NAME} from '@/store/mutation-types';
  import chart from '@/components/chart/hack_chart';
  export default {
    data () {
      return {
        dataHack: this.$store.getters.get_image_data, //  [0,0,0,0],
        dataName:this.$store.getters.get_image_data_name //['no data', 'no data', 'no data', 'no data']
      }
    },
    components: {
      chart,
    },
    mounted () {
      this.dataHack = this.$store.getters.get_image_data; //  [0,0,0,0],
      this.dataName = this.$store.getters.get_image_data_name; //['no data', 'no data', 'no data', 'no data']
      var socket = io.connect('http://localhost:9090');
      socket.on('news', (data) => {
        if(Array.isArray(data.data_arr)) {
          this.dataHack = data.data_arr;
          this.dataName = data.data_name;
          this.dataHack.forEach((val, index) => {
            this.$store.dispatch(SET_DATA_ARR, {data_name:this.dataName[index], data_val:val});
          })
          this.$store.dispatch(SET_IMAGE_DATA, data.data_arr); //
          this.$store.dispatch(SET_IMAGE_DATA_NAME, data.data_name);
        }
      });
    },
  }
</script>